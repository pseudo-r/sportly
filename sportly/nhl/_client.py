"""Native NHL Web API client.

Base URL: https://api-web.nhle.com/v1
"""

from __future__ import annotations

from typing import Any

from sportly.client import SportlyClient, get_client

_BASE = "https://api-web.nhle.com/v1"


class NHLClient:
    """Client for the official NHL Web API.

    Provides team, schedule, and game data directly from the NHL
    (more detailed than ESPN for hockey).

    Parameters
    ----------
    client:
        Optional :class:`~sportly.client.SportlyClient` override.
    """

    def __init__(self, client: SportlyClient | None = None) -> None:
        self._client = client

    @property
    def http(self) -> SportlyClient:
        return self._client or get_client()

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        return self.http.get(f"{_BASE}/{path.lstrip('/')}", params=params or None)

    # ── Teams ─────────────────────────────────────────────────────────────────

    def teams(self) -> list[dict[str, Any]]:
        """Return all NHL franchise records.

        Returns
        -------
        list[dict]
            Raw franchise dicts from ``/v1/franchise``.

        Example
        -------
        ::

            from sportly.nhl import teams
            all_teams = teams()
        """
        data = self._get("/franchise")
        return data.get("data", [])  # type: ignore[return-value]

    # ── Schedule ──────────────────────────────────────────────────────────────

    def schedule(self, date: str | None = None) -> dict[str, Any]:
        """Return the NHL schedule for a given date (or today).

        Parameters
        ----------
        date:
            Date in ``YYYY-MM-DD`` format.  Defaults to today (server time).

        Example
        -------
        ::

            from sportly.nhl import schedule
            today = schedule()
            specific = schedule("2024-04-15")
        """
        path = f"/schedule/{date}" if date else "/schedule/now"
        return self._get(path)

    # ── Game ──────────────────────────────────────────────────────────────────

    def game(self, game_id: str) -> dict[str, Any]:
        """Return boxscore for a game.

        Parameters
        ----------
        game_id:
            NHL game ID, e.g. ``"2024020001"``.
        """
        return self._get(f"/gamecenter/{game_id}/boxscore")

    def play_by_play(self, game_id: str) -> dict[str, Any]:
        """Return play-by-play data for a game.

        Parameters
        ----------
        game_id:
            NHL game ID.
        """
        return self._get(f"/gamecenter/{game_id}/play-by-play")
