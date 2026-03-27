"""nfl.endpoints.league — league-wide standings, injuries, transactions, news, QBR."""
from __future__ import annotations
from typing import Any
from sportly.client import SportlyClient, get_client
from sportly.espn._domains import ESPNDomain, build_url
from sportly.espn.endpoints import advanced as _adv
from sportly.espn.endpoints import news as _news_ep
from sportly.espn.endpoints import standings as _standings

SPORT  = "football"
LEAGUE = "nfl"


def standings(*, season: int | None = None, client: SportlyClient | None = None) -> Any:
    """NFL standings."""
    return _standings.standings(SPORT, LEAGUE, season=season, client=client)


def injuries(*, client: SportlyClient | None = None) -> list[dict[str, Any]]:
    """League-wide injury report."""
    return _adv.injuries(SPORT, LEAGUE, client=client)


def transactions(*, client: SportlyClient | None = None) -> list[dict[str, Any]]:
    """Recent transactions (signings, releases, trades)."""
    return _adv.transactions(SPORT, LEAGUE, client=client)


def news(*, limit: int = 25, client: SportlyClient | None = None) -> list[Any]:
    """NFL news feed."""
    return _news_ep.news(SPORT, LEAGUE, limit=limit, client=client)


def qbr(
    *,
    season: int | None = None,
    season_type: int = 2,
    week: int | None = None,
    client: SportlyClient | None = None,
) -> dict[str, Any]:
    """ESPN Quarterback Rating (QBR).

    Parameters
    ----------
    season_type: ``2`` = regular (default), ``1`` = pre, ``3`` = post.
    week:        Specific week filter.
    """
    http = client or get_client()
    year = season or "current"
    base = f"sports/{SPORT}/leagues/{LEAGUE}/seasons/{year}/types/{season_type}"
    path = f"{base}/weeks/{week}/qbr/0" if week else f"{base}/groups/1/qbr/0"
    return http.get(build_url(ESPNDomain.CORE, path))  # type: ignore[return-value]
