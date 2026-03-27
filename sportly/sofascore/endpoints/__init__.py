"""sportly.sofascore.endpoints — public endpoint submodules.

Submodules
----------
- ``_client`` — shared HTTP helper (``get()``, ``get_curl_session()``, ``SPORTS``)
- ``schedule`` — ``matches()`` by sport/date
- ``events``   — match detail, stats, lineups, incidents, momentum, point-by-point
- ``players``  — player profile, career seasons
- ``teams``    — team profile, squad roster
- ``tournaments`` — tournament directory, popular entities
"""
from sportly.sofascore.endpoints import (  # noqa: F401
    schedule,
    events,
    players,
    teams,
    tournaments,
)
