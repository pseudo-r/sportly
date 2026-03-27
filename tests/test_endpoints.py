"""Tests for endpoint submodule files — sofascore, fotmob, fantasy, nfl endpoints.

These tests exercise the endpoint files directly (not via __init__.py) to boost coverage
of the new endpoint subpackage structure.
"""
from __future__ import annotations
import pytest


# ── Sofascore endpoint submodules ─────────────────────────────────────────────

class TestSofascoreScheduleEp:
    def test_matches_football(self, monkeypatch):
        import sportly.sofascore.endpoints.schedule as schedep
        monkeypatch.setattr(schedep, "get", lambda path, client=None: {"events": [{"id": 1}]})
        result = schedep.matches("football", "2026-03-26")
        assert result[0]["id"] == 1

    def test_matches_soccer_alias(self, monkeypatch):
        import sportly.sofascore.endpoints.schedule as schedep
        monkeypatch.setattr(schedep, "get", lambda path, client=None: {"events": [{"id": 2}]})
        result = schedep.matches("soccer", "2026-03-26")
        assert result[0]["id"] == 2

    def test_matches_tennis_tournaments(self, monkeypatch):
        import sportly.sofascore.endpoints.schedule as schedep
        monkeypatch.setattr(schedep, "get", lambda path, client=None: {"tournaments": [{"id": 9}]})
        result = schedep.matches("tennis", "2026-03-26")
        assert result[0]["id"] == 9


class TestSofascoreEventsEp:
    def _patch(self, monkeypatch, body):
        import sportly.sofascore.endpoints.events as evep
        monkeypatch.setattr(evep, "get", lambda path, client=None: body)
        return evep

    def test_match(self, monkeypatch):
        ep = self._patch(monkeypatch, {"event": {"id": 999}})
        assert ep.match(999)["event"]["id"] == 999

    def test_stats(self, monkeypatch):
        ep = self._patch(monkeypatch, {"statistics": []})
        assert "statistics" in ep.stats(999)

    def test_lineups(self, monkeypatch):
        ep = self._patch(monkeypatch, {"home": {"players": []}})
        assert "home" in ep.lineups(999)

    def test_incidents(self, monkeypatch):
        ep = self._patch(monkeypatch, {"incidents": []})
        assert "incidents" in ep.incidents(999)

    def test_momentum(self, monkeypatch):
        ep = self._patch(monkeypatch, {"graphPoints": []})
        assert "graphPoints" in ep.momentum(999)

    def test_point_by_point(self, monkeypatch):
        ep = self._patch(monkeypatch, {"sets": []})
        assert "sets" in ep.point_by_point(999)


class TestSofascorePlayersEp:
    def test_player(self, monkeypatch):
        import sportly.sofascore.endpoints.players as plep
        monkeypatch.setattr(plep, "get", lambda path, client=None: {"player": {"id": 1}})
        assert plep.player(1)["player"]["id"] == 1

    def test_seasons(self, monkeypatch):
        import sportly.sofascore.endpoints.players as plep
        monkeypatch.setattr(plep, "get", lambda path, client=None: {"seasons": []})
        assert "seasons" in plep.seasons(1)


class TestSofascoreTeamsEp:
    def test_team(self, monkeypatch):
        import sportly.sofascore.endpoints.teams as tep
        monkeypatch.setattr(tep, "get", lambda path, client=None: {"team": {"id": 4705}})
        assert tep.team(4705)["team"]["id"] == 4705

    def test_squad(self, monkeypatch):
        import sportly.sofascore.endpoints.teams as tep
        monkeypatch.setattr(tep, "get", lambda path, client=None: {"players": [{"id": 1}]})
        result = tep.squad(4705)
        assert result[0]["id"] == 1


class TestSofascoreTournamentsEp:
    def test_tournaments(self, monkeypatch):
        import sportly.sofascore.endpoints.tournaments as trnep
        monkeypatch.setattr(trnep, "get", lambda path, client=None: {"uniqueTournaments": []})
        assert "uniqueTournaments" in trnep.tournaments("football")

    def test_popular(self, monkeypatch):
        import sportly.sofascore.endpoints.tournaments as trnep
        monkeypatch.setattr(trnep, "get", lambda path, client=None: {"entities": []})
        assert "entities" in trnep.popular("US")

    def test_sports_constant(self):
        from sportly.sofascore.endpoints._client import SPORTS
        assert SPORTS["soccer"] == "football"
        assert SPORTS["hockey"] == "ice-hockey"


