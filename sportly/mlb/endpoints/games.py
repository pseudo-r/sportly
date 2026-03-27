"""sportly.mlb.endpoints.games — Live game data endpoints."""
from __future__ import annotations

from typing import Any

from sportly.mlb._client import MLBClient, get_client


def boxscore(game_pk: int | str, *, client: MLBClient | None = None) -> dict[str, Any]:
    """Return full boxscore for a game.

    Key fields: ``teams``, ``officials``, ``info``, ``pitchingNotes``.
    """
    return (client or get_client()).get(f"game/{game_pk}/boxscore")  # type: ignore[return-value]


def linescore(game_pk: int | str, *, client: MLBClient | None = None) -> dict[str, Any]:
    """Return linescore (inning-by-inning) for a game.

    Key fields: ``innings``, ``teams``, ``balls``, ``strikes``, ``outs``,
    ``currentInning``, ``offense``, ``defense``.
    """
    return (client or get_client()).get(f"game/{game_pk}/linescore")  # type: ignore[return-value]


def play_by_play(game_pk: int | str, *, client: MLBClient | None = None) -> dict[str, Any]:
    """Return full play-by-play log for a game.

    Key field: ``allPlays[]`` — each entry has ``result``, ``about``,
    ``matchup``, ``pitchIndex``, ``actionIndex``, ``playEvents``.
    """
    return (client or get_client()).get(f"game/{game_pk}/playByPlay")  # type: ignore[return-value]


def live_feed(game_pk: int | str, *, client: MLBClient | None = None) -> dict[str, Any]:
    """Return the full live game feed (play-by-play + boxscore + linescore).

    .. note::
        May return 404 for older completed games. Use ``boxscore()`` +
        ``linescore()`` for historical data instead.
    """
    return (client or get_client()).get(f"game/{game_pk}/feed/live")  # type: ignore[return-value]


def win_probability(game_pk: int | str, *, client: MLBClient | None = None) -> list[dict[str, Any]]:
    """Return win probability by play (live or completed)."""
    data = (client or get_client()).get(f"game/{game_pk}/winProbability")
    return data if isinstance(data, list) else data.get("winProbability", [])  # type: ignore[return-value]


def decisions(game_pk: int | str, *, client: MLBClient | None = None) -> dict[str, Any]:
    """Return W/L/Save pitcher decisions for a completed game."""
    return (client or get_client()).get(f"game/{game_pk}/decisions")  # type: ignore[return-value]


def content(game_pk: int | str, *, client: MLBClient | None = None) -> dict[str, Any]:
    """Return game media content — highlights, editorial, recap."""
    return (client or get_client()).get(f"game/{game_pk}/content")  # type: ignore[return-value]
