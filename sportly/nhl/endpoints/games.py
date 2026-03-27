"""nhl.endpoints.games — boxscore, play-by-play, and shifts."""
from __future__ import annotations

from typing import Any

from sportly.nhl._client import NHLClient


def boxscore(game_id: str, *, client: NHLClient | None = None) -> dict[str, Any]:
    """Full boxscore for a game.

    Parameters
    ----------
    game_id: NHL game ID, e.g. ``"2024020001"``.

    Example::

        from sportly.nhl.endpoints import games
        box = games.boxscore("2024020001")
    """
    return (client or NHLClient())._get(f"/gamecenter/{game_id}/boxscore")


def play_by_play(game_id: str, *, client: NHLClient | None = None) -> dict[str, Any]:
    """All plays with x/y coordinates, shot types, and player references.

    Example::

        pbp = games.play_by_play("2024020001")
        for play in pbp["plays"]:
            print(play["typeDescKey"], play["timeInPeriod"])
    """
    return (client or NHLClient())._get(f"/gamecenter/{game_id}/play-by-play")


def landing(game_id: str, *, client: NHLClient | None = None) -> dict[str, Any]:
    """Game landing page data (used by NHL.com — includes live score, period summary)."""
    return (client or NHLClient())._get(f"/gamecenter/{game_id}/landing")