# ── FotMob endpoint submodules ────────────────────────────────────────────────

class _FotMobMockClient:
    def __init__(self, body):
        self._body = body
    def get(self, endpoint, **params):
        return self._body


class TestFotMobMatchesEp:
    def test_matches(self):
        from sportly.fotmob.endpoints import matches
        c = _FotMobMockClient({"leagues": []})
        assert matches.matches("20260326", client=c) == {"leagues": []}

    def test_match(self):
        from sportly.fotmob.endpoints import matches
        c = _FotMobMockClient({"id": 99})
        assert matches.match(99, client=c) == {"id": 99}


class TestFotMobLeaguesEp:
    def test_league(self):
        from sportly.fotmob.endpoints import leagues
        c = _FotMobMockClient({"table": []})
        assert leagues.league(47, client=c) == {"table": []}

    def test_all_leagues(self):
        from sportly.fotmob.endpoints import leagues
        c = _FotMobMockClient({"international": []})
        assert leagues.all_leagues(client=c) == {"international": []}

    def test_tv_listings(self):
        from sportly.fotmob.endpoints import leagues
        c = _FotMobMockClient({"listings": []})
        assert leagues.tv_listings(date="20260326", client=c) == {"listings": []}

    def test_leagues_constant(self):
        from sportly.fotmob.endpoints._client import LEAGUES
        assert LEAGUES["Premier League"] == 47
        assert LEAGUES["Champions League"] == 42


class TestFotMobTeamsEp:
    def test_team(self):
        from sportly.fotmob.endpoints import teams
        c = _FotMobMockClient({"details": {"id": 8456}})
        assert teams.team(8456, client=c)["details"]["id"] == 8456


class TestFotMobPlayersEp:
    def test_player(self):
        from sportly.fotmob.endpoints import players
        c = _FotMobMockClient({"career": []})
        assert players.player(174543, client=c) == {"career": []}

    def test_search(self):
        from sportly.fotmob.endpoints import players
        c = _FotMobMockClient({"squad": [], "team": [], "tournament": []})
        r = players.search("haaland", client=c)
        assert "squad" in r

    def test_transfers(self):
        from sportly.fotmob.endpoints import players
        c = _FotMobMockClient({"data": []})
        assert players.transfers(client=c) == {"data": []}

    def test_world_news(self):
        from sportly.fotmob.endpoints import players
        c = _FotMobMockClient({"articles": []})
        assert players.world_news(client=c) == {"articles": []}


# ── Fantasy endpoint submodules ───────────────────────────────────────────────

class _FantasyMockClient:
    def __init__(self, body):
        self._body = body
    def get(self, path, *, headers=None, **params):
        return self._body


class TestFantasyLeagueEp:
    def _mock(self, body):
        return _FantasyMockClient(body)

    def test_fetch(self, monkeypatch):
        import sportly.fantasy.endpoints.league as lep
        monkeypatch.setattr(lep, "get_client", lambda cookies=None: _FantasyMockClient({"teams": [{"id": 1}]}))
        r = lep.fetch("ffl", league_id=123, season=2025, views=["mTeam"])
        assert r["teams"][0]["id"] == 1

    def test_teams(self, monkeypatch):
        import sportly.fantasy.endpoints.league as lep
        monkeypatch.setattr(lep, "get_client", lambda cookies=None: _FantasyMockClient({"teams": [{"id": 2}]}))
        r = lep.teams("ffl", league_id=123, season=2025)
        assert r[0]["id"] == 2

    def test_standings(self, monkeypatch):
        import sportly.fantasy.endpoints.league as lep
        monkeypatch.setattr(lep, "get_client", lambda cookies=None: _FantasyMockClient({"teams": [{"rank": 1}]}))
        r = lep.standings("ffl", league_id=123, season=2025)
        assert r[0]["rank"] == 1

    def test_draft(self, monkeypatch):
        import sportly.fantasy.endpoints.league as lep
        monkeypatch.setattr(lep, "get_client", lambda cookies=None: _FantasyMockClient({"draftDetail": {"picks": []}}))
        r = lep.draft("ffl", league_id=123, season=2025)
        assert "picks" in r


