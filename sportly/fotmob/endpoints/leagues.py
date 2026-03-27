"""fotmob.endpoints.leagues — league tables, all leagues directory."""
from __future__ import annotations
from typing import Any
from sportly.fotmob.endpoints._client import FotMobClient, get_client


def league(league_id: int | str, *, client: FotMobClient | None = None) -> dict[str, Any]:
    """League data: standings table, recent results, upcoming fixtures.

    Parameters
    ----------
    league_id: Numeric FotMob league ID — see :data:`sportly.fotmob.LEAGUES`.

    Example::

        from sportly.fotmob.endpoints import leagues
        epl = leagues.league(47)
        table = epl["table"][0]["data"]["table"]["all"]
    """
    return (client or get_client()).get("leagues", id=league_id)  # type: ignore[return-value]


def all_leagues(*, client: FotMobClient | None = None) -> dict[str, Any]:
    """Full directory of every competition tracked by FotMob."""
    return (client or get_client()).get("allLeagues")  # type: ignore[return-value]


def tv_listings(*, date: str | None = None, client: FotMobClient | None = None) -> dict[str, Any]:
    """TV broadcast schedule.

    Parameters
    ----------
    date: ``YYYYMMDD`` (optional, defaults to today on remote).
    """
    return (client or get_client()).get("tvlistings", date=date)  # type: ignore[return-value]
