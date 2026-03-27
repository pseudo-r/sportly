"""Tests for sportly.mlb — all mocked, no network."""
from __future__ import annotations

import httpx
import pytest

from sportly.mlb._client import MLBClient

# ── Shared fixtures ───────────────────────────────────────────────────────────

TEAMS_RESPONSE = {
    "teams": [
        {"id": 119, "name": "Los Angeles Dodgers", "abbreviation": "LAD",
         "teamName": "Dodgers", "locationName": "Los Angeles",
         "league": {"name": "National League"}, "division": {"name": "NL West"}}
    ]
}
ROSTER_RESPONSE = {
    "roster": [
        {"person": {"id": 660271, "fullName": "Shohei Ohtani"}, "jerseyNumber": "17",
         "position": {"name": "Infielder", "abbreviation": "1B"}, "status": {"description": "Active"}}
    ]
}
SCHEDULE_RESPONSE = {
    "dates": [
        {
            "date": "2025-04-01",
            "games": [
                {"gamePk": 745444, "gameDate": "2025-04-01T22:10:00Z",
                 "status": {"detailedState": "Final"},
                 "teams": {
                     "home": {"team": {"name": "Los Angeles Dodgers"}, "score": 7},
                     "away": {"team": {"name": "San Diego Padres"}, "score": 2},
                 }}
            ],
        }
    ]
}
BOXSCORE_RESPONSE = {
    "teams": {"home": {"team": {"id": 119}, "teamStats": {}},
              "away": {"team": {"id": 135}, "teamStats": {}}},
    "officials": [], "info": [],
}
PBP_RESPONSE = {
    "allPlays": [
        {"result": {"event": "Strikeout", "description": "K"}, "about": {"inning": 1}},
    ]
}
STANDINGS_RESPONSE = {
    "records": [
        {"standingsType": "regularSeason", "league": {"id": 103},
         "division": {"name": "AL West"},
         "teamRecords": [{"team": {"name": "Houston Astros"}, "wins": 90, "losses": 72}]}
    ]
}
LEADERS_RESPONSE = {
    "leagueLeaders": [
        {"leaderCategory": "homeRuns", "leaders": [
            {"rank": 1, "value": "58", "person": {"fullName": "Aaron Judge"}}
        ]}
    ]
}
PLAYER_RESPONSE = {
    "people": [
        {"id": 660271, "fullName": "Shohei Ohtani", "primaryNumber": "17",
         "primaryPosition": {"name": "Designated Hitter"},
         "currentTeam": {"id": 119}, "active": True}
    ]
}


def _mock(status: int, body: dict):
    """Return an MLBClient backed by a mock transport."""
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(status, json=body)
    transport = httpx.MockTransport(handler)
    client = MLBClient()
    client._http = httpx.Client(transport=transport)
    return client


# ── Teams ─────────────────────────────────────────────────────────────────────

class TestMLBTeams:
    def test_all_teams(self):
        from sportly.mlb.endpoints import teams
        c = _mock(200, TEAMS_RESPONSE)
        result = teams.all(client=c)
        assert len(result) == 1
        assert result[0]["abbreviation"] == "LAD"

    def test_single_team(self):
        from sportly.mlb.endpoints import teams
        c = _mock(200, {"teams": [TEAMS_RESPONSE["teams"][0]]})
        t = teams.one(119, client=c)
        assert t["id"] == 119

    def test_roster(self):
        from sportly.mlb.endpoints import teams
        c = _mock(200, ROSTER_RESPONSE)
        r = teams.roster(119, client=c)
        assert r[0]["person"]["fullName"] == "Shohei Ohtani"


# ── Schedule ──────────────────────────────────────────────────────────────────

