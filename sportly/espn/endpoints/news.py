"""ESPN news endpoint functions."""

from __future__ import annotations

from sportly.client import SportlyClient, get_client
from sportly.espn._domains import ESPNDomain, build_url
from sportly.espn._parse import parse_article
from sportly.models import Article


def news(
    sport: str,
    league: str,
    *,
    limit: int = 25,
    client: SportlyClient | None = None,
) -> list[Article]:
    """Return latest news articles for a league (site API)."""
    http = client or get_client()
    url = build_url(ESPNDomain.SITE, f"sports/{sport}/{league}/news")
    data = http.get(url, params={"limit": limit})
    return [a for raw in data.get("articles", []) if (a := parse_article(raw))]


def now_news(
    sport: str,
    *,
    league: str | None = None,
    limit: int = 25,
    client: SportlyClient | None = None,
) -> list[Article]:
    """Return real-time headlines from now.core.api.espn.com."""
    http = client or get_client()
    url = build_url(ESPNDomain.NOW, "/sports/news")
    params: dict = {"sport": sport, "limit": limit}
    if league:
        params["leagues"] = league
    data = http.get(url, params=params)
    headlines = data.get("headlines", data.get("articles", []))
    return [a for raw in headlines if (a := parse_article(raw))]
