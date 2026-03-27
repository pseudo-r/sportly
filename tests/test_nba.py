"""Tests for sportly.nba — all mocked, no network."""
from __future__ import annotations

import httpx

from sportly.nba._client import NBAClient, parse_result_sets

# ── Helpers ───────────────────────────────────────────────────────────────────

def _mock(status: int, body: dict) -> NBAClient:
    def handler(req: httpx.Request) -> httpx.Response:
        return httpx.Response(status, json=body)
    c = NBAClient()
    c._http = httpx.Client(transport=httpx.MockTransport(handler))
    return c

def _rs(name: str, headers: list, rows: list) -> dict:
    """Build a minimal NBA resultSets response."""
    return {"resultSets": [{"name": name, "headers": headers, "rowSet": rows}]}

# ── parse_result_sets ─────────────────────────────────────────────────────────

class TestParseResultSets:
    def test_converts_rows_to_dicts(self):
        raw = _rs("PlayerStats", ["PLAYER_ID", "PTS", "AST"], [["2544", 25.7, 8.3]])
        result = parse_result_sets(raw)
        assert result["PlayerStats"][0] == {"PLAYER_ID": "2544", "PTS": 25.7, "AST": 8.3}

    def test_empty_rowset(self):
        raw = _rs("Empty", ["A", "B"], [])
        result = parse_result_sets(raw)
        assert result["Empty"] == []

    def test_multiple_result_sets(self):
        raw = {"resultSets": [
            {"name": "A", "headers": ["X"], "rowSet": [[1]]},
            {"name": "B", "headers": ["Y"], "rowSet": [[2]]},
        ]}
        out = parse_result_sets(raw)
        assert out["A"][0]["X"] == 1
        assert out["B"][0]["Y"] == 2

# ── Games ─────────────────────────────────────────────────────────────────────

class TestNBAGames:
    def test_scoreboard_parses_result_sets(self):
        from sportly.nba.endpoints import games
        body = _rs("GameHeader",
            ["GAME_ID", "GAME_STATUS_TEXT", "HOME_TEAM_ID", "VISITOR_TEAM_ID"],
            [["0022401045", "Final", "1610612747", "1610612738"]]
        )
        c = _mock(200, body)
        sb = games.scoreboard("2025-03-26", client=c)
        assert sb["GameHeader"][0]["GAME_ID"] == "0022401045"
        assert sb["GameHeader"][0]["GAME_STATUS_TEXT"] == "Final"

    def test_play_by_play(self):
        from sportly.nba.endpoints import games
        body = {"game": {"actions": [
            {"actionNumber": 1, "actionType": "Made Shot", "description": "LeBron layup"},
        ]}}
        c = _mock(200, body)
        pbp = games.play_by_play("0022401045", client=c)
        assert pbp[0]["actionType"] == "Made Shot"

# ── Players ───────────────────────────────────────────────────────────────────

class TestNBAPlayers:
    def test_career_stats(self):
        from sportly.nba.endpoints import players
        body = _rs("SeasonTotalsRegularSeason",
            ["PLAYER_ID", "SEASON_ID", "PTS"],
            [["2544", "2023-24", 25.7]]
        )
        c = _mock(200, body)
        stats = players.career_stats("2544", client=c)
        assert stats["SeasonTotalsRegularSeason"][0]["PTS"] == 25.7

    def test_game_log(self):
        from sportly.nba.endpoints import players
        body = _rs("PlayerGameLog",
            ["GAME_DATE", "MATCHUP", "PTS"],
            [["2025-03-20", "vs. BOS", 32]]
        )
        c = _mock(200, body)
        log = players.game_log("2544", "2024-25", client=c)
        assert log[0]["PTS"] == 32

    def test_shot_chart(self):
        from sportly.nba.endpoints import players
        body = _rs("Shot_Chart_Detail",
            ["SHOT_MADE_FLAG", "LOC_X", "LOC_Y"],
            [[1, -52, 23], [0, 142, 80]]
        )
        c = _mock(200, body)
        shots = players.shot_chart("201939", "2024-25", client=c)
        makes = [s for s in shots if s["SHOT_MADE_FLAG"] == 1]
        assert len(makes) == 1

    def test_player_info(self):
        from sportly.nba.endpoints import players
        body = _rs("CommonPlayerInfo",
            ["PERSON_ID", "DISPLAY_FIRST_LAST", "TEAM_NAME"],
            [[2544, "LeBron James", "Los Angeles Lakers"]]
        )
        c = _mock(200, body)
        p = players.info(2544, client=c)
        assert p["DISPLAY_FIRST_LAST"] == "LeBron James"

# ── League ────────────────────────────────────────────────────────────────────

class TestNBALeague:
    def test_standings(self):
        from sportly.nba.endpoints import league
        body = _rs("Standings",
            ["TeamName", "WINS", "LOSSES"],
            [["Boston Celtics", 64, 18]]
        )
        c = _mock(200, body)
        rows = league.standings("2024-25", client=c)
        assert rows[0]["TeamName"] == "Boston Celtics"
        assert rows[0]["WINS"] == 64

    def test_leaders(self):
        from sportly.nba.endpoints import league
        body = _rs("LeagueLeaders",
            ["PLAYER_ID", "PLAYER", "PTS"],
            [[1641705, "Victor Wembanyama", 24.4]]
        )
        c = _mock(200, body)
        rows = league.leaders("PTS", client=c)
        assert rows[0]["PLAYER"] == "Victor Wembanyama"

# ── Module-level API ──────────────────────────────────────────────────────────

class TestNBAModule:
    def test_imports_and_constants(self):
        import sportly.nba as nba
        assert callable(nba.scoreboard)
        assert callable(nba.leaders)
        assert callable(nba.shot_chart)
        assert "LAL" in nba.TEAM_IDS
        assert "LeBron James" in nba.PLAYER_IDS

    def test_module_standings(self):
        import sportly.nba as nba
        body = _rs("Standings", ["TeamName", "WINS", "LOSSES"], [["Celtics", 64, 18]])
        c = _mock(200, body)
        rows = nba.standings("2024-25", client=c)
        assert rows[0]["WINS"] == 64
