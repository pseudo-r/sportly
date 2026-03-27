"""nfl.endpoints.games — scoreboard, game summaries, play-by-play, CDN packages."""
from __future__ import annotations

from typing import Any

from sportly.client import SportlyClient, get_client
from sportly.espn._domains import ESPNDomain, build_url
from sportly.espn.endpoints import advanced as _adv
from sportly.espn.endpoints import schedule as _sched

SPORT  = "football"
LEAGUE = "nfl"


def scoreboard(
    *,
    week: int | None = None,
    season: int | None = None,
    season_type: int | None = None,
    date: str | None = None,
    limit: int = 32,
    client: SportlyClient | None = None,
) -> list[dict[str, Any]]:
    """NFL scoreboard filtered by week, season, or date."""
    http = client or get_client()
    qp: dict[str, Any] = {k: v for k, v in {
        "week": week, "seasontype": season_type,
        "season": season, "dates": date, "limit": limit,
    }.items() if v is not None}
    path = f"sports/{SPORT}/leagues/{LEAGUE}/scoreboard"
    data = http.get(build_url(ESPNDomain.SITE, path), params=qp)
    return data.get("events", [])  # type: ignore[return-value]


def game(game_id: str, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """Full game summary (boxscore, drives, scoring plays)."""
    return _sched.game(SPORT, LEAGUE, game_id, client=client)


def cdn_game(game_id: str, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """CDN game package (drives, win probability, odds)."""
    return _adv.cdn_game(SPORT, game_id, client=client)


def play_by_play(event_id: str, *, limit: int = 300, client: SportlyClient | None = None) -> dict[str, Any]:
    """Play-by-play (max 300 plays per page) for a game."""
    return _adv.play_by_play(SPORT, LEAGUE, event_id, limit=limit, client=client)


def odds(event_id: str, *, client: SportlyClient | None = None) -> dict[str, Any]:
    """Betting odds for a game."""
    return _adv.odds(SPORT, LEAGUE, event_id, client=client)
