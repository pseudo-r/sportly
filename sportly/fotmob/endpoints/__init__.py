"""sportly.fotmob.endpoints — FotMob endpoint submodules.

Submodules
----------
- ``_client``  — :class:`FotMobClient`, ``LEAGUES`` constant, ``get_client()``
- ``matches``  — ``matches()`` (daily schedule), ``match()`` (full detail)
- ``leagues``  — ``league()``, ``all_leagues()``, ``tv_listings()``
- ``teams``    — ``team()`` profile + squad
- ``players``  — ``player()``, ``search()``, ``transfers()``, ``world_news()``
"""
from sportly.fotmob.endpoints import (  # noqa: F401
    leagues,
    matches,
    players,
    teams,
)