class TestFantasyMetaEp:
    def test_game_meta(self, monkeypatch):
        import sportly.fantasy.endpoints.meta as mep
        monkeypatch.setattr(mep, "get_client", lambda cookies=None: _FantasyMockClient({"currentSeasonId": 2026}))
        r = mep.game_meta("ffl")
        assert r["currentSeasonId"] == 2026

    def test_season_meta(self, monkeypatch):
        import sportly.fantasy.endpoints.meta as mep
        monkeypatch.setattr(mep, "get_client", lambda cookies=None: _FantasyMockClient({"id": 2025}))
        r = mep.season_meta("ffl", 2025)
        assert r["id"] == 2025

    def test_game_codes_constant(self):
        from sportly.fantasy.endpoints._client import GAME_CODES
        assert "ffl" in GAME_CODES
        assert "fba" in GAME_CODES


# ── NFL endpoint submodules ───────────────────────────────────────────────────

def _mock_nfl_client(body: dict):
    import httpx
    from sportly.client import SportlyClient
    c = SportlyClient()
    c._http = httpx.Client(transport=httpx.MockTransport(lambda req: httpx.Response(200, json=body)))
    return c


class TestNFLGamesEp:
    def test_scoreboard_structure(self):
        import sportly.nfl.endpoints.games as g
        c = _mock_nfl_client({"events": [{"id": "401671827"}]})
        result = g.scoreboard(week=1, season=2024, client=c)
        assert isinstance(result, list)
        assert result[0]["id"] == "401671827"

    def test_scoreboard_empty(self):
        import sportly.nfl.endpoints.games as g
        c = _mock_nfl_client({})
        result = g.scoreboard(client=c)
        assert result == []


class TestNFLLeagueEp:
    def test_news_delegates_to_espn(self, monkeypatch):
        import sportly.espn.endpoints.news as news_ep
        monkeypatch.setattr(news_ep, "news", lambda sport, league, limit=25, client=None: [{"headline": "TD"}])
        import sportly.nfl.endpoints.league as le
        result = le.news()
        assert result[0]["headline"] == "TD"

    def test_injuries_delegates_to_espn(self, monkeypatch):
        import sportly.espn.endpoints.advanced as adv
        monkeypatch.setattr(adv, "injuries", lambda sport, league, client=None: [{"team": "KC"}])
        import sportly.nfl.endpoints.league as le
        result = le.injuries()
        assert result[0]["team"] == "KC"

    def test_transactions_delegates_to_espn(self, monkeypatch):
        import sportly.espn.endpoints.advanced as adv
        monkeypatch.setattr(adv, "transactions", lambda sport, league, client=None: [{"type": "trade"}])
        import sportly.nfl.endpoints.league as le
        result = le.transactions()
        assert result[0]["type"] == "trade"


# ── NHL endpoint submodules ───────────────────────────────────────────────────

def _mock_nhl_client(body: dict):
    """Return an NHLClient whose _get() is monkeypatched to return body."""
    from sportly.nhl._client import NHLClient
    c = NHLClient()
    c._get = lambda path, **params: body
    return c


class TestNHLGamesEp:
    def test_boxscore_returns_dict(self):
        from sportly.nhl.endpoints import games
        c = _mock_nhl_client({"id": "2024020001", "homeTeam": {"abbrev": "TOR"}})
        result = games.boxscore("2024020001", client=c)
        assert result["homeTeam"]["abbrev"] == "TOR"

    def test_play_by_play_returns_dict(self):
        from sportly.nhl.endpoints import games
        c = _mock_nhl_client({"plays": [{"typeDescKey": "shot-on-goal"}]})
        result = games.play_by_play("2024020001", client=c)
        assert result["plays"][0]["typeDescKey"] == "shot-on-goal"

    def test_landing_returns_dict(self):
        from sportly.nhl.endpoints import games
        c = _mock_nhl_client({"gameState": "FINAL"})
        result = games.landing("2024020001", client=c)
        assert result["gameState"] == "FINAL"


