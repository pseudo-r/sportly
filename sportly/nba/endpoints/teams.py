"""sportly.nba.endpoints.teams — Team info, roster, stats."""
from __future__ import annotations

from typing import Any

from sportly.nba._client import LEAGUE_NBA, NBAClient, get_client, parse_result_sets


def all(
    *,
    league_id: str = LEAGUE_NBA,
    client: NBAClient | None = None,
) -> list[dict[str, Any]]:
    """Return all NBA teams."""
    http = client or get_client()
    data = http.get("leagueteams", LeagueID=league_id)
    rs = parse_result_sets(data)
    return rs.get("LeagueTeams", [])  # type: ignore[return-value]


def stats(
    team_id: str,
    season: str,
    *,
    season_type: str = "Regular Season",
    per_mode: str = "PerGame",
    client: NBAClient | None = None,
) -> dict[str, Any]:
    """Return team season stats summary."""
    http = client or get_client()
    data = http.get(
        "teamdashboardbygeneralsplits",
        TeamID=team_id,
        Season=season,
        SeasonType=season_type,
        PerMode=per_mode,
        MeasureType="Base",
        PlusMinus="N",
        PaceAdjust="N",
        Rank="N",
        Outcome="",
        Location="",
        Month=0,
        SeasonSegment="",
        DateFrom="",
        DateTo="",
        OpponentTeamID=0,
        VsConference="",
        VsDivision="",
        GameSegment="",
        Period=0,
        ShotClockRange="",
        LastNGames=0,
    )
    rs = parse_result_sets(data)
    rows = rs.get("OverallTeamDashboard", [{}])
    return rows[0] if rows else {}  # type: ignore[return-value]


def roster(
    team_id: str,
    season: str,
    *,
    client: NBAClient | None = None,
) -> list[dict[str, Any]]:
    """Return the roster for a team in a given season."""
    http = client or get_client()
    data = http.get("commonteamroster", TeamID=team_id, Season=season)
    rs = parse_result_sets(data)
    return rs.get("CommonTeamRoster", [])  # type: ignore[return-value]
