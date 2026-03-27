"""fantasy.endpoints.league — league-level data (teams, rosters, standings, draft)."""
from __future__ import annotations
from typing import Any
from sportly.fantasy.endpoints._client import FantasyClient, get_client


def fetch(
    game_code: str,
    *,
    league_id: int,
    season: int,
    views: list[str] | None = None,
    scoring_period_id: int | None = None,
    matchup_period_id: int | None = None,
    cookies: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Raw league fetch with arbitrary view(s).

    Parameters
    ----------
    game_code:         ``"ffl"``, ``"fba"``, ``"flb"``, ``"fhl"``
    league_id:         ESPN Fantasy league ID
    season:            Season year
    views:             One or more view names (see :data:`sportly.fantasy.VIEWS`)
    scoring_period_id: Filter by week / day
    cookies:           ``{"espn_s2": "...", "SWID": "{...}"}`` for private leagues
    """
    http = get_client(cookies)
    path = f"{game_code}/seasons/{season}/segments/0/leagues/{league_id}"
    params: dict[str, Any] = {}
    if views:
        params["view"] = views
    if scoring_period_id is not None:
        params["scoringPeriodId"] = scoring_period_id
    if matchup_period_id is not None:
        params["matchupPeriodId"] = matchup_period_id
    return http.get(path, **params)  # type: ignore[return-value]


def teams(game_code: str, *, league_id: int, season: int, cookies: dict[str, str] | None = None) -> list[dict[str, Any]]:
    """All fantasy teams — names, owners, records."""
    return fetch(game_code, league_id=league_id, season=season, views=["mTeam"], cookies=cookies).get("teams", [])  # type: ignore[return-value]


def roster(game_code: str, *, league_id: int, season: int, scoring_period_id: int | None = None, cookies: dict[str, str] | None = None) -> list[dict[str, Any]]:
    """All team rosters with player entries and lineup slot assignments."""
    return fetch(game_code, league_id=league_id, season=season, views=["mRoster"], scoring_period_id=scoring_period_id, cookies=cookies).get("teams", [])  # type: ignore[return-value]


def standings(game_code: str, *, league_id: int, season: int, cookies: dict[str, str] | None = None) -> list[dict[str, Any]]:
    """Teams with W/L/PF/PA standings."""
    return fetch(game_code, league_id=league_id, season=season, views=["mTeam", "mStandings"], cookies=cookies).get("teams", [])  # type: ignore[return-value]


def draft(game_code: str, *, league_id: int, season: int, cookies: dict[str, str] | None = None) -> dict[str, Any]:
    """Full draft history — picks, player IDs, round order."""
    return fetch(game_code, league_id=league_id, season=season, views=["mDraftDetail"], cookies=cookies).get("draftDetail", {})  # type: ignore[return-value]


def live_scoring(game_code: str, *, league_id: int, season: int, scoring_period_id: int, cookies: dict[str, str] | None = None) -> list[dict[str, Any]]:
    """Live scoring for an active scoring period."""
    return fetch(game_code, league_id=league_id, season=season, views=["mBoxscore", "mLiveScoring", "mScoreboard"], scoring_period_id=scoring_period_id, cookies=cookies).get("schedule", [])  # type: ignore[return-value]


def transactions(game_code: str, *, league_id: int, season: int, cookies: dict[str, str] | None = None) -> list[dict[str, Any]]:
    """All transactions: waiver claims, trades, FA adds/drops."""
    return fetch(game_code, league_id=league_id, season=season, views=["mTransactions2"], cookies=cookies).get("transactions", [])  # type: ignore[return-value]
