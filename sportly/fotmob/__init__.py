"""sportly.fotmob — FotMob public API.

Base URL: https://www.fotmob.com/api/
No auth required. No versioning — all endpoints under /api/.
Unique features: xG, xA, momentum graphs, player ratings, shot maps.

Usage::

    from sportly import fotmob

    # Today's matches
    day = fotmob.matches("20260326")

    # Match detail (lineups, stats, incidents, xG)
    m = fotmob.match(4310531)

    # Premier League table (league ID 47)
    epl = fotmob.league(47)

    # Man City squad + results
    city = fotmob.team(8456)

    # De Bruyne profile
    player = fotmob.player(174543)

    # Search
    results = fotmob.search("messi")

    # Browse leagues
    all_leagues = fotmob.all_leagues()

    print(fotmob.LEAGUES)   # popular league IDs
"""
from __future__ import annotations
from typing import Any

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential
from sportly.exceptions import NotFoundError, RateLimitError, SportlyError

BASE_URL = "https://www.fotmob.com/api"

# ── Popular league IDs (numeric) ──────────────────────────────────────────────
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
    "Primera División":  239,  # Argentina
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

# ── Client ────────────────────────────────────────────────────────────────────

class FotMobClient:
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
    def get(self, endpoint: str, **params) -> Any:
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

    def __enter__(self): return self
    def __exit__(self, *_): self.close()


_default: FotMobClient | None = None

def _get_client() -> FotMobClient:
    global _default
    if _default is None:
        _default = FotMobClient()
    return _default


# ── Public API ────────────────────────────────────────────────────────────────

def matches(date: str, *, client: FotMobClient | None = None) -> dict[str, Any]:
    """Return all matches for a date.

    Parameters
    ----------
    date: ``YYYYMMDD`` format (e.g. ``"20260326"``).

    Returns a large payload with ``leagues[].matches[]``.
    """
    return (client or _get_client()).get("matches", date=date)  # type: ignore[return-value]


def match(match_id: int | str, *, client: FotMobClient | None = None) -> dict[str, Any]:
    """Return full match details: lineups, incidents, stats, xG, player ratings.

    Parameters
    ----------
    match_id: FotMob match ID (from ``matches()`` → ``leagues[].matches[].id``).
    """
    return (client or _get_client()).get("matchDetails", matchId=match_id)  # type: ignore[return-value]


def league(league_id: int | str, *, client: FotMobClient | None = None) -> dict[str, Any]:
    """Return league data: standing table, recent results, upcoming fixtures.

    Parameters
    ----------
    league_id: FotMob numeric league ID. See ``fotmob.LEAGUES`` for commons.

    Example
    -------
    ::

        epl = fotmob.league(47)   # Premier League
        table = epl["table"][0]["data"]["table"]["all"]
    """
    return (client or _get_client()).get("leagues", id=league_id)  # type: ignore[return-value]


def team(team_id: int | str, *, client: FotMobClient | None = None) -> dict[str, Any]:
    """Return team profile, squad, recent fixtures, and season stats.

    Parameters
    ----------
    team_id: FotMob numeric team ID (e.g. ``8456`` = Man City).
    """
    return (client or _get_client()).get("teams", id=team_id)  # type: ignore[return-value]


def player(player_id: int | str, *, client: FotMobClient | None = None) -> dict[str, Any]:
    """Return player profile, career stats, season stats, and recent matches.

    Parameters
    ----------
    player_id: FotMob numeric player ID (e.g. ``174543`` = De Bruyne).
    """
    return (client or _get_client()).get("playerData", id=player_id)  # type: ignore[return-value]


def search(term: str, *, client: FotMobClient | None = None) -> dict[str, Any]:
    """Search for teams, players, and tournaments.

    Returns ``{squad: [...], team: [...], tournament: [...]}``.
    """
    return (client or _get_client()).get("searchData", term=term)  # type: ignore[return-value]


def all_leagues(*, client: FotMobClient | None = None) -> dict[str, Any]:
    """Return all available leagues and tournaments tracked by FotMob."""
    return (client or _get_client()).get("allLeagues")  # type: ignore[return-value]


def tv_listings(*, date: str | None = None, client: FotMobClient | None = None) -> dict[str, Any]:
    """Return TV / broadcast listings for upcoming matches.

    Parameters
    ----------
    date: ``YYYYMMDD`` (optional, defaults to today).
    """
    return (client or _get_client()).get("tvlistings", date=date)  # type: ignore[return-value]


def world_news(*, client: FotMobClient | None = None) -> dict[str, Any]:
    """Return global football news feed."""
    return (client or _get_client()).get("worldnews")  # type: ignore[return-value]


def transfers(*, client: FotMobClient | None = None) -> dict[str, Any]:
    """Return recent transfer news and rumours."""
    return (client or _get_client()).get("transfers")  # type: ignore[return-value]
