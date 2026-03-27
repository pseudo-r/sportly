"""Tests for the sportly CLI entry point."""

from __future__ import annotations

import argparse
import contextlib
import io

from sportly.cli import _build_parser


class TestCLIParserExisting:
    def test_info_subcommand(self):
        args = _build_parser().parse_args(["info"])
        assert args.command == "info"

    def test_espn_basketball_teams(self):
        args = _build_parser().parse_args(["espn", "basketball", "teams", "--league", "nba"])
        assert args.sport == "basketball"
        assert args.method == "teams"
        assert args.league == "nba"

    def test_espn_football_scoreboard(self):
        args = _build_parser().parse_args(["espn", "football", "scoreboard"])
        assert args.sport == "football"
        assert args.method == "scoreboard"

    def test_nhl_teams(self):
        args = _build_parser().parse_args(["nhl", "teams"])
        assert args.nhl_cmd == "teams"

    def test_nhl_schedule_with_date(self):
        args = _build_parser().parse_args(["nhl", "schedule", "--date", "2024-04-15"])
        assert args.date == "2024-04-15"

    def test_espn_game_with_id(self):
        args = _build_parser().parse_args(["espn", "basketball", "game", "--id", "401671803", "--league", "nba"])
        assert args.id == "401671803"


class TestCLIParserMLB:
    def test_schedule_no_date(self):
        args = _build_parser().parse_args(["mlb", "schedule"])
        assert args.mlb_cmd == "schedule"
        assert getattr(args, "date", None) is None

    def test_schedule_with_date(self):
        args = _build_parser().parse_args(["mlb", "schedule", "--date", "2025-04-01"])
        assert args.date == "2025-04-01"

    def test_teams(self):
        args = _build_parser().parse_args(["mlb", "teams"])
        assert args.mlb_cmd == "teams"

    def test_player_id(self):
        args = _build_parser().parse_args(["mlb", "player", "660271"])
        assert args.id == "660271"

    def test_leaders(self):
        args = _build_parser().parse_args(["mlb", "leaders", "homeRuns", "--season", "2025"])
        assert args.category == "homeRuns"
        assert args.season == 2025

    def test_standings(self):
        args = _build_parser().parse_args(["mlb", "standings"])
        assert args.mlb_cmd == "standings"

    def test_boxscore(self):
        args = _build_parser().parse_args(["mlb", "boxscore", "745444"])
        assert args.mlb_cmd == "boxscore"


class TestCLIParserNBA:
    def test_scoreboard(self):
        args = _build_parser().parse_args(["nba", "scoreboard", "2025-03-26"])
        assert args.nba_cmd == "scoreboard"
        assert args.date == "2025-03-26"

    def test_teams(self):
        assert _build_parser().parse_args(["nba", "teams"]).nba_cmd == "teams"

    def test_leaders(self):
        args = _build_parser().parse_args(["nba", "leaders", "PTS", "--season", "2024-25"])
        assert args.stat == "PTS"
        assert args.season == "2024-25"

    def test_career(self):
        args = _build_parser().parse_args(["nba", "career", "2544"])
        assert args.nba_cmd == "career"
        assert args.id == "2544"

    def test_standings(self):
        args = _build_parser().parse_args(["nba", "standings", "--season", "2024-25"])
        assert args.nba_cmd == "standings"

    def test_shot_chart(self):
        args = _build_parser().parse_args(["nba", "shot-chart", "201939", "--season", "2024-25"])
        assert args.nba_cmd == "shot-chart"


class TestCLIParserNFL:
    def test_scoreboard_week(self):
        args = _build_parser().parse_args(["nfl", "scoreboard", "--week", "1", "--season", "2024"])
        assert args.nfl_cmd == "scoreboard"
        assert args.week == 1
        assert args.season == 2024

    def test_teams(self):
        assert _build_parser().parse_args(["nfl", "teams"]).nfl_cmd == "teams"

    def test_injuries(self):
        assert _build_parser().parse_args(["nfl", "injuries"]).nfl_cmd == "injuries"

    def test_qbr(self):
        assert _build_parser().parse_args(["nfl", "qbr"]).nfl_cmd == "qbr"

    def test_depth_chart(self):
        args = _build_parser().parse_args(["nfl", "depth-chart", "6"])
        assert args.nfl_cmd == "depth-chart"
        assert args.id == "6"

    def test_news(self):
        assert _build_parser().parse_args(["nfl", "news"]).nfl_cmd == "news"


class TestCLIParserFotMob:
    def test_matches(self):
        args = _build_parser().parse_args(["fotmob", "matches", "20260326"])
        assert args.fm_cmd == "matches"
        assert args.date == "20260326"

    def test_league(self):
        args = _build_parser().parse_args(["fotmob", "league", "47"])
        assert args.id == 47

    def test_team(self):
        args = _build_parser().parse_args(["fotmob", "team", "8456"])
        assert args.id == 8456

    def test_search(self):
        args = _build_parser().parse_args(["fotmob", "search", "haaland"])
        assert args.term == "haaland"

    def test_leagues(self):
        assert _build_parser().parse_args(["fotmob", "leagues"]).fm_cmd == "leagues"


