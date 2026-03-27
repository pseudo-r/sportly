"""ESPN API domain/version enum and URL constants."""

from enum import Enum


class ESPNDomain(str, Enum):
    """ESPN API domain selector.

    Pass to any endpoint function via ``domain=ESPNDomain.CDN``.

    Examples
    --------
    ::

        from sportly.espn import basketball
        from sportly.espn._domains import ESPNDomain

        # Default (site v2)
        games = basketball.scoreboard("nba")

        # Explicit CDN game package
        pkg = basketball.cdn_game("401671803")

        # Explicit v3 scoreboard
        games_v3 = basketball.scoreboard("nba", domain=ESPNDomain.SITE_V3)
    """

    SITE    = "site"      # site.api.espn.com/apis/site/v2/   — scores, teams, news
    SITE_V2 = "site_v2"  # site.api.espn.com/apis/v2/         — standings only
    SITE_V3 = "site_v3"  # site.api.espn.com/apis/site/v3/    — enriched scoreboard
    CORE    = "core"      # sports.core.api.espn.com/v2/       — athletes, odds, plays
    CORE_V3 = "core_v3"  # sports.core.api.espn.com/v3/       — enriched athletes
    WEB_V3  = "web_v3"   # site.web.api.espn.com/apis/common/v3/ — gamelog, splits
    CDN     = "cdn"       # cdn.espn.com/core/                 — full game packages
    NOW     = "now"       # now.core.api.espn.com/v1/          — real-time news


# Base URLs for each domain
DOMAIN_BASES: dict[ESPNDomain, str] = {
    ESPNDomain.SITE:    "https://site.api.espn.com/apis/site/v2",
    ESPNDomain.SITE_V2: "https://site.api.espn.com/apis/v2",
    ESPNDomain.SITE_V3: "https://site.api.espn.com/apis/site/v3",
    ESPNDomain.CORE:    "https://sports.core.api.espn.com/v2",
    ESPNDomain.CORE_V3: "https://sports.core.api.espn.com/v3",
    ESPNDomain.WEB_V3:  "https://site.web.api.espn.com/apis/common/v3",
    ESPNDomain.CDN:     "https://cdn.espn.com/core",
    ESPNDomain.NOW:     "https://now.core.api.espn.com/v1",
}


def build_url(domain: ESPNDomain, path: str) -> str:
    """Construct a full URL for a given domain and path."""
    base = DOMAIN_BASES[domain]
    return f"{base}/{path.lstrip('/')}"