class TestNHLScheduleEp:
    def test_schedule_today(self):
        from sportly.nhl.endpoints import schedule
        c = _mock_nhl_client({"gameWeek": []})
        result = schedule.schedule(client=c)
        assert "gameWeek" in result

    def test_schedule_specific_date(self):
        from sportly.nhl.endpoints import schedule
        c = _mock_nhl_client({"gameWeek": [{"date": "2024-04-15"}]})
        result = schedule.schedule("2024-04-15", client=c)
        assert result["gameWeek"][0]["date"] == "2024-04-15"

    def test_weekly_schedule(self):
        from sportly.nhl.endpoints import schedule
        c = _mock_nhl_client({"gameWeek": [{"date": "2024-04-15"}, {"date": "2024-04-16"}]})
        result = schedule.weekly(client=c)
        assert len(result["gameWeek"]) == 2


class TestNHLTeamsEp:
    def test_franchises_returns_list(self):
        from sportly.nhl.endpoints import teams
        c = _mock_nhl_client({"data": [{"id": 1, "fullName": "Montreal Canadiens"}]})
        result = teams.franchises(client=c)
        assert result[0]["fullName"] == "Montreal Canadiens"

    def test_franchises_empty_data(self):
        from sportly.nhl.endpoints import teams
        c = _mock_nhl_client({})
        result = teams.franchises(client=c)
        assert result == []

    def test_roster_current(self):
        from sportly.nhl.endpoints import teams
        c = _mock_nhl_client({"forwards": [], "defense": [], "goalies": []})
        result = teams.roster("TOR", client=c)
        assert "forwards" in result

    def test_roster_historical(self):
        from sportly.nhl.endpoints import teams
        c = _mock_nhl_client({"forwards": [{"lastName": {"default": "Sundin"}}]})
        result = teams.roster("TOR", "20052006", client=c)
        assert result["forwards"][0]["lastName"]["default"] == "Sundin"

    def test_standings_current(self):
        from sportly.nhl.endpoints import teams
        c = _mock_nhl_client({"standings": [{"teamAbbrev": {"default": "TOR"}}]})
        result = teams.standings(client=c)
        assert result["standings"][0]["teamAbbrev"]["default"] == "TOR"

    def test_standings_by_date(self):
        from sportly.nhl.endpoints import teams
        c = _mock_nhl_client({"standings": []})
        result = teams.standings(date="2024-03-01", client=c)
        assert "standings" in result

    def test_player_profile(self):
        from sportly.nhl.endpoints import teams
        c = _mock_nhl_client({"playerId": 8481528, "firstName": {"default": "Connor"}})
        result = teams.player(8481528, client=c)
        assert result["firstName"]["default"] == "Connor"


class TestNHLModulePublicAPI:
    def test_all_functions_callable(self):
        import sportly.nhl as nhl
        for fn in ["teams", "schedule", "game", "play_by_play", "landing",
                   "roster", "standings", "player", "weekly"]:
            assert callable(getattr(nhl, fn)), f"nhl.{fn} not callable"


# ── Fantasy players endpoint ──────────────────────────────────────────────────

class TestFantasyPlayersEp:
    def test_players_returns_list(self, monkeypatch):
        import sportly.fantasy.endpoints.players as pep
        monkeypatch.setattr(pep, "get_client",
            lambda cookies=None: _FantasyMockClient([{"id": 1, "fullName": "Patrick Mahomes"}]))
        result = pep.players("ffl", season=2025)
        assert result[0]["fullName"] == "Patrick Mahomes"

    def test_players_non_list_response_returns_empty(self, monkeypatch):
        import sportly.fantasy.endpoints.players as pep
        monkeypatch.setattr(pep, "get_client",
            lambda cookies=None: _FantasyMockClient({"error": "no data"}))
        result = pep.players("ffl", season=2025)
        assert result == []

    def test_players_active_only_false(self, monkeypatch):
        import sportly.fantasy.endpoints.players as pep
        monkeypatch.setattr(pep, "get_client",
            lambda cookies=None: _FantasyMockClient([{"id": 99}]))
        result = pep.players("ffl", season=2025, active_only=False)
        assert result[0]["id"] == 99

    def test_players_with_cookies(self, monkeypatch):
        import sportly.fantasy.endpoints.players as pep
        cookies = {"espn_s2": "abc", "SWID": "{xyz}"}
        monkeypatch.setattr(pep, "get_client",
            lambda cookies=None: _FantasyMockClient([{"id": 7}]))
        result = pep.players("fba", season=2025, cookies=cookies)
        assert result[0]["id"] == 7
