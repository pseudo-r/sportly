"""sportly.nfl.endpoints — NFL endpoint submodules (delegates to ESPN infrastructure).

Submodules
----------
- ``games``     — ``scoreboard()``, ``game()``, ``cdn_game()``, ``play_by_play()``, ``odds()``
- ``teams``     — ``teams()``, ``team()``, ``roster()``, ``team_schedule()``, ``depth_chart()``
- ``players``   — ``athlete()``, ``athlete_stats()``, ``athlete_gamelog()``, ``athlete_news()``
- ``league``    — ``standings()``, ``injuries()``, ``transactions()``, ``news()``, ``qbr()``
"""
from sportly.nfl.endpoints import (  # noqa: F401
    games,
    league,
    players,
    teams,
)
