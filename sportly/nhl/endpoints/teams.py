"""nhl.endpoints.teams — franchise list, roster, standings."""
from __future__ import annotations
from typing import Any
from sportly.nhl._client import NHLClient


def franchises(*, client: NHLClient | None = None) -> list[dict[str, Any]]:
    """All NHL franchise records.

    Example::

        from sportly.nhl.endpoints import teams
        all_teams = teams.franchises()
    """
    data = (client or NHLClient())._get("/franchise")
    return data.get("data", [])  # type: ignore[return-value]


def roster(team_abbrev: str, season: str | None = None, *, client: NHLClient | None = None) -> dict[str, Any]:
    """Current (or historical) roster for a team.

    Parameters
    ----------
    team_abbrev: Three-letter team code, e.g. ``"TOR"``, ``"MTL"``.
    season:      Optional season in ``YYYYYYYY`` format, e.g. ``"20242025"``.
                 Defaults to current season.

    Example::

        from sportly.nhl.endpoints import teams
        leafs = teams.roster("TOR")
    """
    path = f"/roster/{team_abbrev}/{season}" if season else f"/roster/{team_abbrev}/current"
    return (client or NHLClient())._get(path)


def standings(*, date: str | None = None, client: NHLClient | None = None) -> dict[str, Any]:
    """League standings (optionally for a specific date).

    Parameters
    ----------
    date: ``YYYY-MM-DD`` — standings as of that date; defaults to current.
    """
    path = f"/standings/{date}" if date else "/standings/now"
    return (client or NHLClient())._get(path)


def player(player_id: int | str, *, client: NHLClient | None = None) -> dict[str, Any]:
    """Player profile and career stats.

    Parameters
    ----------
    player_id: Numeric NHL player ID (e.g. ``8481528`` = Connor McDavid).
    """
    return (client or NHLClient())._get(f"/player/{player_id}/landing")