class TestCLIParserFantasy:
    def test_teams(self):
        args = _build_parser().parse_args(
            ["fantasy", "teams", "ffl", "--league-id", "336358", "--season", "2025"]
        )
        assert args.fs_cmd == "teams"
        assert args.game == "ffl"
        assert args.league_id == 336358
        assert args.season == 2025

    def test_draft(self):
        args = _build_parser().parse_args(
            ["fantasy", "draft", "fba", "--league-id", "999", "--season", "2025"]
        )
        assert args.fs_cmd == "draft"
        assert args.game == "fba"

    def test_meta(self):
        args = _build_parser().parse_args(["fantasy", "meta", "ffl"])
        assert args.fs_cmd == "meta"
        assert args.game == "ffl"

    def test_league_with_views(self):
        args = _build_parser().parse_args(
            ["fantasy", "league", "ffl", "--league-id", "123", "--season", "2025",
             "--views", "mTeam,mRoster"]
        )
        assert args.views == "mTeam,mRoster"

    def test_private_cookies(self):
        args = _build_parser().parse_args(
            ["fantasy", "teams", "ffl", "--league-id", "123", "--season", "2025",
             "--espn-s2", "AEB123", "--swid", "{ABC}"]
        )
        assert args.espn_s2 == "AEB123"
        assert args.swid == "{ABC}"


class TestCLIParserSofascore:
    def test_matches(self):
        args = _build_parser().parse_args(["sofascore", "matches", "football", "2026-03-26"])
        assert args.ss_cmd == "matches"
        assert args.sport == "football"
        assert args.date == "2026-03-26"

    def test_match(self):
        args = _build_parser().parse_args(["sofascore", "match", "11352523"])
        assert args.ss_cmd == "match"
        assert args.id == 11352523

    def test_player(self):
        args = _build_parser().parse_args(["sofascore", "player", "814123"])
        assert args.id == 814123

    def test_squad(self):
        args = _build_parser().parse_args(["sofascore", "squad", "4705"])
        assert args.ss_cmd == "squad"

    def test_team(self):
        args = _build_parser().parse_args(["sofascore", "team", "4705"])
        assert args.ss_cmd == "team"


# ── Handler smoke tests ───────────────────────────────────────────────────────

class TestCLIHandlers:
    def test_info_prints_version(self, capsys):
        from sportly.cli import _cmd_info
        _cmd_info(argparse.Namespace())
        out = capsys.readouterr().out
        assert "sportly" in out
        assert "1.1.0" in out
        assert "fotmob" in out.lower()

    def test_mlb_teams_handler(self, monkeypatch):
        import sportly.cli as cli
        import sportly.mlb as mlb
        monkeypatch.setattr(mlb, "teams", lambda: [{"id": 119, "name": "Dodgers"}])
        args = _build_parser().parse_args(["mlb", "teams"])
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            cli._cmd_mlb(args)
        assert "Dodgers" in out.getvalue()

    def test_mlb_standings_handler(self, monkeypatch):
        import sportly.cli as cli
        import sportly.mlb as mlb
        monkeypatch.setattr(mlb, "standings", lambda **_: {"records": []})
        args = _build_parser().parse_args(["mlb", "standings"])
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            cli._cmd_mlb(args)
        assert "records" in out.getvalue()

    def test_nfl_teams_handler(self, monkeypatch):
        import sportly.cli as cli
        import sportly.nfl as nfl
        monkeypatch.setattr(nfl, "teams", lambda _l=32: [{"id": 12, "name": "Chiefs"}])
        args = _build_parser().parse_args(["nfl", "teams"])
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            cli._cmd_nfl(args)
        assert "Chiefs" in out.getvalue()

    def test_nfl_injuries_handler(self, monkeypatch):
        import sportly.cli as cli
        import sportly.nfl as nfl
        monkeypatch.setattr(nfl, "injuries", lambda: [{"team": "DAL"}])
        args = _build_parser().parse_args(["nfl", "injuries"])
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            cli._cmd_nfl(args)
        assert "DAL" in out.getvalue()

    def test_fotmob_leagues_handler(self, capsys):
        from sportly.cli import _cmd_fotmob
        args = _build_parser().parse_args(["fotmob", "leagues"])
        _cmd_fotmob(args)
        out = capsys.readouterr().out
        assert "47" in out  # Premier League

    def test_nba_teams_handler(self, monkeypatch):
        import sportly.cli as cli
        import sportly.nba as nba
        monkeypatch.setattr(nba, "teams", lambda league_id="00": [{"id": "1610612747"}])
        args = _build_parser().parse_args(["nba", "teams"])
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            cli._cmd_nba(args)
        assert "1610612747" in out.getvalue()

    def test_fantasy_meta_handler(self, monkeypatch):
        import sportly.cli as cli
        import sportly.fantasy as fantasy
        monkeypatch.setattr(fantasy, "game_meta", lambda game, cookies=None: {"currentSeasonId": 2026})
        args = _build_parser().parse_args(["fantasy", "meta", "ffl"])
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            cli._cmd_fantasy(args)
        assert "2026" in out.getvalue()

    def test_fantasy_teams_handler(self, monkeypatch):
        import sportly.cli as cli
        import sportly.fantasy as fantasy
        monkeypatch.setattr(fantasy, "teams", lambda g, *, league_id, season, cookies=None: [{"id": 1}])
        args = _build_parser().parse_args(
            ["fantasy", "teams", "ffl", "--league-id", "123", "--season", "2025"]
        )
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            cli._cmd_fantasy(args)
        assert '"id": 1' in out.getvalue()

    def test_nfl_scoreboard_handler(self, monkeypatch):
        import sportly.cli as cli
        import sportly.nfl as nfl
        monkeypatch.setattr(nfl, "scoreboard", lambda week=None, season=None, season_type=None, date=None, limit=32: [])
        args = _build_parser().parse_args(["nfl", "scoreboard", "--week", "1"])
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            cli._cmd_nfl(args)
        assert "[]" in out.getvalue()
