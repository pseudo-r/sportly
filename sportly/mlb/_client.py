"""sportly.mlb — MLB Stats API client.

Base URL: https://statsapi.mlb.com/api/v1/
No authentication required. v1 is the only active version.
"""

from __future__ import annotations

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from sportly.exceptions import NotFoundError, RateLimitError, SportlyError

BASE_URL = "https://statsapi.mlb.com/api/v1"

# ── Sport / League IDs ────────────────────────────────────────────────────────
SPORT_ID = 1          # MLB
LEAGUE_AL = 103       # American League
LEAGUE_NL = 104       # National League

# ── Known Team IDs ────────────────────────────────────────────────────────────
TEAM_IDS: dict[str, int] = {
    "LAA": 108, "ARI": 109, "BAL": 110, "BOS": 111, "CHC": 112,
    "CIN": 113, "CLE": 114, "COL": 115, "DET": 116, "HOU": 117,
    "KC":  118, "LAD": 119, "WSH": 120, "NYM": 121, "ATH": 133,
    "PIT": 134, "SD":  135, "SEA": 136, "SF":  137, "STL": 138,
    "TB":  139, "TEX": 140, "TOR": 141, "MIN": 142, "PHI": 143,
    "ATL": 144, "CWS": 145, "MIA": 146, "NYY": 147, "MIL": 158,
}

# ── Game type codes ───────────────────────────────────────────────────────────
GAME_TYPES = {"S": "Spring Training", "R": "Regular Season", "F": "Wild Card", "D": "Division Series", "L": "LCS", "W": "World Series"}


class MLBClient:
    """Thin HTTP client for statsapi.mlb.com.

    Handles retries and error mapping. All methods return raw dicts.
    """

    def __init__(self, timeout: float = 10.0) -> None:
        self._http = httpx.Client(
            headers={"Accept": "application/json"},
            timeout=timeout,
        )

    @retry(
        retry=retry_if_exception_type(httpx.TransportError),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=0.5, min=0.5, max=8),
        reraise=True,
    )
    def get(self, path: str, **params) -> dict:
        """GET {BASE_URL}/{path} with optional query params."""
        url = f"{BASE_URL}/{path.lstrip('/')}"
        try:
            resp = self._http.get(url, params={k: v for k, v in params.items() if v is not None})
        except httpx.TransportError as exc:
            raise SportlyError(str(exc)) from exc
        if resp.status_code == 404:
            raise NotFoundError(f"Not found: {url}", status_code=404, url=url)
        if resp.status_code == 429:
            raise RateLimitError("Rate limited by MLB Stats API", status_code=429)
        resp.raise_for_status()
        return resp.json()

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> "MLBClient":
        return self

    def __exit__(self, *_) -> None:
        self.close()


_default: MLBClient | None = None


def get_client() -> MLBClient:
    global _default
    if _default is None:
        _default = MLBClient()
    return _default
