"""Tests for sportly.fantasy — mocked, no network."""
from __future__ import annotations

import httpx

from sportly.fantasy import GAME_CODES, FantasyClient


def _mock(status: int, body) -> FantasyClient:
    def handler(req: httpx.Request) -> httpx.Response:
        return httpx.Response(status, json=body)
    c = FantasyClient()
    c._http = httpx.Client(transport=httpx.MockTransport(handler))
    return c


LEAGUE_BODY = {
    "id": 336358,
    "teams": [
        {"id": 1, "name": "Team Alpha", "record": {"overall": {"wins": 10, "losses": 3}}}
    ],
    "draftDetail": {"picks": [{"playerId": 2544}]},
    "transactions": [{"id": "t1", "type": "WAIVER"}],
    "schedule": [{"id": "m1", "home": {}, "away": {}}],
}

META_BODY = {"abbrev": "FFL", "active": True, "currentSeasonId": 2026, "name": "Fantasy Football"}


class TestFantasyGameCodes:
    def test_game_codes_defined(self):
        assert "ffl" in GAME_CODES
        assert "fba" in GAME_CODES
        assert "flb" in GAME_CODES
        assert "fhl" in GAME_CODES


class TestFantasyModule:
    def test_game_meta(self):
        import sportly.fantasy as fantasy
        c = _mock(200, META_BODY)
        # patch the internal client
        import sportly.fantasy as fm
        orig = fm._get_client
        fm._get_client = lambda cookies=None: c
        try:
            meta = fantasy.game_meta("ffl")
            assert meta["currentSeasonId"] == 2026
        finally:
            fm._get_client = orig

    def test_league_returns_raw(self):
        import sportly.fantasy as fantasy
        import sportly.fantasy as fm
        c = _mock(200, LEAGUE_BODY)
        orig = fm._get_client
        fm._get_client = lambda cookies=None: c
        try:
            data = fantasy.league("ffl", league_id=336358, season=2025)
            assert data["id"] == 336358
        finally:
            fm._get_client = orig

    def test_teams_extracts_teams(self):
        import sportly.fantasy as fantasy
        import sportly.fantasy as fm
        c = _mock(200, LEAGUE_BODY)
        orig = fm._get_client
        fm._get_client = lambda cookies=None: c
        try:
            teams = fantasy.teams("ffl", league_id=336358, season=2025)
            assert teams[0]["name"] == "Team Alpha"
        finally:
            fm._get_client = orig

    def test_draft_extracts_draft_detail(self):
        import sportly.fantasy as fantasy
        import sportly.fantasy as fm
        c = _mock(200, LEAGUE_BODY)
        orig = fm._get_client
        fm._get_client = lambda cookies=None: c
        try:
            d = fantasy.draft("ffl", league_id=336358, season=2025)
            assert d["picks"][0]["playerId"] == 2544
        finally:
            fm._get_client = orig

    def test_callable_api(self):
        import sportly.fantasy as fantasy
        assert callable(fantasy.league)
        assert callable(fantasy.standings)
        assert callable(fantasy.live_scoring)
        assert callable(fantasy.transactions)
