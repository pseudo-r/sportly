"""fantasy.endpoints.players — player pool and projections."""
from __future__ import annotations

import json
from typing import Any

from sportly.fantasy.endpoints._client import get_client


def players(
    game_code: str,
    *,
    season: int,
    active_only: bool = True,
    cookies: dict[str, str] | None = None,
) -> list[dict[str, Any]]:
    """Full player pool for a sport/season.

    Parameters
    ----------
    active_only: Filter to only active/rostered players (default ``True``).
    """
    http = get_client(cookies)
    fantasy_filter = json.dumps({"filterActive": {"value": active_only}})
    path = f"{game_code}/seasons/{season}/players"
    data = http.get(path, headers={"X-Fantasy-Filter": fantasy_filter}, view="players_wl")
    return data if isinstance(data, list) else []  # type: ignore[return-value]
