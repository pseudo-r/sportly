"""fotmob.endpoints.matches — daily fixture list and full match detail."""
from __future__ import annotations

from typing import Any

from sportly.fotmob.endpoints._client import FotMobClient, get_client


def matches(date: str, *, client: FotMobClient | None = None) -> dict[str, Any]:
    """All matches for a date (``YYYYMMDD``).

    Returns ``{leagues: [{id, name, matches: [{id, home, away, status}]}]}``.
    """
    return (client or get_client()).get("matches", date=date)  # type: ignore[return-value]


def match(match_id: int | str, *, client: FotMobClient | None = None) -> dict[str, Any]:
    """Full match detail: lineups, incidents, stats, xG, player ratings.

    Parameters
    ----------
    match_id: FotMob match ID (``leagues[].matches[].id`` from :func:`matches`).
    """
    return (client or get_client()).get("matchDetails", matchId=match_id)  # type: ignore[return-value]
