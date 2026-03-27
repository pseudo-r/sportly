"""sofascore.endpoints.schedule — scheduled events by sport and date."""
from __future__ import annotations
from typing import Any
from sportly.sofascore.endpoints._client import SPORTS, get


def matches(sport: str, date: str, *, page: int = 1, client=None) -> list[dict[str, Any]]:
    """Return scheduled events for a sport on a date (``YYYY-MM-DD``).

    Sport aliases: ``soccer`` → ``football``, ``hockey`` → ``ice-hockey``.

    Example::

        from sportly.sofascore.endpoints import schedule
        games = schedule.matches("football", "2026-03-26")
    """
    slug = SPORTS.get(sport, sport)
    if slug == "tennis":
        data = get(f"sport/tennis/scheduled-tournaments/{date}/page/{page}", client=client)
        return data.get("tournaments", [])  # type: ignore[return-value]
    data = get(f"sport/{slug}/scheduled-events/{date}", client=client)
    return data.get("events", [])  # type: ignore[return-value]
