"""sportly.nhl — Native NHL Web API client (future expansion).

This module will provide direct access to the official NHL Web API
(api-web.nhle.com) with richer data than ESPN provides: play-by-play,
shift charts, detailed player stats, and draft data.

Status: **stub** — foundational structure in place, full implementation pending.

Usage (when complete)::

    from sportly.nhl import teams, schedule, game

    all_teams = teams()
    today     = schedule()
    pbp       = game("2024020001")
"""

from sportly.nhl._client import NHLClient  # noqa: F401

_inst = NHLClient()

teams    = _inst.teams
schedule = _inst.schedule

__all__ = ["NHLClient", "teams", "schedule"]
