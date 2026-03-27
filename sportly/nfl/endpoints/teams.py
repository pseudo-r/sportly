"""nfl.endpoints.teams — NFL team roster, schedule, depth chart."""
from __future__ import annotations

from typing import Any

from sportly.client import SportlyClient, get_client
from sportly.espn._domains import ESPNDomain, build_url
from sportly.espn.endpoints import teams as _espn_teams

SPORT  = "football"
LEAGUE = "nfl"


def all(*, limit: int = 32, client: SportlyClient | None = None) -> list[Any]:
    """All 32 NFL teams."""
    return _espn_teams.all(SPORT, LEAGUE, limit=limit, client=client)


def one(team_id: str | int, *, client: SportlyClient | None = None) -> Any:
    """Single NFL team by ESPN ID."""
    return _espn_teams.one(SPORT, LEAGUE, str(team_id), client=client)


def roster(team_id: str | int, *, client: SportlyClient | None = None) -> list[Any]:
    """Current roster for a team."""
    return _espn_teams.roster(SPORT, LEAGUE, str(team_id), client=client)


def schedule(
    team_id: str | int,
    *,
    season: int | None = None,
    season_type: int | None = None,
    client: SportlyClient | None = None,
) -> dict[str, Any]:
    """Full season schedule for a team."""
    http = client or get_client()
    qp = {k: v for k, v in {"season": season, "seasontype": season_type}.items() if v is not None}
    path = f"sports/{SPORT}/leagues/{LEAGUE}/teams/{team_id}/schedule"
    return http.get(build_url(ESPNDomain.SITE, path), params=qp)  # type: ignore[return-value]


def depth_chart(team_id: str | int, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """Depth chart for a team."""
    http = client or get_client()
    path = f"sports/{SPORT}/leagues/{LEAGUE}/teams/{team_id}/depthcharts"
    return http.get(build_url(ESPNDomain.SITE, path))  # type: ignore[return-value]
