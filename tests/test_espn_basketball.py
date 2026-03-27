"""Tests for sportly.espn.basketball (mocked — no network required)."""

from __future__ import annotations

import pytest

from sportly.espn import basketball
from sportly.models import Article, Game, Standings, Team


class TestTeams:
    def test_returns_list_of_team_objects(self, mock_client, nba_teams_payload):
        mock_client.register("/teams", nba_teams_payload)
        teams = basketball.teams("nba")
        assert isinstance(teams, list)
        assert len(teams) == 2
        assert all(isinstance(t, Team) for t in teams)

    def test_lakers_fields(self, mock_client, nba_teams_payload):
        mock_client.register("/teams", nba_teams_payload)
        teams = basketball.teams("nba")
        lakers = next(t for t in teams if t.abbr == "LAL")
        assert lakers.id == "13"
        assert lakers.name == "Los Angeles Lakers"
        assert lakers.nickname == "Lakers"
        assert lakers.color == "552583"
        assert len(lakers.logos) == 1

    def test_default_league_is_nba(self, mock_client, nba_teams_payload):
        mock_client.register("/teams", nba_teams_payload)
        teams = basketball.teams()  # no league arg
        assert len(teams) == 2


class TestScoreboard:
    def test_returns_list_of_game_objects(self, mock_client, nba_scoreboard_payload):
        mock_client.register("/scoreboard", nba_scoreboard_payload)
        games = basketball.scoreboard("nba")
        assert isinstance(games, list)
        assert len(games) == 1
        assert all(isinstance(g, Game) for g in games)

    def test_game_fields(self, mock_client, nba_scoreboard_payload):
        mock_client.register("/scoreboard", nba_scoreboard_payload)
        games = basketball.scoreboard("nba")
        g = games[0]
        assert g.id == "401671803"
        assert g.name == "Los Angeles Lakers vs Boston Celtics"
        assert g.status.state == "post"
        assert g.status.completed is True
        assert g.status.detail == "Final"
        assert len(g.competitors) == 2

    def test_competitors_parsed(self, mock_client, nba_scoreboard_payload):
        mock_client.register("/scoreboard", nba_scoreboard_payload)
        games = basketball.scoreboard("nba")
        home = next(c for c in games[0].competitors if c.home_away == "home")
        assert home.score == "110"
        assert home.winner is True
        assert home.team is not None
        assert home.team.abbr == "LAL"


class TestNews:
    def test_returns_list_of_articles(self, mock_client, nba_news_payload):
        mock_client.register("/news", nba_news_payload)
        articles = basketball.news("nba")
        assert isinstance(articles, list)
        assert len(articles) == 1
        assert all(isinstance(a, Article) for a in articles)

    def test_article_fields(self, mock_client, nba_news_payload):
        mock_client.register("/news", nba_news_payload)
        articles = basketball.news("nba")
        a = articles[0]
        assert a.headline == "LeBron James scores 30 points"
        assert a.description == "Lakers defeat Celtics on Christmas Day."
        assert a.published is not None
        assert a.thumbnail is not None


class TestStandings:
    def test_returns_standings_object(self, mock_client, epl_standings_payload):
        mock_client.register("/standings", epl_standings_payload)
        table = basketball.standings("nba")
        assert isinstance(table, Standings)
        assert len(table.entries) == 1

    def test_entry_fields(self, mock_client, epl_standings_payload):
        mock_client.register("/standings", epl_standings_payload)
        table = basketball.standings("nba")
        entry = table.entries[0]
        assert entry.wins == 20
        assert entry.losses == 3
        assert entry.team is not None
        assert entry.team.abbr == "MCI"
