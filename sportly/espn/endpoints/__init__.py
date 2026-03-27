"""sportly.espn.endpoints — functional ESPN API endpoint modules.

Each sub-module contains plain functions that accept (sport, league, ...)
and return sportly models. Sport modules call these with their own SPORT
constant and LEAGUES mapping.

Available modules
-----------------
- ``teams``     — teams(), team(), roster()
- ``schedule``  — scoreboard(), game()
- ``news``      — news(), now_news()
- ``standings`` — standings(), rankings()
- ``athletes``  — athlete(), overview(), stats(), gamelog(), splits(), leaders()
- ``advanced``  — injuries(), transactions(), odds(), play_by_play(), cdn_game()
"""

from sportly.espn.endpoints import (  # noqa: F401
    advanced,
    athletes,
    news,
    schedule,
    standings,
    teams,
)

__all__ = ["teams", "schedule", "news", "standings", "athletes", "advanced"]
