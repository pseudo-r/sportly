"""sofascore.endpoints.players — player profiles and career stats."""
from __future__ import annotations

from typing import Any

from sportly.sofascore.endpoints._client import get


def player(player_id: int | str, *, client=None) -> dict[str, Any]:
    """Player profile (name, position, nationality, current team)."""
    return get(f"player/{player_id}", client=client)  # type: ignore[return-value]


def seasons(player_id: int | str, *, client=None) -> dict[str, Any]:
    """Career statistics broken down by season."""
    return get(f"player/{player_id}/statistics/seasons", client=client)  # type: ignore[return-value]
