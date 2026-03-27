"""sportly.sofascore — Sofascore public API.

Base URL: https://api.sofascore.com/api/v1/
Multi-sport: football, basketball, tennis, ice-hockey, baseball, esports.

⚠️  WAF / TLS Fingerprinting:
Standard httpx returns 403. This module uses ``curl_cffi`` to impersonate
a Chrome browser at the TLS layer. Install with:

    pip install sportly[sofascore]     # adds curl_cffi
    # or directly:
    pip install curl_cffi>=0.6

Usage::

    from sportly import sofascore

    # Today's football matches
    games = sofascore.matches("football", "2026-03-26")

    # Match detail, stats, lineups, momentum graph
    event      = sofascore.match(11352523)
    stats      = sofascore.match_stats(11352523)
    lineups    = sofascore.lineups(11352523)
    momentum   = sofascore.momentum(11352523)

    # Player and team profiles
    p = sofascore.player(814123)
    t = sofascore.team(4705)

    # All tournaments for a sport
    tours = sofascore.tournaments("football")
"""
from __future__ import annotations
from typing import Any

BASE_URL = "https://api.sofascore.com/api/v1"

# ── Sport slugs ───────────────────────────────────────────────────────────────
SPORTS: dict[str, str] = {
    "football":         "football",
    "soccer":           "football",     # alias
    "basketball":       "basketball",
    "tennis":           "tennis",
    "ice-hockey":       "ice-hockey",
    "hockey":           "ice-hockey",   # alias
    "baseball":         "baseball",
    "american-football":"american-football",
    "esports":          "esports",
    "table-tennis":     "table-tennis",
}


def _get_client():
    """Return a curl_cffi Chrome-impersonated session."""
    try:
        from curl_cffi import requests as cffi_requests  # type: ignore[import]
        return cffi_requests.Session(impersonate="chrome")
    except ImportError as exc:  # pragma: no cover
        raise ImportError(
            "sportly.sofascore requires curl_cffi for TLS fingerprint bypass.\n"
            "Install with: pip install sportly[sofascore]  "
            "or: pip install curl_cffi>=0.6"
        ) from exc


def _get(path: str, *, client=None) -> Any:
    from sportly.exceptions import NotFoundError, RateLimitError, SportlyError
    c = client or _get_client()
    url = f"{BASE_URL}/{path.lstrip('/')}"
    resp = c.get(url, headers={"Accept": "application/json, text/plain, */*"})
    if resp.status_code == 404:
        raise NotFoundError(f"Not found: {url}", status_code=404, url=url)
    if resp.status_code == 429:
        raise RateLimitError("Sofascore rate limited", status_code=429)
    if resp.status_code == 403:
        raise SportlyError(
            "Sofascore returned 403. curl_cffi impersonation may need updating.",
            status_code=403,
        )
    resp.raise_for_status()
    return resp.json()


# ── Schedule ──────────────────────────────────────────────────────────────────

def matches(
    sport: str,
    date: str,
    *,
    page: int = 1,
    client=None,
) -> list[dict[str, Any]]:
    """Return all scheduled matches for a sport on a date.

    Parameters
    ----------
    sport: e.g. ``"football"``, ``"basketball"``, ``"tennis"``.
    date:  ``YYYY-MM-DD`` format.

    Example
    -------
    ::

        games = sofascore.matches("football", "2026-03-26")
        for g in games:
            print(g["homeTeam"]["name"], "vs", g["awayTeam"]["name"])
    """
    slug = SPORTS.get(sport, sport)
    if sport == "tennis":
        data = _get(f"sport/tennis/scheduled-tournaments/{date}/page/{page}", client=client)
        return data.get("tournaments", [])  # type: ignore[return-value]
    data = _get(f"sport/{slug}/scheduled-events/{date}", client=client)
    return data.get("events", [])  # type: ignore[return-value]


# ── Match / Event ─────────────────────────────────────────────────────────────

def match(event_id: int | str, *, client=None) -> dict[str, Any]:
    """Return core event details (teams, score, status, tournament)."""
    return _get(f"event/{event_id}", client=client)  # type: ignore[return-value]


def match_stats(event_id: int | str, *, client=None) -> dict[str, Any]:
    """Return match statistics (possession, shots, passes, xG)."""
    return _get(f"event/{event_id}/statistics", client=client)  # type: ignore[return-value]


def lineups(event_id: int | str, *, client=None) -> dict[str, Any]:
    """Return confirmed lineups for a match."""
    return _get(f"event/{event_id}/lineups", client=client)  # type: ignore[return-value]


def incidents(event_id: int | str, *, client=None) -> dict[str, Any]:
    """Return match incidents timeline (goals, cards, substitutions)."""
    return _get(f"event/{event_id}/incidents", client=client)  # type: ignore[return-value]


def momentum(event_id: int | str, *, client=None) -> dict[str, Any]:
    """Return momentum graph data (football) or tennis power curve."""
    return _get(f"event/{event_id}/graph", client=client)  # type: ignore[return-value]


def point_by_point(event_id: int | str, *, client=None) -> dict[str, Any]:
    """Return point-by-point data for tennis matches."""
    return _get(f"event/{event_id}/point-by-point", client=client)  # type: ignore[return-value]


# ── Players ───────────────────────────────────────────────────────────────────

def player(player_id: int | str, *, client=None) -> dict[str, Any]:
    """Return player profile."""
    return _get(f"player/{player_id}", client=client)  # type: ignore[return-value]


def player_seasons(player_id: int | str, *, client=None) -> dict[str, Any]:
    """Return career stats by season for a player."""
    return _get(f"player/{player_id}/statistics/seasons", client=client)  # type: ignore[return-value]


# ── Teams ─────────────────────────────────────────────────────────────────────

def team(team_id: int | str, *, client=None) -> dict[str, Any]:
    """Return team profile."""
    return _get(f"team/{team_id}", client=client)  # type: ignore[return-value]


def squad(team_id: int | str, *, client=None) -> list[dict[str, Any]]:
    """Return team roster / squad."""
    data = _get(f"team/{team_id}/players", client=client)
    return data.get("players", [])  # type: ignore[return-value]


# ── Tournaments ───────────────────────────────────────────────────────────────

def tournaments(sport: str, *, client=None) -> dict[str, Any]:
    """Return all available tournaments for a sport."""
    slug = SPORTS.get(sport, sport)
    return _get(f"sport/{slug}/unique-tournaments", client=client)  # type: ignore[return-value]


def popular(locale: str = "US", *, client=None) -> dict[str, Any]:
    """Return popular leagues and entities for a locale."""
    return _get(f"config/popular-entities/{locale}", client=client)  # type: ignore[return-value]
