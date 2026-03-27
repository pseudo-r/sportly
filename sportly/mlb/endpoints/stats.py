"""sportly.mlb.endpoints.stats — League stats, leaders, standings."""
from __future__ import annotations
from typing import Any
from sportly.mlb._client import MLBClient, SPORT_ID, LEAGUE_AL, LEAGUE_NL, get_client


def standings(
    *,
    league_ids: str = f"{LEAGUE_AL},{LEAGUE_NL}",
    season: int | None = None,
    standings_type: str = "regularSeason",
    date: str | None = None,
    hydrate: str | None = None,
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return division standings.

    Parameters
    ----------
    league_ids:     ``"103,104"`` (AL+NL, default).
    season:         Season year. Omit for current.
    standings_type: ``"regularSeason"`` (default), ``"springTraining"``,
                    ``"firstHalf"``, ``"secondHalf"``, ``"playoffs"``.
    date:           Standings as-of date ``YYYY-MM-DD``.
    hydrate:        Embed sub-resources, e.g. ``"team,league,division"``.

    Example
    -------
    ::

        from sportly.mlb.endpoints import stats
        records = stats.standings(season=2025)
    """
    http = client or get_client()
    data = http.get(
        "standings",
        leagueId=league_ids,
        season=season,
        standingsTypes=standings_type,
        date=date,
        hydrate=hydrate,
    )
    return data.get("records", [])  # type: ignore[return-value]


def leaders(
    category: str,
    *,
    season: int | None = None,
    sport_id: int = SPORT_ID,
    limit: int = 10,
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return statistical leaders for a category.

    Parameters
    ----------
    category: e.g. ``"homeRuns"``, ``"battingAverage"``, ``"era"``,
              ``"wins"``, ``"strikeOuts"``, ``"rbi"``, ``"stolenBases"``.

    Example
    -------
    ::

        leaders = stats.leaders("homeRuns", season=2025)
    """
    http = client or get_client()
    data = http.get(
        "stats/leaders",
        leaderCategories=category,
        season=season,
        sportId=sport_id,
        limit=limit,
    )
    return data.get("leagueLeaders", [])  # type: ignore[return-value]


def transactions(
    *,
    start_date: str,
    end_date: str,
    team_id: int | None = None,
    player_id: int | None = None,
    sport_id: int = SPORT_ID,
    limit: int = 100,
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return player transactions in a date range.

    Parameters
    ----------
    start_date: ``YYYY-MM-DD`` (required).
    end_date:   ``YYYY-MM-DD`` (required).

    Example
    -------
    ::

        moves = stats.transactions(start_date="2025-03-01", end_date="2025-03-10")
    """
    http = client or get_client()
    data = http.get(
        "transactions",
        startDate=start_date,
        endDate=end_date,
        teamId=team_id,
        playerId=player_id,
        sportId=sport_id,
        limit=limit,
    )
    return data.get("transactions", [])  # type: ignore[return-value]


def venues(
    *,
    sport_id: int = SPORT_ID,
    season: int | None = None,
    venue_id: int | None = None,
    hydrate: str | None = None,
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return stadium info (name, location, field dimensions).

    Parameters
    ----------
    hydrate: ``"location,fieldInfo"`` for GPS coords + dimensions.

    Example
    -------
    ::

        # Dodger Stadium (venueId=22) with field dimensions
        from sportly.mlb.endpoints import stats
        [stadium] = stats.venues(venue_id=22, hydrate="location,fieldInfo")
    """
    http = client or get_client()
    path = f"venues/{venue_id}" if venue_id else "venues"
    data = http.get(path, sportId=sport_id, season=season, hydrate=hydrate)
    return data.get("venues", [])  # type: ignore[return-value]


def draft(year: int, *, client: MLBClient | None = None) -> dict[str, Any]:
    """Return full draft results for a year.

    Key fields: ``drafts.rounds[].picks[]`` — each pick has ``team``,
    ``person``, ``school``, ``position``, ``signingBonus``.
    """
    return (client or get_client()).get(f"draft/{year}")  # type: ignore[return-value]
