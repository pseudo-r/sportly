"""Tests for the sportly CLI entry point."""

from __future__ import annotations

import sys

import pytest

from sportly.cli import _build_parser, main


class TestCLIParser:
    def test_info_subcommand(self):
        parser = _build_parser()
        args = parser.parse_args(["info"])
        assert args.command == "info"

    def test_espn_basketball_teams(self):
        parser = _build_parser()
        args = parser.parse_args(["espn", "basketball", "teams", "--league", "nba"])
        assert args.command == "espn"
        assert args.sport == "basketball"
        assert args.method == "teams"
        assert args.league == "nba"

    def test_espn_football_scoreboard(self):
        parser = _build_parser()
        args = parser.parse_args(["espn", "football", "scoreboard"])
        assert args.sport == "football"
        assert args.method == "scoreboard"

    def test_nhl_teams(self):
        parser = _build_parser()
        args = parser.parse_args(["nhl", "teams"])
        assert args.command == "nhl"
        assert args.nhl_cmd == "teams"

    def test_nhl_schedule_with_date(self):
        parser = _build_parser()
        args = parser.parse_args(["nhl", "schedule", "--date", "2024-04-15"])
        assert args.nhl_cmd == "schedule"
        assert args.date == "2024-04-15"

    def test_espn_game_with_id(self):
        parser = _build_parser()
        args = parser.parse_args(["espn", "basketball", "game", "--id", "401671803", "--league", "nba"])
        assert args.id == "401671803"
        assert args.league == "nba"
