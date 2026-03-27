"""sportly.nba.endpoints.league — Standings, leaders, draft."""
from __future__ import annotations
from typing import Any
from sportly.nba._client import NBAClient, LEAGUE_NBA, parse_result_sets, get_client


def standings(
    season: str,
    *,
    season_type: str = "Regular Season",
    league_id: str = LEAGUE_NBA,
    client: NBAClient | None = None,
) -> list[dict[str, Any]]:
    """Return league standings (v3).

    Parameters
    ----------
    season: ``"2024-25"`` format.

    Example
    -------
    ::

        rows = league.standings("2024-25")
        for team in rows:
            print(team["TeamName"], team["WINS"], team["LOSSES"])
    """
    http = client or get_client()
    data = http.get(
        "leaguestandingsv3",
        LeagueID=league_id,
        Season=season,
        SeasonType=season_type,
    )
    rs = parse_result_sets(data)
    return rs.get("Standings", [])  # type: ignore[return-value]


def leaders(
    stat: str = "PTS",
    *,
    season: str = "2024-25",
    season_type: str = "Regular Season",
    scope: str = "S",
    per_mode: str = "PerGame",
    league_id: str = LEAGUE_NBA,
    client: NBAClient | None = None,
) -> list[dict[str, Any]]:
    """Return league scoring/stat leaders.

    Parameters
    ----------
    stat:    ``"PTS"``, ``"REB"``, ``"AST"``, ``"STL"``, ``"BLK"``, ``"FG_PCT"``.
    scope:   ``"S"`` = season (default), ``"RS"`` = rookies.

    Example
    -------
    ::

        top_scorers = league.leaders("PTS", season="2024-25")
    """
    http = client or get_client()
    data = http.get(
        "leagueleaders",
        LeagueID=league_id,
        PerMode=per_mode,
        Scope=scope,
        Season=season,
        SeasonType=season_type,
        StatCategory=stat,
    )
    rs = parse_result_sets(data)
    return rs.get("LeagueLeaders", [])  # type: ignore[return-value]


def draft(
    season: str,
    *,
    league_id: str = LEAGUE_NBA,
    client: NBAClient | None = None,
) -> list[dict[str, Any]]:
    """Return draft history for a season.

    Parameters
    ----------
    season: Season end year as 4-digit string e.g. ``"2024"``.
    """
    http = client or get_client()
    data = http.get("drafthistory", LeagueID=league_id, Season=season)
    rs = parse_result_sets(data)
    return rs.get("DraftHistory", [])  # type: ignore[return-value]
