"""sofascore.endpoints._client — shared HTTP helper."""
from __future__ import annotations

from typing import Any

BASE_URL = "https://api.sofascore.com/api/v1"

SPORTS: dict[str, str] = {
    "football":          "football",
    "soccer":            "football",
    "basketball":        "basketball",
    "tennis":            "tennis",
    "ice-hockey":        "ice-hockey",
    "hockey":            "ice-hockey",
    "baseball":          "baseball",
    "american-football": "american-football",
    "esports":           "esports",
    "table-tennis":      "table-tennis",
}


def get_curl_session():
    """Return a curl_cffi Chrome-impersonated session."""
    try:
        from curl_cffi import requests as cffi_requests  # type: ignore[import]
        return cffi_requests.Session(impersonate="chrome")
    except ImportError as exc:  # pragma: no cover
        raise ImportError(
            "sportly.sofascore requires curl_cffi for TLS fingerprint bypass.\n"
            "Install with: pip install sportly[sofascore]  "
            "or: pip install curl_cffi>=0.6"
        ) from exc


def get(path: str, *, client=None) -> Any:
    """Perform a GET request against the Sofascore v1 API."""
    from sportly.exceptions import NotFoundError, RateLimitError, SportlyError
    c = client or get_curl_session()
    url = f"{BASE_URL}/{path.lstrip('/')}"
    resp = c.get(url, headers={"Accept": "application/json, text/plain, */*"})
    if resp.status_code == 404:
        raise NotFoundError(f"Not found: {url}", status_code=404, url=url)
    if resp.status_code == 429:
        raise RateLimitError("Sofascore rate limited", status_code=429)
    if resp.status_code == 403:
        raise SportlyError(
            "Sofascore returned 403. curl_cffi impersonation may need updating.",
            status_code=403,
        )
    resp.raise_for_status()
    return resp.json()
