"""nhl.endpoints.schedule — daily and date-range schedule."""
from __future__ import annotations
from typing import Any
from sportly.nhl._client import NHLClient


def schedule(date: str | None = None, *, client: NHLClient | None = None) -> dict[str, Any]:
    """NHL schedule for a date (``YYYY-MM-DD``) or today.

    Example::

        from sportly.nhl.endpoints import schedule as sched
        today    = sched.schedule()
        specific = sched.schedule("2024-04-15")
    """
    path = f"/schedule/{date}" if date else "/schedule/now"
    return (client or NHLClient())._get(path)


def weekly(date: str | None = None, *, client: NHLClient | None = None) -> dict[str, Any]:
    """Week-long schedule centred around a date.

    Returns ``gameWeek`` data used by the NHL scoreboard widget.
    """
    path = f"/schedule/{date}/week" if date else "/schedule/now/week"
    return (client or NHLClient())._get(path)
