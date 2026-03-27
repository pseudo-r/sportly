"""sofascore.endpoints.tournaments — competitions and popular leagues."""
from __future__ import annotations
from typing import Any
from sportly.sofascore.endpoints._client import SPORTS, get


def tournaments(sport: str, *, client=None) -> dict[str, Any]:
    """All available tournaments / unique leagues for a sport."""
    slug = SPORTS.get(sport, sport)
    return get(f"sport/{slug}/unique-tournaments", client=client)  # type: ignore[return-value]


def popular(locale: str = "US", *, client=None) -> dict[str, Any]:
    """Popular leagues and entities for a locale (e.g. ``"US"``, ``"GB"``)."""
    return get(f"config/popular-entities/{locale}", client=client)  # type: ignore[return-value]
