"""sportly.fantasy — ESPN Fantasy API (public leagues only, no auth for read).

Base URL: https://lm-api-reads.fantasy.espn.com/apis/v3/games/{gameCode}/
Only v3 on lm-api-reads.fantasy.espn.com is active. v1/v2 are dead.

Private leagues require cookies: espn_s2 + SWID

Usage::

    from sportly import fantasy

    # Public league (no auth)
    info  = fantasy.league("ffl", league_id=336358, season=2025, views=["mTeam"])
    teams = fantasy.teams("ffl", league_id=336358, season=2025)
    draft = fantasy.draft("ffl", league_id=336358, season=2025)

    # Private league (requires cookies)
    private = fantasy.league(
        "ffl", league_id=123456, season=2025, views=["mRoster"],
        cookies={"espn_s2": "...", "SWID": "{...}"},
    )

    # Game metadata
    meta = fantasy.game_meta("ffl")

    # All sport codes
    print(fantasy.GAME_CODES)
"""
from __future__ import annotations
from typing import Any

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential
from sportly.exceptions import NotFoundError, RateLimitError, SportlyError

BASE_URL = "https://lm-api-reads.fantasy.espn.com/apis/v3/games"

# ── Constants ─────────────────────────────────────────────────────────────────
GAME_CODES: dict[str, str] = {
    "ffl": "Fantasy Football",
    "fba": "Fantasy Basketball",
    "flb": "Fantasy Baseball",
    "fhl": "Fantasy Hockey",
}

VIEWS = {
    "mSettings", "mTeam", "mRoster", "mMatchupScore", "mMatchup",
    "mScoreboard", "mStandings", "mSchedule", "mBoxscore", "mLiveScoring",
    "mDraftDetail", "mTransactions2", "mStatus", "kona_player_info",
    "proTeamSchedules_wl",
}

# ── Client ────────────────────────────────────────────────────────────────────

class FantasyClient:
    """Thin client for lm-api-reads.fantasy.espn.com."""

    def __init__(self, timeout: float = 10.0, cookies: dict[str, str] | None = None) -> None:
        self._http = httpx.Client(
            headers={"Accept": "application/json"},
            cookies=cookies or {},
            timeout=timeout,
        )

    @retry(
        retry=retry_if_exception_type(httpx.TransportError),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=0.5, min=0.5, max=8),
        reraise=True,
    )
    def get(self, path: str, *, headers: dict | None = None, **params) -> Any:
        url = f"{BASE_URL}/{path.lstrip('/')}"
        try:
            resp = self._http.get(
                url,
                params={k: v for k, v in params.items() if v is not None},
                headers=headers or {},
            )
        except httpx.TransportError as exc:
            raise SportlyError(str(exc)) from exc
        if resp.status_code == 404:
            raise NotFoundError(f"Not found: {url}", status_code=404, url=url)
        if resp.status_code == 429:
            raise RateLimitError("ESPN Fantasy rate limited", status_code=429)
        resp.raise_for_status()
        return resp.json()

    def close(self) -> None:
        self._http.close()

    def __enter__(self): return self
    def __exit__(self, *_): self.close()


_default: FantasyClient | None = None

def _get_client(cookies: dict[str, str] | None = None) -> FantasyClient:
    global _default
    if cookies:
        return FantasyClient(cookies=cookies)
    if _default is None:
        _default = FantasyClient()
    return _default


# ── Public API ────────────────────────────────────────────────────────────────

