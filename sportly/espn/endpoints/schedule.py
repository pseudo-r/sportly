"""ESPN schedule/scoreboard endpoint functions."""

from __future__ import annotations

from datetime import datetime
from typing import Any

from sportly.client import SportlyClient, get_client
from sportly.espn._domains import ESPNDomain, build_url
from sportly.espn._parse import parse_game
from sportly.models import Game


def scoreboard(
    sport: str,
    league: str,
    *,
    date: str | datetime | None = None,
    limit: int = 100,
    domain: ESPNDomain = ESPNDomain.SITE,
    client: SportlyClient | None = None,
) -> list[Game]:
    """Return games for a given date (default: today).

    Parameters
    ----------
    sport:   ESPN sport slug.
    league:  League slug.
    date:    ``YYYYMMDD`` string or :class:`datetime`. Omit for today.
    limit:   Max events returned.
    domain:  ``ESPNDomain.SITE`` (default) or ``ESPNDomain.SITE_V3`` for enriched data.
    """
    http = client or get_client()
    url = build_url(domain, f"sports/{sport}/{league}/scoreboard")
    params: dict[str, Any] = {"limit": limit}
    if date:
        params["dates"] = date.strftime("%Y%m%d") if isinstance(date, datetime) else date
    data = http.get(url, params=params)
    return [parse_game(e) for e in data.get("events", [])]


def game(
    sport: str,
    league: str,
    game_id: str,
    *,
    domain: ESPNDomain = ESPNDomain.SITE,
    client: SportlyClient | None = None,
) -> Game:
    """Return the full summary for a single game.

    Parameters
    ----------
    sport:    ESPN sport slug.
    league:   League slug.
    game_id:  ESPN event ID.
    domain:   ``ESPNDomain.SITE`` (default) or ``ESPNDomain.SITE_V3``.
    """
    http = client or get_client()
    url = build_url(domain, f"sports/{sport}/{league}/summary")
    data = http.get(url, params={"event": game_id})
    return parse_game(data.get("header", {}))
