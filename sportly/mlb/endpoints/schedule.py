"""sportly.mlb.endpoints.schedule — Schedule endpoints."""
from __future__ import annotations
from typing import Any
from sportly.mlb._client import MLBClient, SPORT_ID, get_client


def today(
    *,
    hydrate: str | None = None,
    sport_id: int = SPORT_ID,
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return all games scheduled for today."""
    return games(sport_id=sport_id, hydrate=hydrate, client=client)


def games(
    *,
    date: str | None = None,
    start_date: str | None = None,
    end_date: str | None = None,
    team_id: int | None = None,
    sport_id: int = SPORT_ID,
    season: int | None = None,
    game_pk: int | None = None,
    hydrate: str | None = None,
    client: MLBClient | None = None,
) -> list[dict[str, Any]]:
    """Return games for a date, date range, or team.

    Parameters
    ----------
    date:       Single date ``YYYY-MM-DD``.
    start_date: Range start ``YYYY-MM-DD``.
    end_date:   Range end ``YYYY-MM-DD``.
    team_id:    Filter to one team.
    hydrate:    Embed sub-resources, e.g. ``"team,linescore,probablePitcher"``.

    Examples
    --------
    ::

        from sportly.mlb.endpoints import schedule

        # Today
        schedule.today()

        # April 1, 2025
        schedule.games(date="2025-04-01")

        # Dodgers full April
        schedule.games(team_id=119, start_date="2025-04-01", end_date="2025-04-30")

        # With probable pitchers
        schedule.games(date="2025-04-01", hydrate="team,linescore,probablePitcher")
    """
    http = client or get_client()
    data = http.get(
        "schedule",
        sportId=sport_id,
        date=date,
        startDate=start_date,
        endDate=end_date,
        teamId=team_id,
        season=season,
        gamePk=game_pk,
        hydrate=hydrate,
    )
    result: list[dict] = []
    for day in data.get("dates", []):
        result.extend(day.get("games", []))
    return result  # type: ignore[return-value]
