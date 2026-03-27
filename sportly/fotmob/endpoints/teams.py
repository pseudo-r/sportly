"""fotmob.endpoints.teams — team profiles and squad details."""
from __future__ import annotations
from typing import Any
from sportly.fotmob.endpoints._client import FotMobClient, get_client


def team(team_id: int | str, *, client: FotMobClient | None = None) -> dict[str, Any]:
    """Team profile: squad list, season stats, recent and upcoming fixtures.

    Parameters
    ----------
    team_id: Numeric FotMob team ID (e.g. ``8456`` = Manchester City).
    """
    return (client or get_client()).get("teams", id=team_id)  # type: ignore[return-value]
