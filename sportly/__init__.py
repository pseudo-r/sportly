"""sportly — Python SDK for multi-source sports data.

Sources
-------
- ``sportly.espn``      ESPN (17 sports, 139+ leagues)
- ``sportly.nhl``       NHL Web API + Stats REST
- ``sportly.mlb``       MLB Stats API
- ``sportly.nba``       NBA Stats API (WAF headers auto-injected)
- ``sportly.nfl``       NFL via ESPN public infrastructure
- ``sportly.fantasy``   ESPN Fantasy API v3 (public + private leagues)
- ``sportly.fotmob``    FotMob web API (xG, shot maps, ratings)
- ``sportly.sofascore`` Sofascore API (requires ``pip install sportly[sofascore]``)

Quick start
-----------
::

    from sportly import mlb, nba, nfl, fotmob

    # Today's MLB games
    mlb.schedule()

    # NBA scoring leaders
    nba.leaders("PTS", season="2024-25")

    # NFL scoreboard, Week 1
    nfl.scoreboard(week=1, season=2024)

    # Premier League table
    fotmob.league(47)

    # ESPN fantasy roster
    from sportly import fantasy
    fantasy.roster("ffl", league_id=123456, season=2025)

"""

__version__ = "1.1.0"
__author__ = "Joseph Wilson"
__email__ = "jwilson@kloverdevs.ca"

# Core client and exceptions — importable at top level
from sportly.client import SportlyClient  # noqa: F401
from sportly.exceptions import NotFoundError, RateLimitError, SportlyError  # noqa: F401

__all__ = [
    "__version__",
    "SportlyClient",
    "SportlyError",
    "NotFoundError",
    "RateLimitError",
]
