"""sportly.nba.endpoints.games — Scoreboard and game data."""
from __future__ import annotations
from typing import Any
from sportly.nba._client import NBAClient, LEAGUE_NBA, parse_result_sets, get_client


def scoreboard(
    date: str,
    *,
    league_id: str = LEAGUE_NBA,
    day_offset: int = 0,
    client: NBAClient | None = None,
) -> dict[str, list[dict[str, Any]]]:
    """Return today's scoreboard as ``{GameHeader: [...], LineScore: [...], ...}``.

    Parameters
    ----------
    date: ``YYYY-MM-DD`` format.

    Example
    -------
    ::

        sb = games.scoreboard("2025-03-26")
        for g in sb["GameHeader"]:
            print(g["GAMECODE"], g["GAME_STATUS_TEXT"])
    """
    http = client or get_client()
    data = http.get("scoreboardv2", GameDate=date, LeagueID=league_id, DayOffset=day_offset)
    return parse_result_sets(data)


def boxscore(
    game_id: str,
    *,
    start_period: int = 0,
    end_period: int = 10,
    range_type: int = 0,
    client: NBAClient | None = None,
) -> dict[str, list[dict[str, Any]]]:
    """Return traditional boxscore (v3 shape with named JSON objects).

    Parameters
    ----------
    game_id: 10-digit NBA game ID (e.g. ``"0022401045"``).
    """
    http = client or get_client()
    data = http.get(
        "boxscoretraditionalv3",
        GameID=game_id,
        StartPeriod=start_period,
        EndPeriod=end_period,
        RangeType=range_type,
        StartRange=0,
        EndRange=0,
    )
    # v3 returns named objects, not resultSets
    return data.get("boxScoreTraditional", data)  # type: ignore[return-value]


def play_by_play(
    game_id: str,
    *,
    start_period: int = 1,
    end_period: int = 10,
    client: NBAClient | None = None,
) -> list[dict[str, Any]]:
    """Return play-by-play events for a game (v3)."""
    http = client or get_client()
    data = http.get("playbyplayv3", GameID=game_id, StartPeriod=start_period, EndPeriod=end_period)
    pbp = data.get("game", {})
    return pbp.get("actions", [])  # type: ignore[return-value]


def win_probability(
    game_id: str, *, client: NBAClient | None = None
) -> list[dict[str, Any]]:
    """Return win probability by play."""
    http = client or get_client()
    data = http.get("winprobabilitypbp", GameID=game_id, RunType="each second")
    rs = parse_result_sets(data)
    return rs.get("WinProbPBP", [])  # type: ignore[return-value]
