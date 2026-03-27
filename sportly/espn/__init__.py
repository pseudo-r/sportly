"""sportly.espn — ESPN data source (17 sports, 139+ leagues, 6 API domains).

Usage
-----
::

    from sportly.espn import basketball, football, soccer, hockey
    from sportly.espn import baseball, cricket, tennis, golf, mma, racing
    from sportly.espn import lacrosse, volleyball, water_polo
    from sportly.espn import field_hockey, rugby, rugby_league, australian_football

    # NBA scoreboard today
    games = basketball.scoreboard("nba")

    # All EPL teams (260+ soccer leagues supported)
    teams = soccer.teams("eng.1")

    # NFL injury report
    report = football.injuries("nfl")

    # NBA play-by-play
    plays = basketball.play_by_play("401671803", league="nba")

    # Full CDN game package (drives, odds, win probability)
    pkg = football.cdn_game("401671803")

ESPN API Domains Used
----------------------
- ``site.api.espn.com/apis/site/v2/`` — scores, teams, news, injuries, transactions
- ``site.api.espn.com/apis/v2/`` — standings (site/v2 returns a stub)
- ``sports.core.api.espn.com/v2/`` — athletes, stats, odds, play-by-play
- ``site.web.api.espn.com/apis/common/v3/`` — athlete stats, gamelog, splits
- ``cdn.espn.com/core/`` — full game packages (requires xhr=1)
- ``now.core.api.espn.com/v1/`` — real-time news feed

Sports Coverage
---------------
17 sports · 139+ leagues · verified 2026-03-26
"""

from sportly.espn import (  # noqa: F401
    australian_football,
    baseball,
    basketball,
    cricket,
    field_hockey,
    football,
    golf,
    hockey,
    lacrosse,
    mma,
    racing,
    rugby,
    rugby_league,
    soccer,
    tennis,
    volleyball,
    water_polo,
)

__all__ = [
    "basketball",
    "football",
    "soccer",
    "hockey",
    "baseball",
    "cricket",
    "tennis",
    "golf",
    "mma",
    "racing",
    "lacrosse",
    "volleyball",
    "water_polo",
    "field_hockey",
    "rugby",
    "rugby_league",
    "australian_football",
]
