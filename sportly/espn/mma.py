"""sportly.espn.mma — Bellator, LFA, Cage Warriors, and 25+ promotions."""
from __future__ import annotations
from sportly.client import SportlyClient
from sportly.espn._leagues import LEAGUES as _ALL_LEAGUES
from sportly.espn.endpoints import news as _news_ep
from sportly.espn.endpoints import schedule as _schedule_ep
from sportly.models import Article, Game

SPORT = "mma"
DEFAULT_LEAGUE = "bellator"
LEAGUES: dict[str, str] = _ALL_LEAGUES[SPORT]

def scoreboard(league: str = DEFAULT_LEAGUE, *, date: str | None = None, client: SportlyClient | None = None) -> list[Game]:
    return _schedule_ep.scoreboard(SPORT, league, date=date, client=client)

def game(game_id: str, league: str = DEFAULT_LEAGUE, *, client: SportlyClient | None = None) -> Game:
    return _schedule_ep.game(SPORT, league, game_id, client=client)

def news(league: str = DEFAULT_LEAGUE, *, limit: int = 25, client: SportlyClient | None = None) -> list[Article]:
    return _news_ep.news(SPORT, league, limit=limit, client=client)
