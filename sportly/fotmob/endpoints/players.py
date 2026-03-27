"""fotmob.endpoints.players — player profiles and search."""
from __future__ import annotations

from typing import Any

from sportly.fotmob.endpoints._client import FotMobClient, get_client


def player(player_id: int | str, *, client: FotMobClient | None = None) -> dict[str, Any]:
    """Player profile: career stats, season stats, recent matches, heatmaps.

    Parameters
    ----------
    player_id: Numeric FotMob player ID (e.g. ``174543`` = Kevin De Bruyne).
    """
    return (client or get_client()).get("playerData", id=player_id)  # type: ignore[return-value]


def search(term: str, *, client: FotMobClient | None = None) -> dict[str, Any]:
    """Search players, teams, and tournaments.

    Returns ``{"squad": [...], "team": [...], "tournament": [...]}``.
    """
    return (client or get_client()).get("searchData", term=term)  # type: ignore[return-value]


def transfers(*, client: FotMobClient | None = None) -> dict[str, Any]:
    """Recent transfer news and confirmed moves."""
    return (client or get_client()).get("transfers")  # type: ignore[return-value]


def world_news(*, client: FotMobClient | None = None) -> dict[str, Any]:
    """Global football news feed."""
    return (client or get_client()).get("worldnews")  # type: ignore[return-value]
