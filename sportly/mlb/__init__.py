"""sportly.mlb — MLB Stats API.

Usage::

    from sportly import mlb

    # Today's games
    games = mlb.schedule()

    # All teams
    teams = mlb.teams()

    # Shohei Ohtani profile
    ohtani = mlb.player(660271)

    # Home run leaders, 2025
    leaders = mlb.leaders("homeRuns", season=2025)

    # Dodgers roster
    roster = mlb.roster(119)

    # Game boxscore
    box = mlb.boxscore(745444)

    # AL + NL standings
    records = mlb.standings(season=2025)

    # Browse team abbreviations → IDs
    print(mlb.TEAM_IDS)    # {"LAD": 119, "NYY": 147, ...}
"""
from __future__ import annotations
from typing import Any
from sportly.mlb._client import LEAGUE_AL, LEAGUE_NL, SPORT_ID, TEAM_IDS, MLBClient, get_client
from sportly.mlb.endpoints import games as _games_ep
from sportly.mlb.endpoints import players as _players_ep
from sportly.mlb.endpoints import schedule as _schedule_ep
from sportly.mlb.endpoints import stats as _stats_ep
from sportly.mlb.endpoints import teams as _teams_ep

__all__ = [
    "TEAM_IDS", "SPORT_ID", "LEAGUE_AL", "LEAGUE_NL",
    "teams", "team", "roster", "team_stats",
    "schedule", "game_schedule",
    "player", "player_stats", "player_gamelog", "search",
    "boxscore", "linescore", "play_by_play", "live_feed",
    "win_probability", "decisions", "game_content",
    "standings", "leaders", "transactions", "venues", "draft",
]

# ── Teams ─────────────────────────────────────────────────────────────────────