def league(
    game_code: str,
    *,
    league_id: int,
    season: int,
    views: list[str] | None = None,
    scoring_period_id: int | None = None,
    matchup_period_id: int | None = None,
    cookies: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Fetch league data by view(s).

    Parameters
    ----------
    game_code:        ``"ffl"`` (football), ``"fba"``, ``"flb"``, ``"fhl"``.
    league_id:        Your ESPN Fantasy league ID.
    season:           Season year, e.g. ``2025``.
    views:            List of view names. Multiple views can reduce round-trips.
    scoring_period_id: Filter by week (football) or day (baseball/basketball).
    cookies:          ``{"espn_s2": "...", "SWID": "{...}"}`` for private leagues.

    Example
    -------
    ::

        # Teams + rosters in one call
        data = fantasy.league("ffl", league_id=123, season=2025,
                               views=["mTeam", "mRoster"])
    """
    http = _get_client(cookies)
    path = f"{game_code}/seasons/{season}/segments/0/leagues/{league_id}"
    params: dict[str, Any] = {}
    if views:
        # httpx accepts list params natively as repeated query keys
        params["view"] = views
    if scoring_period_id is not None:
        params["scoringPeriodId"] = scoring_period_id
    if matchup_period_id is not None:
        params["matchupPeriodId"] = matchup_period_id
    return http.get(path, **params)  # type: ignore[return-value]


def teams(
    game_code: str,
    *,
    league_id: int,
    season: int,
    cookies: dict[str, str] | None = None,
) -> list[dict[str, Any]]:
    """Return all fantasy teams (names, owners, records)."""
    data = league(game_code, league_id=league_id, season=season, views=["mTeam"], cookies=cookies)
    return data.get("teams", [])  # type: ignore[return-value]


def roster(
    game_code: str,
    *,
    league_id: int,
    season: int,
    scoring_period_id: int | None = None,
    cookies: dict[str, str] | None = None,
) -> list[dict[str, Any]]:
    """Return all team rosters with player entries and lineup slots."""
    data = league(
        game_code, league_id=league_id, season=season,
        views=["mRoster"], scoring_period_id=scoring_period_id, cookies=cookies,
    )
    return data.get("teams", [])  # type: ignore[return-value]


def standings(
    game_code: str,
    *,
    league_id: int,
    season: int,
    cookies: dict[str, str] | None = None,
) -> list[dict[str, Any]]:
    """Return teams with standings (W/L, points for/against)."""
    data = league(game_code, league_id=league_id, season=season, views=["mTeam", "mStandings"], cookies=cookies)
    return data.get("teams", [])  # type: ignore[return-value]


def draft(
    game_code: str,
    *,
    league_id: int,
    season: int,
    cookies: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Return full draft history (picks, player IDs, round order)."""
    data = league(game_code, league_id=league_id, season=season, views=["mDraftDetail"], cookies=cookies)
    return data.get("draftDetail", {})  # type: ignore[return-value]


def live_scoring(
    game_code: str,
    *,
    league_id: int,
    season: int,
    scoring_period_id: int,
    cookies: dict[str, str] | None = None,
) -> list[dict[str, Any]]:
    """Return live scoring for an active scoring period."""
    data = league(
        game_code, league_id=league_id, season=season,
        views=["mBoxscore", "mLiveScoring", "mScoreboard"],
        scoring_period_id=scoring_period_id, cookies=cookies,
    )
    return data.get("schedule", [])  # type: ignore[return-value]


def transactions(
    game_code: str,
    *,
    league_id: int,
    season: int,
    cookies: dict[str, str] | None = None,
) -> list[dict[str, Any]]:
    """Return all transactions (waivers, trades, FA adds)."""
    data = league(game_code, league_id=league_id, season=season, views=["mTransactions2"], cookies=cookies)
    return data.get("transactions", [])  # type: ignore[return-value]


def players(
    game_code: str,
    *,
    season: int,
    active_only: bool = True,
    cookies: dict[str, str] | None = None,
) -> list[dict[str, Any]]:
    """Return all players in the player pool.

    Parameters
    ----------
    active_only: Filter to only active players (default ``True``).
    """
    http = _get_client(cookies)
    import json
    fantasy_filter = json.dumps({"filterActive": {"value": active_only}})
    path = f"{game_code}/seasons/{season}/players"
    data = http.get(path, headers={"X-Fantasy-Filter": fantasy_filter}, view="players_wl")
    return data if isinstance(data, list) else []  # type: ignore[return-value]


def game_meta(game_code: str, *, cookies: dict[str, str] | None = None) -> dict[str, Any]:
    """Return game metadata (currentSeasonId, name, active).

    Does not require a league ID.

    Example
    -------
    ::

        meta = fantasy.game_meta("ffl")
        print(meta["currentSeasonId"])   # 2026
    """
    return _get_client(cookies).get(game_code)  # type: ignore[return-value]


def season_meta(game_code: str, season: int, *, cookies: dict[str, str] | None = None) -> dict[str, Any]:
    """Return season info (start/end dates, current scoring period)."""
    return _get_client(cookies).get(f"{game_code}/seasons/{season}")  # type: ignore[return-value]
