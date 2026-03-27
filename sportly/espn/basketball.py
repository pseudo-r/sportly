"""sportly.espn.basketball — NBA, WNBA, college, and international basketball.

Usage::

    from sportly.espn import basketball

    # All NBA teams
    teams = basketball.teams()                        # default league: nba

    # WNBA scoreboard
    games = basketball.scoreboard("wnba")

    # Specific date
    games = basketball.scoreboard("nba", date="20241225")

    # v3 enriched scoreboard
    from sportly.espn._domains import ESPNDomain
    games = basketball.scoreboard("nba", domain=ESPNDomain.SITE_V3)

    # Lakers roster
    roster = basketball.roster("13")                  # team_id 13 = Lakers

    # LeBron stats
    overview = basketball.athlete_overview("1966")    # id 1966 = LeBron

    # NCAA Bracketology
    bracket = basketball.bracketology()

    # NBA BPI power index
    bpi = basketball.power_index("nba")
"""

from __future__ import annotations

from typing import Any

from sportly.client import SportlyClient, get_client
from sportly.espn._domains import ESPNDomain, build_url
from sportly.espn._leagues import LEAGUES as _ALL_LEAGUES
from sportly.espn.endpoints import athletes as _athletes_ep
from sportly.espn.endpoints import advanced as _advanced_ep
from sportly.espn.endpoints import news as _news_ep
from sportly.espn.endpoints import schedule as _schedule_ep
from sportly.espn.endpoints import standings as _standings_ep
from sportly.espn.endpoints import teams as _teams_ep
from sportly.models import Article, Athlete, Game, Standings, Team

SPORT = "basketball"
DEFAULT_LEAGUE = "nba"

#: All known ESPN basketball leagues. Keys are valid league slugs.
LEAGUES: dict[str, str] = _ALL_LEAGUES[SPORT]


# ── Common methods ─────────────────────────────────────────────────────────────

def teams(league: str = DEFAULT_LEAGUE, *, limit: int = 100, client: SportlyClient | None = None) -> list[Team]:
    """Return all teams. Defaults to NBA."""
    return _teams_ep.all(SPORT, league, limit=limit, client=client)


def team(team_id: str, league: str = DEFAULT_LEAGUE, *, client: SportlyClient | None = None) -> Team:
    """Return a single team by ESPN team ID (e.g. ``"13"`` = Lakers)."""
    return _teams_ep.one(SPORT, league, team_id, client=client)


def roster(team_id: str, league: str = DEFAULT_LEAGUE, *, client: SportlyClient | None = None) -> list[Athlete]:
    """Return the roster for a team."""
    return _teams_ep.roster(SPORT, league, team_id, client=client)


def scoreboard(
    league: str = DEFAULT_LEAGUE,
    *,
    date: str | None = None,
    limit: int = 100,
    domain: ESPNDomain = ESPNDomain.SITE,
    client: SportlyClient | None = None,
) -> list[Game]:
    """Return games. Pass ``domain=ESPNDomain.SITE_V3`` for enriched data."""
    return _schedule_ep.scoreboard(SPORT, league, date=date, limit=limit, domain=domain, client=client)


def game(game_id: str, league: str = DEFAULT_LEAGUE, *, client: SportlyClient | None = None) -> Game:
    """Return full game summary."""
    return _schedule_ep.game(SPORT, league, game_id, client=client)


def news(league: str = DEFAULT_LEAGUE, *, limit: int = 25, client: SportlyClient | None = None) -> list[Article]:
    """Return latest news articles."""
    return _news_ep.news(SPORT, league, limit=limit, client=client)


def now_news(*, league: str | None = None, limit: int = 25, client: SportlyClient | None = None) -> list[Article]:
    """Real-time headlines from now.core.api.espn.com."""
    return _news_ep.now_news(SPORT, league=league, limit=limit, client=client)


def standings(league: str = DEFAULT_LEAGUE, *, season: int | None = None, client: SportlyClient | None = None) -> Standings:
    """Return league standings (uses /apis/v2/ — site/v2 returns a stub)."""
    return _standings_ep.standings(SPORT, league, season=season, client=client)


