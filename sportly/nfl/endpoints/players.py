"""nfl.endpoints.players — NFL athlete profiles, stats, and game logs."""
from __future__ import annotations
from typing import Any
from sportly.client import SportlyClient, get_client
from sportly.espn._domains import ESPNDomain, build_url
from sportly.espn.endpoints import athletes as _athletes

SPORT  = "football"
LEAGUE = "nfl"


def athlete(athlete_id: str | int, *, client: SportlyClient | None = None) -> Any:
    """Player profile by ESPN athlete ID."""
    return _athletes.athlete(SPORT, LEAGUE, athlete_id, client=client)


def stats(athlete_id: str | int, *, season: int | None = None, client: SportlyClient | None = None) -> dict[str, Any]:
    """Season statistics for a player."""
    return _athletes.stats(SPORT, LEAGUE, athlete_id, client=client)


def gamelog(athlete_id: str | int, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """Game-by-game log for a player."""
    return _athletes.gamelog(SPORT, LEAGUE, athlete_id, client=client)


def news(athlete_id: str | int, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """News articles about a player."""
    http = client or get_client()
    path = f"sports/{SPORT}/leagues/{LEAGUE}/athletes/{athlete_id}/news"
    return http.get(build_url(ESPNDomain.SITE, path))  # type: ignore[return-value]
