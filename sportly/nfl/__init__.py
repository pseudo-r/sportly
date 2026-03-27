"""sportly.nfl — NFL data via ESPN public APIs.

NFL's native api.nfl.com requires OAuth. All reliable, public NFL data
is served through ESPN's infrastructure (already used by sportly.espn).

Domains:
  - site.api.espn.com     → scoreboard, teams, rosters, injuries
  - sports.core.api.espn  → events, athletes, play-by-play, odds
  - cdn.espn.com          → CDN game packages (drives, win probability)

Usage::

    from sportly import nfl

    sb    = nfl.scoreboard(week=1, season=2024)
    t     = nfl.teams()
    pbp   = nfl.play_by_play("401671827")
    inj   = nfl.injuries()
    dc    = nfl.depth_chart("6")              # Cowboys
    sched = nfl.team_schedule("12", season=2024)  # Chiefs
    rating = nfl.qbr(season=2024)

    print(nfl.TEAM_IDS)   # {"KC": 12, "PHI": 21, ...}

Endpoint subpackage::

    from sportly.nfl.endpoints import games, teams, players, league
"""
from __future__ import annotations
from typing import Any
from sportly.client import SportlyClient

from sportly.nfl.endpoints import games as _games_ep
from sportly.nfl.endpoints import teams as _teams_ep
from sportly.nfl.endpoints import players as _players_ep
from sportly.nfl.endpoints import league as _league_ep

# ── Constants ─────────────────────────────────────────────────────────────────
SPORT  = "football"
LEAGUE = "nfl"

TEAM_IDS: dict[str, int] = {
    "ARI": 22, "ATL": 1,  "BAL": 33, "BUF": 2,  "CAR": 29, "CHI": 3,
    "CIN": 4,  "CLE": 5,  "DAL": 6,  "DEN": 7,  "DET": 8,  "GB":  9,
    "HOU": 34, "IND": 11, "JAX": 30, "KC":  12, "LV":  13, "LAC": 24,
    "LAR": 14, "MIA": 15, "MIN": 16, "NE":  17, "NO":  18, "NYG": 19,
    "NYJ": 20, "PHI": 21, "PIT": 23, "SF":  25, "SEA": 26, "TB":  27,
    "TEN": 10, "WSH": 28,
}

__all__ = [
    "TEAM_IDS", "SPORT", "LEAGUE",
    "scoreboard", "game", "cdn_game", "play_by_play", "odds",
    "teams", "team", "roster", "team_schedule", "depth_chart",
    "athlete", "athlete_stats", "athlete_gamelog", "athlete_news",
    "standings", "injuries", "transactions", "news", "qbr",
]


# ── Schedule / Games ──────────────────────────────────────────────────────────

def scoreboard(
    *,
    week: int | None = None,
    season: int | None = None,
    season_type: int | None = None,
    date: str | None = None,
    limit: int = 32,
    client: SportlyClient | None = None,
) -> list[dict[str, Any]]:
    """NFL scoreboard filtered by week, season, or date."""
    return _games_ep.scoreboard(week=week, season=season, season_type=season_type, date=date, limit=limit, client=client)


def game(game_id: str, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """Full game summary (boxscore, drives, scoring plays)."""
    return _games_ep.game(game_id, client=client)


def cdn_game(game_id: str, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """CDN game package (drives, win probability, odds)."""
    return _games_ep.cdn_game(game_id, client=client)


def play_by_play(event_id: str, *, limit: int = 300, client: SportlyClient | None = None) -> dict[str, Any]:
    """Play-by-play for a game (max 300 plays per page)."""
    return _games_ep.play_by_play(event_id, limit=limit, client=client)


def odds(event_id: str, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """Betting odds for a game."""
    return _games_ep.odds(event_id, client=client)


# ── Teams ─────────────────────────────────────────────────────────────────────

def teams(*, limit: int = 32, client: SportlyClient | None = None) -> list[Any]:
    """All 32 NFL teams."""
    return _teams_ep.all(limit=limit, client=client)


def team(team_id: str | int, *, client: SportlyClient | None = None) -> Any:
    """Single NFL team by ESPN ID (see ``nfl.TEAM_IDS``)."""
    return _teams_ep.one(team_id, client=client)


def roster(team_id: str | int, *, client: SportlyClient | None = None) -> list[Any]:
    """Current roster for a team."""
    return _teams_ep.roster(team_id, client=client)


def team_schedule(
    team_id: str | int,
    *,
    season: int | None = None,
    season_type: int | None = None,
    client: SportlyClient | None = None,
) -> dict[str, Any]:
    """Full season schedule for a team."""
    return _teams_ep.schedule(team_id, season=season, season_type=season_type, client=client)


def depth_chart(team_id: str | int, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """Depth chart for a team."""
    return _teams_ep.depth_chart(team_id, client=client)


# ── Players / Athletes ────────────────────────────────────────────────────────

def athlete(athlete_id: str | int, *, client: SportlyClient | None = None) -> Any:
    """Player profile by ESPN athlete ID."""
    return _players_ep.athlete(athlete_id, client=client)


def athlete_stats(athlete_id: str | int, *, season: int | None = None, client: SportlyClient | None = None) -> dict[str, Any]:
    """Season statistics for a player."""
    return _players_ep.stats(athlete_id, season=season, client=client)


def athlete_gamelog(athlete_id: str | int, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """Game-by-game log for a player."""
    return _players_ep.gamelog(athlete_id, client=client)


def athlete_news(athlete_id: str | int, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """News articles about a player."""
    return _players_ep.news(athlete_id, client=client)


# ── League-wide ───────────────────────────────────────────────────────────────

def standings(*, season: int | None = None, client: SportlyClient | None = None) -> Any:
    """NFL standings."""
    return _league_ep.standings(season=season, client=client)


def injuries(*, client: SportlyClient | None = None) -> list[dict[str, Any]]:
    """League-wide injury report."""
    return _league_ep.injuries(client=client)


def transactions(*, client: SportlyClient | None = None) -> list[dict[str, Any]]:
    """Recent transactions (signings, releases, trades)."""
    return _league_ep.transactions(client=client)


def news(*, limit: int = 25, client: SportlyClient | None = None) -> list[Any]:
    """NFL news feed."""
    return _league_ep.news(limit=limit, client=client)


def qbr(
    *,
    season: int | None = None,
    season_type: int = 2,
    week: int | None = None,
    client: SportlyClient | None = None,
) -> dict[str, Any]:
    """ESPN Quarterback Rating (QBR)."""
    return _league_ep.qbr(season=season, season_type=season_type, week=week, client=client)
