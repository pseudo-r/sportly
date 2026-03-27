"""sportly.fantasy.endpoints — ESPN Fantasy endpoint submodules.

Submodules
----------
- ``_client``  — :class:`FantasyClient`, ``GAME_CODES``, ``VIEWS``, ``get_client()``
- ``league``   — ``fetch()``, ``teams()``, ``roster()``, ``standings()``, ``draft()``,
                 ``live_scoring()``, ``transactions()``
- ``players``  — ``players()`` pool with X-Fantasy-Filter header
- ``meta``     — ``game_meta()``, ``season_meta()``
"""
from sportly.fantasy.endpoints import (  # noqa: F401
    league,
    meta,
    players,
)
