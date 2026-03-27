"""Base HTTP client shared by all sportly data sources.

All upstream calls go through SportlyClient which provides:
- Automatic retries with exponential backoff (via tenacity)
- Configurable timeouts
- Consistent error mapping
- Structured logging
"""

from __future__ import annotations

from typing import Any

import httpx
import structlog
from tenacity import (
    RetryError,
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

from sportly.exceptions import (
    NotFoundError,
    ParseError,
    RateLimitError,
    SportlyError,
    UpstreamError,
)

logger = structlog.get_logger(__name__)

_DEFAULT_TIMEOUT = 30.0
_DEFAULT_MAX_RETRIES = 3
_DEFAULT_BACKOFF = 1.0
_DEFAULT_USER_AGENT = "sportly/1.0 (https://github.com/pseudo-r/sportly)"


class SportlyClient:
    """Shared HTTP client with retry logic and error mapping.

    Instantiated once per data-source module and reused across calls.
    Thread-safe for concurrent use (httpx.Client is thread-safe).

    Parameters
    ----------
    timeout:
        Request timeout in seconds (default 30).
    max_retries:
        Number of retry attempts for transient errors (default 3).
    backoff:
        Multiplier for exponential backoff between retries (default 1.0 s).
    user_agent:
        Value sent in the User-Agent header.

    Examples
    --------
    ::

        client = SportlyClient()
        data = client.get("https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams")
    """

    def __init__(
        self,
        *,
        timeout: float = _DEFAULT_TIMEOUT,
        max_retries: int = _DEFAULT_MAX_RETRIES,
        backoff: float = _DEFAULT_BACKOFF,
        user_agent: str = _DEFAULT_USER_AGENT,
    ) -> None:
        self._timeout = timeout
        self._max_retries = max_retries
        self._backoff = backoff
        self._http: httpx.Client | None = None
        self._headers = {
            "User-Agent": user_agent,
            "Accept": "application/json",
        }

    # ── Lifecycle ────────────────────────────────────────────────────────────

    @property
    def http(self) -> httpx.Client:
        """Lazily initialised httpx client."""
        if self._http is None or self._http.is_closed:
            self._http = httpx.Client(
                timeout=httpx.Timeout(self._timeout),
                headers=self._headers,
                follow_redirects=True,
            )
        return self._http

    def close(self) -> None:
        """Close the underlying HTTP client."""
        if self._http and not self._http.is_closed:
            self._http.close()
            self._http = None

    def __enter__(self) -> SportlyClient:
        return self

    def __exit__(self, *_: Any) -> None:
        self.close()

    # ── Request ──────────────────────────────────────────────────────────────

    def get(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Perform a GET request and return the parsed JSON body.

        Retries on transient network errors and 5xx responses.
        Raises a :class:`~sportly.exceptions.SportlyError` subclass on failure.
        """

        @retry(
            retry=retry_if_exception_type((httpx.TransportError, UpstreamError)),
            stop=stop_after_attempt(self._max_retries),
            wait=wait_exponential(multiplier=self._backoff, min=1, max=10),
            reraise=True,
        )
        def _attempt() -> dict[str, Any]:
            logger.debug("sportly.request", url=url, params=params)
            try:
                response = self.http.request("GET", url, params=params)
            except httpx.TransportError as exc:
                logger.warning("sportly.transport_error", url=url, error=str(exc))
                raise

            return self._handle(response, url)

        try:
            return _attempt()
        except RetryError as exc:
            raise SportlyError(
                f"Request failed after {self._max_retries} retries: {url}",
                url=url,
            ) from exc
        except (NotFoundError, RateLimitError):
            raise
        except httpx.TransportError as exc:
            raise SportlyError(f"Connection error: {exc}", url=url) from exc

    # ── Response Handling ────────────────────────────────────────────────────

    def _handle(self, response: httpx.Response, url: str) -> dict[str, Any]:
        """Map HTTP status codes to sportly exceptions."""
        code = response.status_code

        if code == 404:
            raise NotFoundError(f"Resource not found: {url}", status_code=404, url=url)

        if code == 429:
            raise RateLimitError("Rate limit exceeded", status_code=429, url=url)

        if code >= 500:
            raise UpstreamError(
                f"Upstream server error {code}", status_code=code, url=url
            )

        if code >= 400:
            raise SportlyError(
                f"Client error {code}: {url}", status_code=code, url=url
            )

        try:
            return response.json()  # type: ignore[no-any-return]
        except Exception as exc:
            raise ParseError(f"Failed to parse JSON from {url}: {exc}", url=url) from exc


# Module-level default client — can be replaced for testing
_default_client: SportlyClient | None = None


def get_client() -> SportlyClient:
    """Return the shared default :class:`SportlyClient` instance."""
    global _default_client  # noqa: PLW0603
    if _default_client is None:
        _default_client = SportlyClient()
    return _default_client


def set_client(client: SportlyClient) -> None:
    """Replace the default client (useful for testing with mocks)."""
    global _default_client  # noqa: PLW0603
    _default_client = client
