"""ESPN athlete endpoint functions."""

from __future__ import annotations

from typing import Any

from sportly.client import SportlyClient, get_client
from sportly.espn._domains import ESPNDomain, build_url
from sportly.espn._parse import parse_athlete
from sportly.models import Athlete


def athlete(
    sport: str,
    league: str,
    athlete_id: str | int,
    *,
    domain: ESPNDomain = ESPNDomain.CORE,
    client: SportlyClient | None = None,
) -> Athlete:
    """Return a single athlete profile.

    Parameters
    ----------
    domain: ``ESPNDomain.CORE`` (v2, default) or ``ESPNDomain.CORE_V3`` (enriched).
    """
    http = client or get_client()
    url = build_url(domain, f"sports/{sport}/leagues/{league}/athletes/{athlete_id}")
    return parse_athlete(http.get(url))


def overview(
    sport: str,
    league: str,
    athlete_id: str | int,
    *,
    client: SportlyClient | None = None,
) -> dict[str, Any]:
    """Stats snapshot, next game, and news for an athlete (web/v3).

    .. note:: Soccer returns minimal data from this endpoint.
    """
    http = client or get_client()
    url = build_url(ESPNDomain.WEB_V3, f"sports/{sport}/{league}/athletes/{athlete_id}/overview")
    return http.get(url)  # type: ignore[return-value]


def stats(
    sport: str,
    league: str,
    athlete_id: str | int,
    *,
    client: SportlyClient | None = None,
) -> dict[str, Any]:
    """Season statistics for an athlete (web/v3).

    Works for NFL, NBA, NHL, MLB. Returns 404 for Soccer.
    """
    http = client or get_client()
    url = build_url(ESPNDomain.WEB_V3, f"sports/{sport}/{league}/athletes/{athlete_id}/stats")
    return http.get(url)  # type: ignore[return-value]


def gamelog(
    sport: str,
    league: str,
    athlete_id: str | int,
    *,
    client: SportlyClient | None = None,
) -> dict[str, Any]:
    """Game-by-game log for an athlete (web/v3)."""
    http = client or get_client()
    url = build_url(ESPNDomain.WEB_V3, f"sports/{sport}/{league}/athletes/{athlete_id}/gamelog")
    return http.get(url)  # type: ignore[return-value]


def splits(
    sport: str,
    league: str,
    athlete_id: str | int,
    *,
    client: SportlyClient | None = None,
) -> dict[str, Any]:
    """Home / away / opponent splits for an athlete (web/v3)."""
    http = client or get_client()
    url = build_url(ESPNDomain.WEB_V3, f"sports/{sport}/{league}/athletes/{athlete_id}/splits")
    return http.get(url)  # type: ignore[return-value]


def leaders(
    sport: str,
    league: str,
    *,
    season: int | None = None,
    client: SportlyClient | None = None,
) -> dict[str, Any]:
    """Statistical leaders from the core API."""
    http = client or get_client()
    base = f"sports/{sport}/leagues/{league}"
    path = f"{base}/seasons/{season}/leaders" if season else f"{base}/leaders"
    return http.get(build_url(ESPNDomain.CORE, path))  # type: ignore[return-value]


def stats_leaderboard(
    sport: str,
    league: str,
    *,
    category: str | None = None,
    limit: int = 50,
    client: SportlyClient | None = None,
) -> dict[str, Any]:
    """Athletes ranked by stat category (web/v3 byathlete endpoint)."""
    http = client or get_client()
    url = build_url(ESPNDomain.WEB_V3, f"sports/{sport}/{league}/statistics/byathlete")
    params: dict[str, Any] = {"limit": limit}
    if category:
        params["category"] = category
    return http.get(url, params=params)  # type: ignore[return-value]
