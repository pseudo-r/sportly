"""sportly.fantasy — ESPN Fantasy API (public and private leagues).

Base URL: https://lm-api-reads.fantasy.espn.com/apis/v3/games/{gameCode}/
Only v3 on lm-api-reads is active — v1/v2 are decommissioned.

Private leagues require cookies: ``espn_s2`` + ``SWID``.

Usage::

    from sportly import fantasy

    teams = fantasy.teams("ffl", league_id=336358, season=2025)
    draft = fantasy.draft("ffl", league_id=336358, season=2025)
    meta  = fantasy.game_meta("ffl")
    print(meta["currentSeasonId"])   # 2026

    print(fantasy.GAME_CODES)   # ffl / fba / flb / fhl
    print(fantasy.VIEWS)        # all supported view names

Endpoint subpackage::

    from sportly.fantasy.endpoints import league, players, meta
"""
from __future__ import annotations

import json
from typing import Any

from sportly.fantasy.endpoints._client import GAME_CODES, VIEWS, FantasyClient

__all__ = [
    "FantasyClient", "GAME_CODES", "VIEWS",
    "_get_client",
    "league", "teams", "roster", "standings", "draft",
    "live_scoring", "transactions", "players",
    "game_meta", "season_meta",
]

BASE_URL = "https://lm-api-reads.fantasy.espn.com/apis/v3/games"

# Module-level client accessor — exposed so tests can monkeypatch it
_default: FantasyClient | None = None


def _get_client(cookies: dict[str, str] | None = None) -> FantasyClient:
    """Return or create the module-level :class:`FantasyClient`."""
    global _default
    if cookies:
        return FantasyClient(cookies=cookies)
    if _default is None:
        _default = FantasyClient()
    return _default


# ── League ────────────────────────────────────────────────────────────────────

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
    """Raw league fetch with arbitrary view(s).

    Example::

        data = fantasy.league("ffl", league_id=123, season=2025, views=["mTeam","mRoster"])
    """
    http = _get_client(cookies)
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
    """All fantasy teams (names, owners, records)."""
    return league(game_code, league_id=league_id, season=season, views=["mTeam"], cookies=cookies).get("teams", [])  # type: ignore[return-value]


def roster(game_code: str, *, league_id: int, season: int, scoring_period_id: int | None = None, cookies: dict[str, str] | None = None) -> list[dict[str, Any]]:
    """All team rosters with player entries and lineup slot assignments."""
    return league(game_code, league_id=league_id, season=season, views=["mRoster"], scoring_period_id=scoring_period_id, cookies=cookies).get("teams", [])  # type: ignore[return-value]


def standings(game_code: str, *, league_id: int, season: int, cookies: dict[str, str] | None = None) -> list[dict[str, Any]]:
    """Teams with W/L/PF/PA standings."""
    return league(game_code, league_id=league_id, season=season, views=["mTeam", "mStandings"], cookies=cookies).get("teams", [])  # type: ignore[return-value]


def draft(game_code: str, *, league_id: int, season: int, cookies: dict[str, str] | None = None) -> dict[str, Any]:
    """Full draft history (picks, player IDs, round order)."""
    return league(game_code, league_id=league_id, season=season, views=["mDraftDetail"], cookies=cookies).get("draftDetail", {})  # type: ignore[return-value]


def live_scoring(game_code: str, *, league_id: int, season: int, scoring_period_id: int, cookies: dict[str, str] | None = None) -> list[dict[str, Any]]:
    """Live scoring for an active scoring period."""
    return league(game_code, league_id=league_id, season=season, views=["mBoxscore", "mLiveScoring", "mScoreboard"], scoring_period_id=scoring_period_id, cookies=cookies).get("schedule", [])  # type: ignore[return-value]


def transactions(game_code: str, *, league_id: int, season: int, cookies: dict[str, str] | None = None) -> list[dict[str, Any]]:
    """All transactions (waivers, trades, FA adds/drops)."""
    return league(game_code, league_id=league_id, season=season, views=["mTransactions2"], cookies=cookies).get("transactions", [])  # type: ignore[return-value]


# ── Players ───────────────────────────────────────────────────────────────────

def players(game_code: str, *, season: int, active_only: bool = True, cookies: dict[str, str] | None = None) -> list[dict[str, Any]]:
    """Full player pool for a sport/season."""
    http = _get_client(cookies)
    fantasy_filter = json.dumps({"filterActive": {"value": active_only}})
    path = f"{game_code}/seasons/{season}/players"
    data = http.get(path, headers={"X-Fantasy-Filter": fantasy_filter}, view="players_wl")
    return data if isinstance(data, list) else []  # type: ignore[return-value]


# ── Metadata ──────────────────────────────────────────────────────────────────

def game_meta(game_code: str, *, cookies: dict[str, str] | None = None) -> dict[str, Any]:
    """Game metadata (``currentSeasonId``, ``name``, ``active``). No league ID required."""
    return _get_client(cookies).get(game_code)  # type: ignore[return-value]


def season_meta(game_code: str, season: int, *, cookies: dict[str, str] | None = None) -> dict[str, Any]:
    """Season-level metadata (start/end dates, current scoring period)."""
    return _get_client(cookies).get(f"{game_code}/seasons/{season}")  # type: ignore[return-value]
