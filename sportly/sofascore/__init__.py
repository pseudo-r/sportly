"""sportly.sofascore — Sofascore public API.

Base URL: https://api.sofascore.com/api/v1/
Multi-sport: football, basketball, tennis, ice-hockey, baseball, esports.

⚠️  Requires ``curl_cffi`` for TLS fingerprint bypass:

    pip install sportly[sofascore]

Usage::

    from sportly import sofascore

    games     = sofascore.matches("football", "2026-03-26")
    event     = sofascore.match(11352523)
    stats     = sofascore.match_stats(11352523)
    lineups   = sofascore.lineups(11352523)
    momentum  = sofascore.momentum(11352523)
    p         = sofascore.player(814123)
    t         = sofascore.team(4705)
    tours     = sofascore.tournaments("football")

Endpoint subpackage::

    from sportly.sofascore.endpoints import schedule, events, players, teams, tournaments
"""
from __future__ import annotations

from typing import Any

from sportly.sofascore.endpoints._client import SPORTS, get_curl_session

__all__ = [
    "SPORTS",
    "matches", "match", "match_stats", "lineups", "incidents", "momentum", "point_by_point",
    "player", "player_seasons",
    "team", "squad",
    "tournaments", "popular",
    "_get", "_get_client",
]


def _get_client():
    """Return a curl_cffi Chrome-impersonated session (exposed for testing)."""
    return get_curl_session()


def _get(path: str, *, client=None) -> Any:
    """Internal HTTP helper — exposed as module attribute so tests can monkeypatch it."""
    from sportly.sofascore.endpoints._client import get as _raw_get
    return _raw_get(path, client=client)


# ── Schedule ──────────────────────────────────────────────────────────────────

def matches(sport: str, date: str, *, page: int = 1, client=None) -> list[dict[str, Any]]:
    """Scheduled events for a sport on ``YYYY-MM-DD``.

    Sport aliases: ``soccer`` → ``football``, ``hockey`` → ``ice-hockey``.
    """
    slug = SPORTS.get(sport, sport)
    if slug == "tennis":
        data = _get(f"sport/tennis/scheduled-tournaments/{date}/page/{page}", client=client)
        return data.get("tournaments", [])  # type: ignore[return-value]
    data = _get(f"sport/{slug}/scheduled-events/{date}", client=client)
    return data.get("events", [])  # type: ignore[return-value]


# ── Events ────────────────────────────────────────────────────────────────────

def match(event_id: int | str, *, client=None) -> dict[str, Any]:
    """Core event details (teams, score, status, tournament)."""
    return _get(f"event/{event_id}", client=client)  # type: ignore[return-value]


def match_stats(event_id: int | str, *, client=None) -> dict[str, Any]:
    """Match statistics (possession, shots, passes, xG)."""
    return _get(f"event/{event_id}/statistics", client=client)  # type: ignore[return-value]


def lineups(event_id: int | str, *, client=None) -> dict[str, Any]:
    """Confirmed lineups and formations."""
    return _get(f"event/{event_id}/lineups", client=client)  # type: ignore[return-value]


def incidents(event_id: int | str, *, client=None) -> dict[str, Any]:
    """Goals, cards, and substitution timeline."""
    return _get(f"event/{event_id}/incidents", client=client)  # type: ignore[return-value]


def momentum(event_id: int | str, *, client=None) -> dict[str, Any]:
    """Momentum graph (football) or power curve (tennis)."""
    return _get(f"event/{event_id}/graph", client=client)  # type: ignore[return-value]


def point_by_point(event_id: int | str, *, client=None) -> dict[str, Any]:
    """Point-by-point data (tennis only)."""
    return _get(f"event/{event_id}/point-by-point", client=client)  # type: ignore[return-value]


# ── Players ───────────────────────────────────────────────────────────────────

def player(player_id: int | str, *, client=None) -> dict[str, Any]:
    """Player profile."""
    return _get(f"player/{player_id}", client=client)  # type: ignore[return-value]


def player_seasons(player_id: int | str, *, client=None) -> dict[str, Any]:
    """Career statistics by season."""
    return _get(f"player/{player_id}/statistics/seasons", client=client)  # type: ignore[return-value]


# ── Teams ─────────────────────────────────────────────────────────────────────

def team(team_id: int | str, *, client=None) -> dict[str, Any]:
    """Team profile."""
    return _get(f"team/{team_id}", client=client)  # type: ignore[return-value]


def squad(team_id: int | str, *, client=None) -> list[dict[str, Any]]:
    """Team roster / squad."""
    data = _get(f"team/{team_id}/players", client=client)
    return data.get("players", [])  # type: ignore[return-value]


# ── Tournaments ───────────────────────────────────────────────────────────────

def tournaments(sport: str, *, client=None) -> dict[str, Any]:
    """All tournaments for a sport."""
    slug = SPORTS.get(sport, sport)
    return _get(f"sport/{slug}/unique-tournaments", client=client)  # type: ignore[return-value]


def popular(locale: str = "US", *, client=None) -> dict[str, Any]:
    """Popular leagues and entities for a locale."""
    return _get(f"config/popular-entities/{locale}", client=client)  # type: ignore[return-value]
