"""fotmob.endpoints._client — FotMob HTTP client."""
from __future__ import annotations
from typing import Any

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential
from sportly.exceptions import NotFoundError, RateLimitError, SportlyError

BASE_URL = "https://www.fotmob.com/api"

LEAGUES: dict[str, int] = {
    "Premier League":    47,
    "La Liga":           87,
    "Bundesliga":        54,
    "Serie A":           55,
    "Ligue 1":           53,
    "Eredivisie":        57,
    "Champions League":  42,
    "Europa League":     73,
    "Conference League": 10007,
    "MLS":               130,
    "Brasileirao":       268,
    "Liga MX":           208,
    "Primera División":  239,
    "World Cup":         77,
    "EURO":              50,
    "Copa America":      322,
    "Nations League":    931,
    "FA Cup":            132,
    "Carabao Cup":       133,
    "DFB-Pokal":         147,
    "Copa del Rey":      193,
    "Coppa Italia":      151,
}


class FotMobClient:
    """Stateless HTTP client for fotmob.com/api with retry logic."""

    def __init__(self, timeout: float = 10.0) -> None:
        self._http = httpx.Client(
            headers={
                "Accept": "application/json",
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/122.0.0.0 Safari/537.36"
                ),
                "Referer": "https://www.fotmob.com/",
            },
            timeout=timeout,
        )

    @retry(
        retry=retry_if_exception_type(httpx.TransportError),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=0.5, min=0.5, max=8),
        reraise=True,
    )
    def get(self, endpoint: str, **params: Any) -> Any:
        url = f"{BASE_URL}/{endpoint}"
        try:
            resp = self._http.get(url, params={k: v for k, v in params.items() if v is not None})
        except httpx.TransportError as exc:
            raise SportlyError(str(exc)) from exc
        if resp.status_code == 404:
            raise NotFoundError(f"Not found: {url}", status_code=404, url=url)
        if resp.status_code == 429:
            raise RateLimitError("FotMob rate limited", status_code=429)
        resp.raise_for_status()
        return resp.json()

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> "FotMobClient":
        return self

    def __exit__(self, *_: Any) -> None:
        self.close()


_default: FotMobClient | None = None


def get_client() -> FotMobClient:
    """Return the module-level default :class:`FotMobClient`."""
    global _default
    if _default is None:
        _default = FotMobClient()
    return _default
