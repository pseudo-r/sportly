"""sportly — Python SDK for ESPN and NHL sports data.

Quick start
-----------
::

    from sportly.espn import basketball, football, soccer, hockey

    # NBA teams
    teams = basketball.teams("nba")

    # Today's NBA scores
    scores = basketball.scoreboard("nba")

    # EPL table
    table = soccer.standings("eng.1")

    # NFL game summary
    game = football.game("nfl", "401671803")

"""

__version__ = "1.0.0"
__author__ = "Joseph Wilson"
__email__ = "jwilson@kloverdevs.ca"

# Convenience re-exports
from sportly.client import SportlyClient  # noqa: F401
from sportly.exceptions import SportlyError, NotFoundError, RateLimitError  # noqa: F401

__all__ = [
    "__version__",
    "SportlyClient",
    "SportlyError",
    "NotFoundError",
    "RateLimitError",
]
