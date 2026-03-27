"""ESPN advanced endpoint functions — injuries, odds, play-by-play, CDN."""

from __future__ import annotations

from typing import Any

from sportly.client import SportlyClient, get_client
from sportly.espn._domains import ESPNDomain, build_url


def injuries(
    sport: str,
    league: str,
    *,
    client: SportlyClient | None = None,
) -> list[dict[str, Any]]:
    """League-wide injury report."""
    http = client or get_client()
    url = build_url(ESPNDomain.SITE, f"sports/{sport}/{league}/injuries")
    data = http.get(url)
    return data.get("items", data.get("injuries", []))  # type: ignore[return-value]


def transactions(
    sport: str,
    league: str,
    *,
    client: SportlyClient | None = None,
) -> list[dict[str, Any]]:
    """Recent signings, trades, and waivers."""
    http = client or get_client()
    url = build_url(ESPNDomain.SITE, f"sports/{sport}/{league}/transactions")
    data = http.get(url)
    return data.get("items", data.get("transactions", []))  # type: ignore[return-value]


def odds(
    sport: str,
    league: str,
    event_id: str,
    competition_id: str | None = None,
    *,
    client: SportlyClient | None = None,
) -> dict[str, Any]:
    """Betting odds for a game from the core API.

    Includes lines from Caesars (38), FanDuel (37), DraftKings (41), BetMGM (58).
    """
    http = client or get_client()
    comp = competition_id or event_id
    url = build_url(
        ESPNDomain.CORE,
        f"sports/{sport}/leagues/{league}/events/{event_id}/competitions/{comp}/odds",
    )
    return http.get(url)  # type: ignore[return-value]


def play_by_play(
    sport: str,
    league: str,
    event_id: str,
    competition_id: str | None = None,
    *,
    limit: int = 300,
    client: SportlyClient | None = None,
) -> dict[str, Any]:
    """Play-by-play data for a game from the core API."""
    http = client or get_client()
    comp = competition_id or event_id
    url = build_url(
        ESPNDomain.CORE,
        f"sports/{sport}/leagues/{league}/events/{event_id}/competitions/{comp}/plays",
    )
    return http.get(url, params={"limit": limit})  # type: ignore[return-value]


def win_probability(
    sport: str,
    league: str,
    event_id: str,
    competition_id: str | None = None,
    *,
    client: SportlyClient | None = None,
) -> dict[str, Any]:
    """In-game win probability data from the core API."""
    http = client or get_client()
    comp = competition_id or event_id
    url = build_url(
        ESPNDomain.CORE,
        f"sports/{sport}/leagues/{league}/events/{event_id}/competitions/{comp}/probabilities",
    )
    return http.get(url)  # type: ignore[return-value]


def cdn_game(
    sport: str,
    game_id: str,
    *,
    client: SportlyClient | None = None,
) -> dict[str, Any]:
    """Full CDN game package (drives, plays, win prob, odds, boxscore).

    Result key ``gamepackageJSON`` contains the richest available game data.
    """
    http = client or get_client()
    url = build_url(ESPNDomain.CDN, f"{sport}/game")
    return http.get(url, params={"xhr": "1", "gameId": game_id})  # type: ignore[return-value]
