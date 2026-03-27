"""sportly.nfl — NFL data via ESPN public APIs.

NFL's native api.nfl.com requires OAuth. All reliable, public NFL data
is served through ESPN's infrastructure (already used by sportly.espn).

Domains:
  - site.api.espn.com    → scoreboard, teams, rosters, injuries
  - sports.core.api.espn → events, athletes, play-by-play, odds
  - cdn.espn.com         → CDN game packages (drives, win probability)

Usage::

    from sportly import nfl

    sb  = nfl.scoreboard(week=1, season=2024)
    t   = nfl.teams()
    pbp = nfl.play_by_play("401671827")
    inj = nfl.injuries()
    dc  = nfl.depth_chart("6")           # Cowboys
    sched = nfl.team_schedule("12", season=2024)  # Chiefs

    print(nfl.TEAM_IDS)   # {"KC": 12, "PHI": 21, ...}
"""
from __future__ import annotations
from typing import Any
from sportly.client import SportlyClient, get_client
from sportly.espn._domains import ESPNDomain, build_url
from sportly.espn.endpoints import advanced as _advanced_ep
from sportly.espn.endpoints import athletes as _athletes_ep
from sportly.espn.endpoints import news as _news_ep
from sportly.espn.endpoints import schedule as _schedule_ep
from sportly.espn.endpoints import standings as _standings_ep
from sportly.espn.endpoints import teams as _teams_ep

# ── Constants ─────────────────────────────────────────────────────────────────
SPORT   = "football"
LEAGUE  = "nfl"

# ESPN NFL team IDs
TEAM_IDS: dict[str, int] = {
    "ARI": 22, "ATL": 1,  "BAL": 33, "BUF": 2,  "CAR": 29, "CHI": 3,
    "CIN": 4,  "CLE": 5,  "DAL": 6,  "DEN": 7,  "DET": 8,  "GB":  9,
    "HOU": 34, "IND": 11, "JAX": 30, "KC":  12, "LV":  13, "LAC": 24,
    "LAR": 14, "MIA": 15, "MIN": 16, "NE":  17, "NO":  18, "NYG": 19,
    "NYJ": 20, "PHI": 21, "PIT": 23, "SF":  25, "SEA": 26, "TB":  27,
    "TEN": 10, "WSH": 28,
}


# ── Schedule / Games ──────────────────────────────────────────────────────────

def scoreboard(
    *,
    week: int | None = None,
    season: int | None = None,
    season_type: int | None = None,
    date: str | None = None,
    limit: int = 32,
    client: SportlyClient | None = None,
) -> list[dict[str, Any]]:
    """Return NFL scoreboard.

    Parameters
    ----------
    week:        NFL week number (1-18).
    season:      Season year (e.g. ``2024``).
    season_type: ``1``=pre, ``2``=regular (default), ``3``=post.
    date:        Single date in ``YYYYMMDD`` format.
    """
    http = client or get_client()
    qp: dict[str, Any] = {k: v for k, v in {
        "week": week, "seasontype": season_type,
        "season": season, "dates": date, "limit": limit,
    }.items() if v is not None}
    path = f"sports/{SPORT}/leagues/{LEAGUE}/scoreboard"
    data = http.get(build_url(ESPNDomain.SITE, path), params=qp)
    return data.get("events", [])  # type: ignore[return-value]


