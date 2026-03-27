"""ESPN teams endpoint functions."""

from __future__ import annotations

from typing import Any

from sportly.client import SportlyClient, get_client
from sportly.espn._domains import ESPNDomain, build_url
from sportly.espn._parse import parse_athlete, parse_team
from sportly.models import Athlete, Team


def all(
    sport: str,
    league: str,
    *,
    limit: int = 100,
    client: SportlyClient | None = None,
) -> list[Team]:
    """Return all teams for a sport/league."""
    http = client or get_client()
    url = build_url(ESPNDomain.SITE, f"sports/{sport}/{league}/teams")
    data = http.get(url, params={"limit": limit})
    raw_teams = (
        data.get("sports", [{}])[0]
            .get("leagues", [{}])[0]
            .get("teams", [])
    )
    return [parse_team(t) for t in raw_teams]


def one(
    sport: str,
    league: str,
    team_id: str,
    *,
    client: SportlyClient | None = None,
) -> Team:
    """Return a single team by ESPN team ID."""
    http = client or get_client()
    url = build_url(ESPNDomain.SITE, f"sports/{sport}/{league}/teams/{team_id}")
    data = http.get(url)
    return parse_team(data.get("team", data))


def roster(
    sport: str,
    league: str,
    team_id: str,
    *,
    client: SportlyClient | None = None,
) -> list[Athlete]:
    """Return the full roster for a team."""
    http = client or get_client()
    url = build_url(ESPNDomain.SITE, f"sports/{sport}/{league}/teams/{team_id}/roster")
    data = http.get(url)
    raw: list[dict[str, Any]] = []
    for group in data.get("athletes", []):
        if isinstance(group, dict):
            raw.extend(group.get("items", []))
        elif isinstance(group, list):
            raw.extend(group)
    return [parse_athlete(a) for a in raw]
