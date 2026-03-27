"""sportly.nba — NBA Stats API client.

Base URL: https://stats.nba.com/stats/
No auth required, but WAF headers are mandatory on every request.
Response shape: resultSets[{name, headers[], rowSet[[]]}]
"""
from __future__ import annotations

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from sportly.exceptions import NotFoundError, RateLimitError, SportlyError

BASE_URL = "https://stats.nba.com/stats"

# WAF bypass headers — required on every request or NBA returns 403/empty
WAF_HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://www.nba.com",
    "Referer": "https://www.nba.com/",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "x-nba-stats-origin": "stats",
    "x-nba-stats-token": "true",
}

# League IDs
LEAGUE_NBA   = "00"
LEAGUE_WNBA  = "10"
LEAGUE_GLEAGUE = "20"

# Team IDs (abbrev → NBA numeric string ID)
TEAM_IDS: dict[str, str] = {
    "ATL": "1610612737", "BOS": "1610612738", "BKN": "1610612751",
    "CHA": "1610612766", "CHI": "1610612741", "CLE": "1610612739",
    "DAL": "1610612742", "DEN": "1610612743", "DET": "1610612765",
    "GSW": "1610612744", "HOU": "1610612745", "IND": "1610612754",
    "LAC": "1610612746", "LAL": "1610612747", "MEM": "1610612763",
    "MIA": "1610612748", "MIL": "1610612749", "MIN": "1610612750",
    "NOP": "1610612740", "NYK": "1610612752", "OKC": "1610612760",
    "ORL": "1610612753", "PHI": "1610612755", "PHX": "1610612756",
    "POR": "1610612757", "SAC": "1610612758", "SAS": "1610612759",
    "TOR": "1610612761", "UTA": "1610612762", "WAS": "1610612764",
}

# Notable player IDs
PLAYER_IDS: dict[str, str] = {
    "LeBron James":            "2544",
    "Stephen Curry":           "201939",
    "Kevin Durant":            "201142",
    "Nikola Jokic":            "203999",
    "Giannis Antetokounmpo":   "203507",
    "Luka Doncic":             "1629029",
    "Ja Morant":               "1629630",
    "Jayson Tatum":            "1628369",
    "Shai Gilgeous-Alexander": "1628983",
    "Victor Wembanyama":       "1641705",
}


def parse_result_sets(data: dict) -> dict[str, list[dict]]:
    """Convert NBA resultSets (headers + rowSet arrays) → list of dicts.

    Returns ``{DataSetName: [{col: val, ...}, ...]}``.
    """
    out: dict[str, list[dict]] = {}
    for rs in data.get("resultSets", []):
        headers = rs.get("headers", [])
        rows = rs.get("rowSet", [])
        out[rs["name"]] = [dict(zip(headers, row, strict=False)) for row in rows]
    return out


class NBAClient:
    """HTTP client for stats.nba.com with WAF headers and retry."""

    def __init__(self, timeout: float = 15.0) -> None:
        self._http = httpx.Client(headers=WAF_HEADERS, timeout=timeout)

    @retry(
        retry=retry_if_exception_type(httpx.TransportError),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        reraise=True,
    )
    def get(self, endpoint: str, **params) -> dict:
        url = f"{BASE_URL}/{endpoint}"
        try:
            resp = self._http.get(url, params={k: v for k, v in params.items() if v is not None})
        except httpx.TransportError as exc:
            raise SportlyError(str(exc)) from exc
        if resp.status_code == 404:
            raise NotFoundError(f"Not found: {url}", status_code=404, url=url)
        if resp.status_code == 429:
            raise RateLimitError("NBA rate limited", status_code=429)
        resp.raise_for_status()
        return resp.json()

    def close(self) -> None:
        self._http.close()

    def __enter__(self): return self
    def __exit__(self, *_): self.close()


_default: NBAClient | None = None

def get_client() -> NBAClient:
    global _default
    if _default is None:
        _default = NBAClient()
    return _default
