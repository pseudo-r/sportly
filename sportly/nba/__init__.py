"""sportly.nba — NBA Stats API.

Base URL: https://stats.nba.com/stats/
WAF headers are injected automatically on every request.
Responses use ``resultSets`` row-as-array format (automatically parsed to dicts).

Usage::

    from sportly import nba

    sb  = nba.scoreboard("2025-03-26")          # today's games
    log = nba.game_log("2544", "2024-25")        # LeBron game log
    top = nba.leaders("PTS")                     # scoring leaders
    st  = nba.standings("2024-25")               # full standings
    shots = nba.shot_chart("201939", "2024-25")  # Curry shot chart

    print(nba.TEAM_IDS)    # {"LAL": "1610612747", ...}
    print(nba.PLAYER_IDS)  # {"LeBron James": "2544", ...}
"""
from __future__ import annotations
from typing import Any

from sportly.nba._client import (
    LEAGUE_NBA, LEAGUE_WNBA, LEAGUE_GLEAGUE,
    PLAYER_IDS, TEAM_IDS, NBAClient, get_client,
)
from sportly.nba.endpoints import games as _games_ep
from sportly.nba.endpoints import league as _league_ep
from sportly.nba.endpoints import players as _players_ep
from sportly.nba.endpoints import teams as _teams_ep

__all__ = [
    "TEAM_IDS", "PLAYER_IDS", "LEAGUE_NBA", "LEAGUE_WNBA", "LEAGUE_GLEAGUE",
    "scoreboard", "boxscore", "play_by_play", "win_probability",
    "teams", "team_stats", "roster",
    "player", "career_stats", "game_log", "shot_chart",
    "standings", "leaders", "draft",
]

# ── Games ─────────────────────────────────────────────────────────────────────

def scoreboard(date: str, *, league_id: str = LEAGUE_NBA, client: NBAClient | None = None) -> dict[str, list[dict[str, Any]]]:
    """Today's scores. Returns ``{GameHeader: [...], LineScore: [...], ...}``."""
    return _games_ep.scoreboard(date, league_id=league_id, client=client)

def boxscore(game_id: str, *, client: NBAClient | None = None) -> dict[str, Any]:
    """Full traditional boxscore for a game (v3)."""
    return _games_ep.boxscore(game_id, client=client)

def play_by_play(game_id: str, *, client: NBAClient | None = None) -> list[dict[str, Any]]:
    """Play-by-play events for a game (v3)."""
    return _games_ep.play_by_play(game_id, client=client)

def win_probability(game_id: str, *, client: NBAClient | None = None) -> list[dict[str, Any]]:
    """Win probability by play."""
    return _games_ep.win_probability(game_id, client=client)

# ── Teams ─────────────────────────────────────────────────────────────────────

def teams(*, league_id: str = LEAGUE_NBA, client: NBAClient | None = None) -> list[dict[str, Any]]:
    """All NBA teams."""
    return _teams_ep.all(league_id=league_id, client=client)

def team_stats(team_id: str, season: str, *, per_mode: str = "PerGame", client: NBAClient | None = None) -> dict[str, Any]:
    """Season stats summary for a team. ``per_mode``: ``"PerGame"``, ``"Totals"``."""
    return _teams_ep.stats(team_id, season, per_mode=per_mode, client=client)

def roster(team_id: str, season: str, *, client: NBAClient | None = None) -> list[dict[str, Any]]:
    """Current roster for a team."""
    return _teams_ep.roster(team_id, season, client=client)

# ── Players ───────────────────────────────────────────────────────────────────

def player(player_id: str | int, *, client: NBAClient | None = None) -> dict[str, Any]:
    """Biographical info for a player."""
    return _players_ep.info(player_id, client=client)

def career_stats(player_id: str | int, *, per_mode: str = "PerGame", client: NBAClient | None = None) -> dict[str, list[dict[str, Any]]]:
    """Full career stats for a player. Key: ``SeasonTotalsRegularSeason``."""
    return _players_ep.career_stats(player_id, per_mode=per_mode, client=client)

def game_log(player_id: str | int, season: str, *, season_type: str = "Regular Season", client: NBAClient | None = None) -> list[dict[str, Any]]:
    """Game-by-game log for a player. ``season``: ``"2024-25"``."""
    return _players_ep.game_log(player_id, season, season_type=season_type, client=client)

def shot_chart(player_id: str | int, season: str, *, client: NBAClient | None = None) -> list[dict[str, Any]]:
    """Shot chart (X/Y coords + make/miss). Filter by ``SHOT_MADE_FLAG``."""
    return _players_ep.shot_chart(player_id, season, client=client)

# ── League ────────────────────────────────────────────────────────────────────

def standings(season: str, *, season_type: str = "Regular Season", client: NBAClient | None = None) -> list[dict[str, Any]]:
    """Full league standings. ``season``: ``"2024-25"``."""
    return _league_ep.standings(season, season_type=season_type, client=client)

def leaders(stat: str = "PTS", *, season: str = "2024-25", client: NBAClient | None = None) -> list[dict[str, Any]]:
    """League leaders. ``stat``: ``"PTS"``, ``"REB"``, ``"AST"``, ``"STL"``, ``"BLK"``."""
    return _league_ep.leaders(stat, season=season, client=client)

def draft(season: str, *, client: NBAClient | None = None) -> list[dict[str, Any]]:
    """Draft history for a season (year e.g. ``"2024"``)."""
    return _league_ep.draft(season, client=client)
