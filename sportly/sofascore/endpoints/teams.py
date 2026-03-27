"""sofascore.endpoints.teams — team profiles and squad rosters."""
from __future__ import annotations
from typing import Any
from sportly.sofascore.endpoints._client import get


def team(team_id: int | str, *, client=None) -> dict[str, Any]:
    """Team profile (name, country, colours, manager)."""
    return get(f"team/{team_id}", client=client)  # type: ignore[return-value]


def squad(team_id: int | str, *, client=None) -> list[dict[str, Any]]:
    """Full squad roster for a team."""
    data = get(f"team/{team_id}/players", client=client)
    return data.get("players", [])  # type: ignore[return-value]
