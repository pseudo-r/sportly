"""sportly.nhl — Native NHL Web API client.

Base URL: https://api-web.nhle.com/v1
No auth required.

Features not available through ESPN: play-by-play with coordinates,
shift charts, game landing pages, roster history, standings by date.

Usage::

    from sportly import nhl

    # Franchises
    all_teams = nhl.teams()

    # Schedule
    today    = nhl.schedule()
    specific = nhl.schedule("2024-04-15")

    # Games
    box = nhl.game("2024020001")
    pbp = nhl.play_by_play("2024020001")

    # Teams
    roster   = nhl.roster("TOR")
    standings = nhl.standings()

    # Players
    mcdavid = nhl.player(8481528)

Endpoint subpackage::

    from sportly.nhl.endpoints import games, schedule, teams
"""
from __future__ import annotations
from typing import Any

from sportly.nhl._client import NHLClient
from sportly.nhl.endpoints import games as _games_ep
from sportly.nhl.endpoints import schedule as _sched_ep
from sportly.nhl.endpoints import teams as _teams_ep

__all__ = [
    "NHLClient",
    "teams", "schedule", "game", "play_by_play", "landing",
    "roster", "standings", "player",
]

_inst = NHLClient()

# ── Teams / Franchises ────────────────────────────────────────────────────────

def teams() -> list[dict[str, Any]]:
    """All NHL franchises."""
    return _teams_ep.franchises(client=_inst)


def roster(team_abbrev: str, season: str | None = None) -> dict[str, Any]:
    """Current (or historical) roster for a team (e.g. ``"TOR"``)."""
    return _teams_ep.roster(team_abbrev, season, client=_inst)


def standings(*, date: str | None = None) -> dict[str, Any]:
    """League standings — current or as of a specific ``YYYY-MM-DD`` date."""
    return _teams_ep.standings(date=date, client=_inst)


def player(player_id: int | str) -> dict[str, Any]:
    """Player profile and career stats by numeric NHL player ID."""
    return _teams_ep.player(player_id, client=_inst)


# ── Schedule ──────────────────────────────────────────────────────────────────

def schedule(date: str | None = None) -> dict[str, Any]:
    """NHL schedule for a date (``YYYY-MM-DD``) or today."""
    return _sched_ep.schedule(date, client=_inst)


def weekly(date: str | None = None) -> dict[str, Any]:
    """Week-long schedule centred around a date."""
    return _sched_ep.weekly(date, client=_inst)


# ── Games ─────────────────────────────────────────────────────────────────────

def game(game_id: str) -> dict[str, Any]:
    """Full boxscore for a game."""
    return _games_ep.boxscore(game_id, client=_inst)


def play_by_play(game_id: str) -> dict[str, Any]:
    """All plays with x/y coordinates, shot types, and player references."""
    return _games_ep.play_by_play(game_id, client=_inst)


def landing(game_id: str) -> dict[str, Any]:
    """Game landing page (live score, period summary, used by NHL.com)."""
    return _games_ep.landing(game_id, client=_inst)
