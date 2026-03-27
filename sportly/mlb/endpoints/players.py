"""sportly.mlb.endpoints.players — People / player endpoints."""
from __future__ import annotations
from typing import Any
from sportly.mlb._client import MLBClient, get_client


def player(
    person_id: int | str,
    *,
    hydrate: str | None = None,
    client: MLBClient | None = None,
) -> dict[str, Any]:
    """Return a player profile.

    Parameters
    ----------
    person_id: MLB player ID (e.g. ``660271`` = Shohei Ohtani).
    hydrate:   Embed sub-resources, e.g. ``"stats(group=[hitting],type=[season])"``.
    """
    http = client or get_client()
    data = http.get(f"people/{person_id}", hydrate=hydrate)
    people = data.get("people", [{}])
    return people[0] if people else {}  # type: ignore[return-value]


def player_stats(
    person_id: int | str,
    *,
    stats: str = "season",
    group: str = "hitting",
    season: int | None = None,
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return player stats.

    Parameters
    ----------
    stats: ``"season"``, ``"career"``, ``"yearByYear"``, ``"gameLog"``.
    group: ``"hitting"``, ``"pitching"``, ``"fielding"``.

    Examples
    --------
    ::

        # Ohtani 2024 hitting
        players.player_stats(660271, stats="season", group="hitting", season=2024)

        # Year-by-year pitching
        players.player_stats(660271, stats="yearByYear", group="pitching")
    """
    http = client or get_client()
    data = http.get(f"people/{person_id}/stats", stats=stats, group=group, season=season)
    return data.get("stats", [])  # type: ignore[return-value]


def player_gamelog(
    person_id: int | str,
    *,
    season: int | None = None,
    group: str = "hitting",
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return game-by-game log for a player."""
    return player_stats(person_id, stats="gameLog", group=group, season=season, client=client)


def search(
    name: str,
    *,
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Search players by name."""
    http = client or get_client()
    data = http.get("people/search", names=name)
    return data.get("people", [])  # type: ignore[return-value]