def rankings(league: str = DEFAULT_LEAGUE, *, client: SportlyClient | None = None) -> list[dict[str, Any]]:
    """Return poll rankings (NCAA leagues only)."""
    return _standings_ep.rankings(SPORT, league, client=client)


def injuries(league: str = DEFAULT_LEAGUE, *, client: SportlyClient | None = None) -> list[dict[str, Any]]:
    """Return league-wide injury report."""
    return _advanced_ep.injuries(SPORT, league, client=client)


def transactions(league: str = DEFAULT_LEAGUE, *, client: SportlyClient | None = None) -> list[dict[str, Any]]:
    """Return recent signings, trades, and waivers."""
    return _advanced_ep.transactions(SPORT, league, client=client)


def athlete(athlete_id: str | int, league: str = DEFAULT_LEAGUE, *, client: SportlyClient | None = None) -> Athlete:
    """Return athlete profile from the core API."""
    return _athletes_ep.athlete(SPORT, league, athlete_id, client=client)


def athlete_overview(athlete_id: str | int, league: str = DEFAULT_LEAGUE, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """Stats snapshot + next game + news (web/v3)."""
    return _athletes_ep.overview(SPORT, league, athlete_id, client=client)


def athlete_stats(athlete_id: str | int, league: str = DEFAULT_LEAGUE, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """Season statistics (web/v3)."""
    return _athletes_ep.stats(SPORT, league, athlete_id, client=client)


def athlete_gamelog(athlete_id: str | int, league: str = DEFAULT_LEAGUE, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """Game-by-game log (web/v3)."""
    return _athletes_ep.gamelog(SPORT, league, athlete_id, client=client)


def athlete_splits(athlete_id: str | int, league: str = DEFAULT_LEAGUE, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """Home/away/opponent splits (web/v3)."""
    return _athletes_ep.splits(SPORT, league, athlete_id, client=client)


def leaders(league: str = DEFAULT_LEAGUE, *, season: int | None = None, client: SportlyClient | None = None) -> dict[str, Any]:
    """Statistical leaders (core API)."""
    return _athletes_ep.leaders(SPORT, league, season=season, client=client)


def odds(event_id: str, competition_id: str | None = None, league: str = DEFAULT_LEAGUE, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """Betting odds for a game."""
    return _advanced_ep.odds(SPORT, league, event_id, competition_id, client=client)


def play_by_play(event_id: str, competition_id: str | None = None, league: str = DEFAULT_LEAGUE, *, limit: int = 300, client: SportlyClient | None = None) -> dict[str, Any]:
    """Play-by-play for a game."""
    return _advanced_ep.play_by_play(SPORT, league, event_id, competition_id, limit=limit, client=client)


def cdn_game(game_id: str, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """Full CDN game package (drives, plays, odds, win probability)."""
    return _advanced_ep.cdn_game(SPORT, game_id, client=client)


# ── Basketball-specific ───────────────────────────────────────────────────────

def bracketology(tournament_id: str = "22", *, year: int | None = None, client: SportlyClient | None = None) -> dict[str, Any]:
    """NCAA Tournament bracket projections.

    Parameters
    ----------
    tournament_id: ``"22"`` = NCAA Men's, ``"23"`` = NCAA Women's.
    year: Tournament year. Omit for current.

    Example
    -------
    ::

        bracket = basketball.bracketology()              # Men's current
        womens  = basketball.bracketology("23")          # Women's
    """
    http = client or get_client()
    path = f"tournament/{tournament_id}/seasons/{year}/bracketology" if year else f"tournament/{tournament_id}/bracketology"
    url = build_url(ESPNDomain.CORE, path)
    return http.get(url)  # type: ignore[return-value]


def power_index(league: str = DEFAULT_LEAGUE, *, season: int | None = None, client: SportlyClient | None = None) -> dict[str, Any]:
    """ESPN BPI (Basketball Power Index) ratings.

    Example
    -------
    ::

        bpi = basketball.power_index("mens-college-basketball")
    """
    http = client or get_client()
    base = f"sports/{SPORT}/leagues/{league}"
    path = f"{base}/seasons/{season}/powerindex" if season else f"{base}/powerindex"
    url = build_url(ESPNDomain.CORE, path)
    return http.get(url)  # type: ignore[return-value]