def game(game_id: str, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """Return full game summary (boxscore + drives + scoring plays)."""
    return _schedule_ep.game(SPORT, LEAGUE, game_id, client=client)


def cdn_game(game_id: str, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """Return CDN game package (drives, win probability, odds)."""
    return _advanced_ep.cdn_game(SPORT, game_id, client=client)


# ── Teams ─────────────────────────────────────────────────────────────────────

def teams(*, limit: int = 32, client: SportlyClient | None = None) -> list[Any]:
    """Return all 32 NFL teams."""
    return _teams_ep.all(SPORT, LEAGUE, limit=limit, client=client)


def team(team_id: str | int, *, client: SportlyClient | None = None) -> Any:
    """Return a single NFL team by ESPN ID (see ``nfl.TEAM_IDS``)."""
    return _teams_ep.one(SPORT, LEAGUE, str(team_id), client=client)


def roster(team_id: str | int, *, client: SportlyClient | None = None) -> list[Any]:
    """Return a team's current roster."""
    return _teams_ep.roster(SPORT, LEAGUE, str(team_id), client=client)


def team_schedule(
    team_id: str | int,
    *,
    season: int | None = None,
    season_type: int | None = None,
    client: SportlyClient | None = None,
) -> dict[str, Any]:
    """Return full season schedule for a team."""
    http = client or get_client()
    qp = {k: v for k, v in {"season": season, "seasontype": season_type}.items() if v is not None}
    path = f"sports/{SPORT}/leagues/{LEAGUE}/teams/{team_id}/schedule"
    return http.get(build_url(ESPNDomain.SITE, path), params=qp)  # type: ignore[return-value]


def depth_chart(team_id: str | int, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """Return depth chart for a team."""
    http = client or get_client()
    path = f"sports/{SPORT}/leagues/{LEAGUE}/teams/{team_id}/depthcharts"
    return http.get(build_url(ESPNDomain.SITE, path))  # type: ignore[return-value]


# ── Players / Athletes ────────────────────────────────────────────────────────

def athlete(athlete_id: str | int, *, client: SportlyClient | None = None) -> Any:
    """Return a player profile by ESPN athlete ID."""
    return _athletes_ep.athlete(SPORT, LEAGUE, athlete_id, client=client)


def athlete_stats(athlete_id: str | int, *, season: int | None = None, client: SportlyClient | None = None) -> dict[str, Any]:
    """Return season stats for a player."""
    return _athletes_ep.stats(SPORT, LEAGUE, athlete_id, client=client)


def athlete_gamelog(athlete_id: str | int, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """Return game-by-game log for a player."""
    return _athletes_ep.gamelog(SPORT, LEAGUE, athlete_id, client=client)


def athlete_news(athlete_id: str | int, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """Return news articles for a player."""
    http = client or get_client()
    path = f"sports/{SPORT}/leagues/{LEAGUE}/athletes/{athlete_id}/news"
    return http.get(build_url(ESPNDomain.SITE, path))  # type: ignore[return-value]


# ── League-wide ───────────────────────────────────────────────────────────────

def standings(*, season: int | None = None, client: SportlyClient | None = None) -> Any:
    """Return NFL standings."""
    return _standings_ep.standings(SPORT, LEAGUE, season=season, client=client)


def injuries(*, client: SportlyClient | None = None) -> list[dict[str, Any]]:
    """Return league-wide injury report."""
    return _advanced_ep.injuries(SPORT, LEAGUE, client=client)


def transactions(*, client: SportlyClient | None = None) -> list[dict[str, Any]]:
    """Return recent transactions."""
    return _advanced_ep.transactions(SPORT, LEAGUE, client=client)


def news(*, limit: int = 25, client: SportlyClient | None = None) -> list[Any]:
    """Return NFL news."""
    return _news_ep.news(SPORT, LEAGUE, limit=limit, client=client)


def play_by_play(event_id: str, *, limit: int = 300, client: SportlyClient | None = None) -> dict[str, Any]:
    """Return play-by-play (max 300 plays per page) for a game."""
    return _advanced_ep.play_by_play(SPORT, LEAGUE, event_id, limit=limit, client=client)


def odds(event_id: str, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """Return betting odds for a game."""
    return _advanced_ep.odds(SPORT, LEAGUE, event_id, client=client)


def qbr(
    *,
    season: int | None = None,
    season_type: int = 2,
    week: int | None = None,
    client: SportlyClient | None = None,
) -> dict[str, Any]:
    """Return ESPN Quarterback Rating (QBR).

    Parameters
    ----------
    season_type: ``2``=regular (default), ``1``=pre, ``3``=post.
    week:        Filter to a specific week.
    """
    http = client or get_client()
    year = season or "current"
    base = f"sports/{SPORT}/leagues/{LEAGUE}/seasons/{year}/types/{season_type}"
    path = f"{base}/weeks/{week}/qbr/0" if week else f"{base}/groups/1/qbr/0"
    return http.get(build_url(ESPNDomain.CORE, path))  # type: ignore[return-value]
