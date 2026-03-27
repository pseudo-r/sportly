"""fantasy.endpoints.meta — game and season metadata."""
from __future__ import annotations
from typing import Any
from sportly.fantasy.endpoints._client import get_client


def game_meta(game_code: str, *, cookies: dict[str, str] | None = None) -> dict[str, Any]:
    """Game metadata: ``currentSeasonId``, ``name``, ``active``.

    No league ID required — works for any game code::

        from sportly.fantasy.endpoints import meta
        info = meta.game_meta("ffl")
        print(info["currentSeasonId"])   # 2026
    """
    return get_client(cookies).get(game_code)  # type: ignore[return-value]


def season_meta(game_code: str, season: int, *, cookies: dict[str, str] | None = None) -> dict[str, Any]:
    """Season-level metadata: start/end dates, current scoring period."""
    return get_client(cookies).get(f"{game_code}/seasons/{season}")  # type: ignore[return-value]
