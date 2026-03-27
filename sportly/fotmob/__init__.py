"""sportly.fotmob — FotMob public API.

Base URL: https://www.fotmob.com/api/
No auth required · No versioning · Unique: xG, xA, momentum, player ratings, shot maps.

Usage::

    from sportly import fotmob

    day    = fotmob.matches("20260326")   # today's matches
    m      = fotmob.match(4310531)        # xG, lineups, incidents, ratings
    epl    = fotmob.league(47)            # Premier League table
    city   = fotmob.team(8456)            # Man City squad
    player = fotmob.player(174543)        # De Bruyne
    results = fotmob.search("messi")

    print(fotmob.LEAGUES)   # popular league IDs

Endpoint subpackage::

    from sportly.fotmob.endpoints import matches, leagues, teams, players
"""
from __future__ import annotations

from typing import Any

from sportly.fotmob.endpoints import leagues as _leagues_ep
from sportly.fotmob.endpoints import matches as _matches_ep
from sportly.fotmob.endpoints import players as _players_ep
from sportly.fotmob.endpoints import teams as _teams_ep
from sportly.fotmob.endpoints._client import LEAGUES, FotMobClient

__all__ = [
    "FotMobClient", "LEAGUES",
    "matches", "match",
    "league", "all_leagues", "tv_listings",
    "team",
    "player", "search", "transfers", "world_news",
]


# ── Matches ───────────────────────────────────────────────────────────────────

def matches(date: str, *, client: FotMobClient | None = None) -> dict[str, Any]:
    """All matches for a date (``YYYYMMDD``) → ``{leagues: [{matches: [...]}]}``."""
    return _matches_ep.matches(date, client=client)


def match(match_id: int | str, *, client: FotMobClient | None = None) -> dict[str, Any]:
    """Full match detail: lineups, incidents, stats, xG, player ratings."""
    return _matches_ep.match(match_id, client=client)


# ── Leagues ───────────────────────────────────────────────────────────────────

def league(league_id: int | str, *, client: FotMobClient | None = None) -> dict[str, Any]:
    """League: standings table, recent results, upcoming fixtures."""
    return _leagues_ep.league(league_id, client=client)


def all_leagues(*, client: FotMobClient | None = None) -> dict[str, Any]:
    """Full directory of every competition tracked by FotMob."""
    return _leagues_ep.all_leagues(client=client)


def tv_listings(*, date: str | None = None, client: FotMobClient | None = None) -> dict[str, Any]:
    """TV broadcast schedule."""
    return _leagues_ep.tv_listings(date=date, client=client)


# ── Teams ─────────────────────────────────────────────────────────────────────

def team(team_id: int | str, *, client: FotMobClient | None = None) -> dict[str, Any]:
    """Team profile, squad list, season stats, recent and upcoming fixtures."""
    return _teams_ep.team(team_id, client=client)


# ── Players / News ────────────────────────────────────────────────────────────

def player(player_id: int | str, *, client: FotMobClient | None = None) -> dict[str, Any]:
    """Player profile, career stats, season stats, recent matches, heatmaps."""
    return _players_ep.player(player_id, client=client)


def search(term: str, *, client: FotMobClient | None = None) -> dict[str, Any]:
    """Search players, teams, and tournaments → ``{squad, team, tournament}``."""
    return _players_ep.search(term, client=client)


def transfers(*, client: FotMobClient | None = None) -> dict[str, Any]:
    """Recent transfer news and confirmed moves."""
    return _players_ep.transfers(client=client)


def world_news(*, client: FotMobClient | None = None) -> dict[str, Any]:
    """Global football news feed."""
    return _players_ep.world_news(client=client)
