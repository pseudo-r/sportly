"""Tests for sportly.sofascore — mocked without curl_cffi (patches _get)."""
from __future__ import annotations

import pytest

# ── Sofascore tests use monkeypatching on the internal _get function ──────────
# because curl_cffi isn't installed in the test env (it's an optional extra).

MATCH_BODY  = {"event": {"id": 11352523, "tournament": {"name": "World Cup"}, "homeScore": {"current": 2}}}
STATS_BODY  = {"statistics": [{"period": "ALL", "groups": [{"groupName": "Football", "statisticsItems": []}]}]}
LINEUP_BODY = {"home": {"players": [{"player": {"name": "Ronaldo"}}]}, "away": {"players": []}}
PLAYER_BODY = {"player": {"id": 814123, "name": "Erling Haaland", "team": {"name": "Manchester City"}}}
TEAM_BODY   = {"team": {"id": 4705, "name": "Juventus"}}
SQUAD_BODY  = {"players": [{"player": {"id": 814123, "name": "Erling Haaland"}}]}
EVENTS_BODY = {"events": [{"id": 11352523, "homeTeam": {"name": "France"}, "awayTeam": {"name": "Germany"}}]}
TOURS_BODY  = {"uniqueTournaments": [{"id": 47, "name": "Premier League"}]}


class TestSofascoreConstants:
    def test_sports_slugs(self):
        from sportly.sofascore import SPORTS
        assert "football" in SPORTS
        assert SPORTS["soccer"] == "football"
        assert SPORTS["hockey"] == "ice-hockey"


class TestSofascoreEndpoints:
    def _patch(self, monkeypatch, body):
        import sportly.sofascore as ss
        monkeypatch.setattr(ss, "_get", lambda path, client=None: body)

    def test_matches_football(self, monkeypatch):
        import sportly.sofascore as ss
        monkeypatch.setattr(ss, "_get", lambda path, client=None: EVENTS_BODY)
        result = ss.matches("football", "2026-03-26")
        assert result[0]["homeTeam"]["name"] == "France"

    def test_match_detail(self, monkeypatch):
        self._patch(monkeypatch, MATCH_BODY)
        import sportly.sofascore as ss
        m = ss.match(11352523)
        assert m["event"]["id"] == 11352523

    def test_match_stats(self, monkeypatch):
        self._patch(monkeypatch, STATS_BODY)
        import sportly.sofascore as ss
        s = ss.match_stats(11352523)
        assert "statistics" in s

    def test_lineups(self, monkeypatch):
        self._patch(monkeypatch, LINEUP_BODY)
        import sportly.sofascore as ss
        l = ss.lineups(11352523)
        assert l["home"]["players"][0]["player"]["name"] == "Ronaldo"

    def test_player(self, monkeypatch):
        self._patch(monkeypatch, PLAYER_BODY)
        import sportly.sofascore as ss
        p = ss.player(814123)
        assert p["player"]["name"] == "Erling Haaland"

    def test_team(self, monkeypatch):
        self._patch(monkeypatch, TEAM_BODY)
        import sportly.sofascore as ss
        t = ss.team(4705)
        assert t["team"]["name"] == "Juventus"

    def test_squad_extracts_players(self, monkeypatch):
        self._patch(monkeypatch, SQUAD_BODY)
        import sportly.sofascore as ss
        players = ss.squad(4705)
        assert players[0]["player"]["name"] == "Erling Haaland"

    def test_tournaments(self, monkeypatch):
        self._patch(monkeypatch, TOURS_BODY)
        import sportly.sofascore as ss
        t = ss.tournaments("football")
        assert "uniqueTournaments" in t

    def test_callable_api(self):
        import sportly.sofascore as ss
        assert callable(ss.matches)
        assert callable(ss.match)
        assert callable(ss.player)
        assert callable(ss.squad)
        assert callable(ss.momentum)
        assert callable(ss.popular)

    def test_missing_curl_cffi_raises_import_error(self):
        """Without curl_cffi, _get_client() raises ImportError with helpful message."""
        import sys
        # Temporarily hide curl_cffi
        saved = sys.modules.get("curl_cffi")
        sys.modules["curl_cffi"] = None  # type: ignore
        try:
            import sportly.sofascore as ss
            with pytest.raises(ImportError, match="curl_cffi"):
                ss._get_client()
        finally:
            if saved is None:
                sys.modules.pop("curl_cffi", None)
            else:
                sys.modules["curl_cffi"] = saved
