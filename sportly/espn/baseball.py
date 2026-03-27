"""sportly.espn.baseball — MLB, NCAA, WBC."""
from __future__ import annotations
from typing import Any
from sportly.client import SportlyClient
from sportly.espn._leagues import LEAGUES as _ALL_LEAGUES
from sportly.espn.endpoints import advanced as _advanced_ep
from sportly.espn.endpoints import athletes as _athletes_ep
from sportly.espn.endpoints import news as _news_ep
from sportly.espn.endpoints import schedule as _schedule_ep
from sportly.espn.endpoints import standings as _standings_ep
from sportly.espn.endpoints import teams as _teams_ep
from sportly.models import Article, Athlete, Game, Standings, Team

SPORT = "baseball"
DEFAULT_LEAGUE = "mlb"
LEAGUES: dict[str, str] = _ALL_LEAGUES[SPORT]

def teams(league: str = DEFAULT_LEAGUE, *, limit: int = 100, client: SportlyClient | None = None) -> list[Team]:
    return _teams_ep.all(SPORT, league, limit=limit, client=client)

def team(team_id: str, league: str = DEFAULT_LEAGUE, *, client: SportlyClient | None = None) -> Team:
    return _teams_ep.one(SPORT, league, team_id, client=client)

def roster(team_id: str, league: str = DEFAULT_LEAGUE, *, client: SportlyClient | None = None) -> list[Athlete]:
    return _teams_ep.roster(SPORT, league, team_id, client=client)

def scoreboard(league: str = DEFAULT_LEAGUE, *, date: str | None = None, limit: int = 100, client: SportlyClient | None = None) -> list[Game]:
    return _schedule_ep.scoreboard(SPORT, league, date=date, limit=limit, client=client)

def game(game_id: str, league: str = DEFAULT_LEAGUE, *, client: SportlyClient | None = None) -> Game:
    return _schedule_ep.game(SPORT, league, game_id, client=client)

def news(league: str = DEFAULT_LEAGUE, *, limit: int = 25, client: SportlyClient | None = None) -> list[Article]:
    return _news_ep.news(SPORT, league, limit=limit, client=client)

def standings(league: str = DEFAULT_LEAGUE, *, season: int | None = None, client: SportlyClient | None = None) -> Standings:
    return _standings_ep.standings(SPORT, league, season=season, client=client)

def injuries(league: str = DEFAULT_LEAGUE, *, client: SportlyClient | None = None) -> list[dict[str, Any]]:
    return _advanced_ep.injuries(SPORT, league, client=client)

def athlete(athlete_id: str | int, league: str = DEFAULT_LEAGUE, *, client: SportlyClient | None = None) -> Athlete:
    return _athletes_ep.athlete(SPORT, league, athlete_id, client=client)

def athlete_stats(athlete_id: str | int, league: str = DEFAULT_LEAGUE, *, client: SportlyClient | None = None) -> dict[str, Any]:
    return _athletes_ep.stats(SPORT, league, athlete_id, client=client)

def athlete_gamelog(athlete_id: str | int, league: str = DEFAULT_LEAGUE, *, client: SportlyClient | None = None) -> dict[str, Any]:
    return _athletes_ep.gamelog(SPORT, league, athlete_id, client=client)

def cdn_game(game_id: str, *, client: SportlyClient | None = None) -> dict[str, Any]:
    return _advanced_ep.cdn_game(SPORT, game_id, client=client)
