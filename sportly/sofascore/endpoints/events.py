"""sofascore.endpoints.events — match/event detail, stats, lineups, incidents."""
from __future__ import annotations
from typing import Any
from sportly.sofascore.endpoints._client import get


def match(event_id: int | str, *, client=None) -> dict[str, Any]:
    """Core event details: teams, score, status, tournament."""
    return get(f"event/{event_id}", client=client)  # type: ignore[return-value]


def stats(event_id: int | str, *, client=None) -> dict[str, Any]:
    """Match statistics: possession, shots, passes, xG."""
    return get(f"event/{event_id}/statistics", client=client)  # type: ignore[return-value]


def lineups(event_id: int | str, *, client=None) -> dict[str, Any]:
    """Confirmed lineups and formations."""
    return get(f"event/{event_id}/lineups", client=client)  # type: ignore[return-value]


def incidents(event_id: int | str, *, client=None) -> dict[str, Any]:
    """Goals, cards, and substitution timeline."""
    return get(f"event/{event_id}/incidents", client=client)  # type: ignore[return-value]


def momentum(event_id: int | str, *, client=None) -> dict[str, Any]:
    """Momentum graph (football) or power curve (tennis)."""
    return get(f"event/{event_id}/graph", client=client)  # type: ignore[return-value]


def point_by_point(event_id: int | str, *, client=None) -> dict[str, Any]:
    """Point-by-point data (tennis only)."""
    return get(f"event/{event_id}/point-by-point", client=client)  # type: ignore[return-value]
