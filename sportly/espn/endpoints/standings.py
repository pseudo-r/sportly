"""ESPN standings and rankings endpoint functions."""

from __future__ import annotations

from typing import Any

from sportly.client import SportlyClient, get_client
from sportly.espn._domains import ESPNDomain, build_url
from sportly.espn._parse import parse_standings
from sportly.models import Standings


def standings(
    sport: str,
    league: str,
    *,
    season: int | None = None,
    domain: ESPNDomain = ESPNDomain.SITE_V2,
    client: SportlyClient | None = None,
) -> Standings:
    """Return league standings.

    Parameters
    ----------
    sport:   ESPN sport slug.
    league:  League slug.
    season:  Season year (e.g. ``2024``). Omit for current.
    domain:  Defaults to ``ESPNDomain.SITE_V2`` which returns full standings.
             ``ESPNDomain.SITE`` returns a stub for most sports.
             Rugby Union requires ``ESPNDomain.CORE``.
    """
    http = client or get_client()
    url = build_url(domain, f"sports/{sport}/{league}/standings")
    params: dict[str, Any] = {}
    if season:
        params["season"] = season
    data = http.get(url, params=params)
    return parse_standings(data)


def rankings(
    sport: str,
    league: str,
    *,
    client: SportlyClient | None = None,
) -> list[dict[str, Any]]:
    """Return poll rankings (college sports only)."""
    http = client or get_client()
    url = build_url(ESPNDomain.SITE, f"sports/{sport}/{league}/rankings")
    data = http.get(url)
    return data.get("rankings", [])  # type: ignore[return-value]
