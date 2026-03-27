"""sportly.mlb.endpoints.teams — Team and roster endpoints."""
from __future__ import annotations
from typing import Any
from sportly.mlb._client import MLBClient, SPORT_ID, get_client


def all(
    *,
    sport_id: int = SPORT_ID,
    season: int | None = None,
    league_ids: str | None = None,
    fields: str | None = None,
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return all MLB teams.

    Parameters
    ----------
    sport_id:   ``1`` = MLB (default), ``11`` = AAA, ``12`` = AA.
    season:     Filter to teams active in a specific year.
    league_ids: ``"103,104"`` for AL+NL.
    fields:     Comma-separated field list to trim response.
    """
    http = client or get_client()
    data = http.get("teams", sportId=sport_id, season=season, leagueIds=league_ids, fields=fields)
    return data.get("teams", [])  # type: ignore[return-value]


def one(
    team_id: int | str,
    *,
    season: int | None = None,
    fields: str | None = None,
    client: MLBClient | None = None,
) -> dict[str, Any]:
    """Return a single MLB team by ID (e.g. ``119`` = Dodgers)."""
    http = client or get_client()
    data = http.get(f"teams/{team_id}", season=season, fields=fields)
    teams = data.get("teams", [{}])
    return teams[0] if teams else {}  # type: ignore[return-value]


def roster(
    team_id: int | str,
    *,
    roster_type: str = "active",
    season: int | None = None,
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return the roster for a team.

    Parameters
    ----------
    roster_type: ``"active"`` (default), ``"40Man"``, ``"fullRoster"``.
    """
    http = client or get_client()
    data = http.get(f"teams/{team_id}/roster", rosterType=roster_type, season=season)
    return data.get("roster", [])  # type: ignore[return-value]


def stats(
    team_id: int | str,
    *,
    stats: str = "season",
    group: str = "hitting",
    season: int | None = None,
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return team stats.

    Parameters
    ----------
    stats: ``"season"``, ``"career"``, ``"yearByYear"``.
    group: ``"hitting"``, ``"pitching"``, ``"fielding"``.
    """
    http = client or get_client()
    data = http.get(f"teams/{team_id}/stats", stats=stats, group=group, season=season)
    return data.get("stats", [])  # type: ignore[return-value]