def teams(
    *,
    season: int | None = None,
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return all active MLB teams."""
    return _teams_ep.all(season=season, client=client)


def team(
    team_id: int | str,
    *,
    season: int | None = None,
    client: MLBClient | None = None,
) -> dict[str, Any]:
    """Return a single team by ID (e.g. ``119`` = Dodgers)."""
    return _teams_ep.one(team_id, season=season, client=client)


def roster(
    team_id: int | str,
    *,
    roster_type: str = "active",
    season: int | None = None,
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return the roster for a team. ``roster_type``: ``"active"`` (default), ``"40Man"``."""
    return _teams_ep.roster(team_id, roster_type=roster_type, season=season, client=client)


def team_stats(
    team_id: int | str,
    *,
    stats: str = "season",
    group: str = "hitting",
    season: int | None = None,
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return team stats. ``group``: ``"hitting"``, ``"pitching"``, ``"fielding"``."""
    return _teams_ep.stats(team_id, stats=stats, group=group, season=season, client=client)


# ── Schedule ──────────────────────────────────────────────────────────────────

def schedule(
    *,
    date: str | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
    team_id: int | None = None,
    season: int | None = None,
    hydrate: str | None = None,
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return scheduled games.

    Called with no arguments returns today's games.

    Parameters
    ----------
    date:       Single date ``YYYY-MM-DD``.
    start_date: Range start.
    end_date:   Range end.
    team_id:    Filter to one team.
    hydrate:    e.g. ``"team,linescore,probablePitcher"``.
    """
    return _schedule_ep.games(
        date=date, start_date=start_date, end_date=end_date,
        team_id=team_id, season=season, hydrate=hydrate, client=client,
    )


def game_schedule(
    team_id: int | str,
    *,
    start_date: str,
    end_date: str,
    hydrate: str | None = None,
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return a team's schedule for a date range."""
    return _schedule_ep.games(
        team_id=int(team_id), start_date=start_date, end_date=end_date,
        hydrate=hydrate, client=client,
    )


# ── Players ───────────────────────────────────────────────────────────────────

def player(
    person_id: int | str,
    *,
    hydrate: str | None = None,
    client: MLBClient | None = None,
) -> dict[str, Any]:
    """Return a player profile by MLB ``personId``."""
    return _players_ep.player(person_id, hydrate=hydrate, client=client)


def player_stats(
    person_id: int | str,
    *,
    stats: str = "season",
    group: str = "hitting",
    season: int | None = None,
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return player stats. ``stats``: ``"season"``, ``"career"``, ``"yearByYear"``."""
    return _players_ep.player_stats(person_id, stats=stats, group=group, season=season, client=client)


def player_gamelog(
    person_id: int | str,
    *,
    season: int | None = None,
    group: str = "hitting",
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return game-by-game log for a player."""
    return _players_ep.player_gamelog(person_id, season=season, group=group, client=client)


def search(name: str, *, client: MLBClient | None = None) -> list[dict[str, Any]]:
    """Search players by name."""
    return _players_ep.search(name, client=client)


# ── Games ─────────────────────────────────────────────────────────────────────

def boxscore(game_pk: int | str, *, client: MLBClient | None = None) -> dict[str, Any]:
    """Return full boxscore for a game."""
    return _games_ep.boxscore(game_pk, client=client)


def linescore(game_pk: int | str, *, client: MLBClient | None = None) -> dict[str, Any]:
    """Return inning-by-inning linescore."""
    return _games_ep.linescore(game_pk, client=client)


def play_by_play(game_pk: int | str, *, client: MLBClient | None = None) -> dict[str, Any]:
    """Return full play-by-play log."""
    return _games_ep.play_by_play(game_pk, client=client)


def live_feed(game_pk: int | str, *, client: MLBClient | None = None) -> dict[str, Any]:
    """Return full live game feed (PBP + boxscore + linescore combined)."""
    return _games_ep.live_feed(game_pk, client=client)


def win_probability(game_pk: int | str, *, client: MLBClient | None = None) -> list[dict[str, Any]]:
    """Return win probability by play."""
    return _games_ep.win_probability(game_pk, client=client)


def decisions(game_pk: int | str, *, client: MLBClient | None = None) -> dict[str, Any]:
    """Return W/L/Save pitcher decisions."""
    return _games_ep.decisions(game_pk, client=client)


def game_content(game_pk: int | str, *, client: MLBClient | None = None) -> dict[str, Any]:
    """Return game highlights and editorial content."""
    return _games_ep.content(game_pk, client=client)


# ── Stats / League ────────────────────────────────────────────────────────────

def standings(
    *,
    league_ids: str = f"{LEAGUE_AL},{LEAGUE_NL}",
    season: int | None = None,
    standings_type: str = "regularSeason",
    date: str | None = None,
    hydrate: str | None = None,
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return division standings. Default: AL + NL current regular season."""
    return _stats_ep.standings(
        league_ids=league_ids, season=season, standings_type=standings_type,
        date=date, hydrate=hydrate, client=client,
    )


def leaders(
    category: str,
    *,
    season: int | None = None,
    limit: int = 10,
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return statistical leaders.

    Parameters
    ----------
    category: ``"homeRuns"``, ``"battingAverage"``, ``"era"``,
              ``"wins"``, ``"strikeOuts"``, ``"rbi"``, ``"stolenBases"``.
    """
    return _stats_ep.leaders(category, season=season, limit=limit, client=client)


def transactions(
    *,
    start_date: str,
    end_date: str,
    team_id: int | None = None,
    player_id: int | None = None,
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return player transactions (trades, IL moves, signings) for a date range."""
    return _stats_ep.transactions(
        start_date=start_date, end_date=end_date,
        team_id=team_id, player_id=player_id, client=client,
    )


def venues(
    *,
    venue_id: int | None = None,
    season: int | None = None,
    hydrate: str | None = None,
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return stadium info. Use ``hydrate="location,fieldInfo"`` for dimensions."""
    return _stats_ep.venues(venue_id=venue_id, season=season, hydrate=hydrate, client=client)


def draft(year: int, *, client: MLBClient | None = None) -> dict[str, Any]:
    """Return full MLB draft results for a year."""
    return _stats_ep.draft(year, client=client)
