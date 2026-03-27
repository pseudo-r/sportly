"""sportly.nba.endpoints.players — Player stats, career, game log, shot chart."""
from __future__ import annotations
from typing import Any
from sportly.nba._client import NBAClient, LEAGUE_NBA, parse_result_sets, get_client


def career_stats(
    player_id: str | int,
    *,
    per_mode: str = "PerGame",
    league_id: str = LEAGUE_NBA,
    client: NBAClient | None = None,
) -> dict[str, list[dict[str, Any]]]:
    """Return career stats for a player.

    Parameters
    ----------
    per_mode: ``"PerGame"`` (default), ``"Totals"``, ``"Per36"``.

    Example
    -------
    ::

        stats = players.career_stats("2544")  # LeBron
        for row in stats["SeasonTotalsRegularSeason"]:
            print(row["SEASON_ID"], row["PTS"])
    """
    http = client or get_client()
    data = http.get("playercareerstats", PlayerID=str(player_id), PerMode=per_mode, LeagueID=league_id)
    return parse_result_sets(data)


def game_log(
    player_id: str | int,
    season: str,
    *,
    season_type: str = "Regular Season",
    per_mode: str = "PerGame",
    league_id: str = LEAGUE_NBA,
    client: NBAClient | None = None,
) -> list[dict[str, Any]]:
    """Return game-by-game log for a player.

    Parameters
    ----------
    season: ``"2024-25"`` format.

    Example
    -------
    ::

        log = players.game_log("201939", "2024-25")  # Curry
        for g in log:
            print(g["MATCHUP"], g["PTS"])
    """
    http = client or get_client()
    data = http.get(
        "playergamelog",
        PlayerID=str(player_id),
        Season=season,
        SeasonType=season_type,
        PerMode=per_mode,
        LeagueID=league_id,
    )
    rs = parse_result_sets(data)
    return rs.get("PlayerGameLog", [])  # type: ignore[return-value]


def shot_chart(
    player_id: str | int,
    season: str,
    *,
    season_type: str = "Regular Season",
    team_id: str = "0",
    game_id: str = "",
    client: NBAClient | None = None,
) -> list[dict[str, Any]]:
    """Return shot chart data (X/Y coordinates + make/miss) for a player.

    Example
    -------
    ::

        shots = players.shot_chart("201142", "2024-25")  # Durant
        makes = [s for s in shots if s["SHOT_MADE_FLAG"] == 1]
    """
    http = client or get_client()
    data = http.get(
        "shotchartdetail",
        PlayerID=str(player_id),
        Season=season,
        SeasonType=season_type,
        TeamID=team_id,
        GameID=game_id,
        ContextMeasure="FGA",
        LeagueID="00",
    )
    rs = parse_result_sets(data)
    return rs.get("Shot_Chart_Detail", [])  # type: ignore[return-value]


def info(player_id: str | int, *, client: NBAClient | None = None) -> dict[str, Any]:
    """Return basic biographical info for a player."""
    http = client or get_client()
    data = http.get("commonplayerinfo", PlayerID=str(player_id))
    rs = parse_result_sets(data)
    rows = rs.get("CommonPlayerInfo", [{}])
    return rows[0] if rows else {}  # type: ignore[return-value]
