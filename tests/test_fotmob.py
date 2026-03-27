"""Tests for sportly.fotmob — mocked, no network."""
from __future__ import annotations

import httpx

from sportly.fotmob import LEAGUES, FotMobClient


def _mock(status: int, body) -> FotMobClient:
    def handler(req: httpx.Request) -> httpx.Response:
        return httpx.Response(status, json=body)
    c = FotMobClient()
    c._http = httpx.Client(transport=httpx.MockTransport(handler))
    return c


class TestFotMobConstants:
    def test_leagues_has_premier_league(self):
        assert "Premier League" in LEAGUES
        assert LEAGUES["Premier League"] == 47

    def test_leagues_has_champions_league(self):
        assert "Champions League" in LEAGUES
        assert LEAGUES["Champions League"] == 42


class TestFotMobEndpoints:
    def test_matches_today(self):
        import sportly.fotmob as fotmob
        body = {"leagues": [{"matches": [{"id": 4310531, "status": {"utcTime": "2026-03-26T15:00:00Z"}}]}]}
        c = _mock(200, body)
        result = fotmob.matches("20260326", client=c)
        assert "leagues" in result

    def test_match_detail(self):
        import sportly.fotmob as fotmob
        body = {"general": {"matchId": 4310531}, "content": {"stats": {}}}
        c = _mock(200, body)
        m = fotmob.match(4310531, client=c)
        assert m["general"]["matchId"] == 4310531

    def test_league_data(self):
        import sportly.fotmob as fotmob
        body = {"details": {"id": 47, "name": "Premier League"}, "table": []}
        c = _mock(200, body)
        data = fotmob.league(47, client=c)
        assert data["details"]["name"] == "Premier League"

    def test_team_data(self):
        import sportly.fotmob as fotmob
        body = {"details": {"id": 8456, "name": "Manchester City"}, "squad": []}
        c = _mock(200, body)
        t = fotmob.team(8456, client=c)
        assert t["details"]["name"] == "Manchester City"

    def test_player_data(self):
        import sportly.fotmob as fotmob
        body = {"id": 174543, "name": "Kevin De Bruyne", "primaryTeam": {"teamId": 8456}}
        c = _mock(200, body)
        p = fotmob.player(174543, client=c)
        assert p["name"] == "Kevin De Bruyne"

    def test_search(self):
        import sportly.fotmob as fotmob
        body = {"squad": [], "team": [{"id": 8456, "name": "Manchester City"}], "tournament": []}
        c = _mock(200, body)
        r = fotmob.search("man city", client=c)
        assert r["team"][0]["name"] == "Manchester City"

    def test_callable_api(self):
        import sportly.fotmob as fotmob
        assert callable(fotmob.matches)
        assert callable(fotmob.match)
        assert callable(fotmob.transfers)
        assert callable(fotmob.world_news)
