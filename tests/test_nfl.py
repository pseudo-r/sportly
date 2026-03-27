"""Tests for sportly.nfl — mocked ESPN calls, no network."""
from __future__ import annotations

import httpx

from sportly.client import SportlyClient


def _mock_espn(body: dict) -> SportlyClient:
    def handler(req: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json=body)
    c = SportlyClient()
    c._http = httpx.Client(transport=httpx.MockTransport(handler))
    return c


SCOREBOARD_BODY = {
    "events": [
        {"id": "401671827", "name": "Green Bay Packers at Philadelphia Eagles",
         "competitions": [{"competitors": [
             {"team": {"abbreviation": "PHI"}, "score": "34", "homeAway": "home"},
             {"team": {"abbreviation": "GB"},  "score": "29", "homeAway": "away"},
         ]}]}
    ]
}

TEAMS_BODY = {
    "sports": [{"leagues": [{"teams": [
        {"team": {"id": "12", "abbreviation": "KC", "displayName": "Kansas City Chiefs"}}
    ]}]}]
}

INJURIES_BODY = {
    "injuries": [
        {"team": {"abbreviation": "DAL"},
         "injuries": [{"athlete": {"fullName": "Micah Parsons"}, "status": "Questionable"}]}
    ]
}


class TestNFLModule:
    def test_constants(self):
        import sportly.nfl as nfl
        assert "KC" in nfl.TEAM_IDS
        assert nfl.TEAM_IDS["KC"] == 12
        assert callable(nfl.scoreboard)
        assert callable(nfl.qbr)
        assert callable(nfl.depth_chart)

    def test_scoreboard_returns_events(self):
        import sportly.nfl as nfl
        c = _mock_espn(SCOREBOARD_BODY)
        events = nfl.scoreboard(week=1, season=2024, client=c)
        assert events[0]["id"] == "401671827"

    def test_teams(self):
        import sportly.nfl as nfl
        c = _mock_espn(TEAMS_BODY)
        result = nfl.teams(client=c)
        # teams() delegates to espn endpoints which returns Team models or dicts
        assert result is not None

    def test_injuries_returns_list(self):
        import sportly.nfl as nfl
        c = _mock_espn(INJURIES_BODY)
        inj = nfl.injuries(client=c)
        assert isinstance(inj, list)

    def test_sport_league_constants(self):
        import sportly.nfl as nfl
        assert nfl.SPORT == "football"
        assert nfl.LEAGUE == "nfl"