class TestMLBSchedule:
    def test_games_returns_flat_list(self):
        from sportly.mlb.endpoints import schedule
        c = _mock(200, SCHEDULE_RESPONSE)
        result = schedule.games(date="2025-04-01", client=c)
        assert isinstance(result, list)
        assert result[0]["gamePk"] == 745444

    def test_games_empty_dates(self):
        from sportly.mlb.endpoints import schedule
        c = _mock(200, {"dates": []})
        result = schedule.games(date="2025-01-01", client=c)
        assert result == []

    def test_today_delegates(self):
        from sportly.mlb.endpoints import schedule
        c = _mock(200, SCHEDULE_RESPONSE)
        result = schedule.today(client=c)
        assert len(result) == 1


# ── Players ───────────────────────────────────────────────────────────────────

class TestMLBPlayers:
    def test_player_profile(self):
        from sportly.mlb.endpoints import players
        c = _mock(200, PLAYER_RESPONSE)
        p = players.player(660271, client=c)
        assert p["fullName"] == "Shohei Ohtani"

    def test_player_not_found(self):
        from sportly.exceptions import NotFoundError
        from sportly.mlb.endpoints import players
        c = _mock(404, {})
        with pytest.raises(NotFoundError):
            players.player(999999, client=c)

    def test_search(self):
        from sportly.mlb.endpoints import players
        c = _mock(200, PLAYER_RESPONSE)
        result = players.search("Ohtani", client=c)
        assert result[0]["id"] == 660271


# ── Games ─────────────────────────────────────────────────────────────────────

class TestMLBGames:
    def test_boxscore(self):
        from sportly.mlb.endpoints import games
        c = _mock(200, BOXSCORE_RESPONSE)
        box = games.boxscore(745444, client=c)
        assert "teams" in box

    def test_play_by_play(self):
        from sportly.mlb.endpoints import games
        c = _mock(200, PBP_RESPONSE)
        pbp = games.play_by_play(745444, client=c)
        assert pbp["allPlays"][0]["result"]["event"] == "Strikeout"


# ── Stats / League ────────────────────────────────────────────────────────────

class TestMLBStats:
    def test_standings(self):
        from sportly.mlb.endpoints import stats
        c = _mock(200, STANDINGS_RESPONSE)
        records = stats.standings(season=2025, client=c)
        assert records[0]["teamRecords"][0]["wins"] == 90

    def test_leaders(self):
        from sportly.mlb.endpoints import stats
        c = _mock(200, LEADERS_RESPONSE)
        result = stats.leaders("homeRuns", season=2025, client=c)
        assert result[0]["leaderCategory"] == "homeRuns"
        assert result[0]["leaders"][0]["person"]["fullName"] == "Aaron Judge"

    def test_transactions(self):
        from sportly.mlb.endpoints import stats
        payload = {"transactions": [
            {"id": 1, "typeDesc": "Trade", "description": "Player A traded", "date": "2025-03-01"}
        ]}
        c = _mock(200, payload)
        tx = stats.transactions(start_date="2025-03-01", end_date="2025-03-10", client=c)
        assert tx[0]["typeDesc"] == "Trade"

    def test_venues(self):
        from sportly.mlb.endpoints import stats
        payload = {"venues": [{"id": 22, "name": "Dodger Stadium"}]}
        c = _mock(200, payload)
        result = stats.venues(venue_id=22, client=c)
        assert result[0]["name"] == "Dodger Stadium"


# ── Top-level module API ──────────────────────────────────────────────────────

class TestMLBModule:
    def test_module_imports(self):
        import sportly.mlb as mlb
        assert callable(mlb.teams)
        assert callable(mlb.schedule)
        assert callable(mlb.player)
        assert callable(mlb.boxscore)
        assert callable(mlb.leaders)
        assert callable(mlb.standings)
        assert "LAD" in mlb.TEAM_IDS
        assert mlb.TEAM_IDS["LAD"] == 119

    def test_module_teams(self):
        import sportly.mlb as mlb
        c = _mock(200, TEAMS_RESPONSE)
        result = mlb.teams(client=c)
        assert result[0]["abbreviation"] == "LAD"

    def test_module_schedule(self):
        import sportly.mlb as mlb
        c = _mock(200, SCHEDULE_RESPONSE)
        result = mlb.schedule(date="2025-04-01", client=c)
        assert result[0]["gamePk"] == 745444
