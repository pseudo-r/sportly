"""Smoke test: verify the package is importable and public API is intact."""

import pytest


def test_package_version():
    import sportly
    assert sportly.__version__ == "1.1.0"


def test_espn_modules_importable():
    from sportly.espn import (
        australian_football, baseball, basketball, cricket,
        field_hockey, football, golf, hockey, lacrosse,
        mma, racing, rugby, rugby_league, soccer, tennis,
        volleyball, water_polo,
    )
    modules = [
        australian_football, baseball, basketball, cricket,
        field_hockey, football, golf, hockey, lacrosse,
        mma, racing, rugby, rugby_league, soccer, tennis,
        volleyball, water_polo,
    ]
    for mod in modules:
        assert hasattr(mod, "scoreboard"), f"{mod.__name__} missing scoreboard"
        assert hasattr(mod, "news"),       f"{mod.__name__} missing news"


def test_basketball_has_advanced_methods():
    from sportly.espn import basketball
    advanced = ["injuries", "transactions", "leaders", "odds",
                "play_by_play", "cdn_game", "now_news",
                "athlete_stats", "athlete_gamelog"]
    for method in advanced:
        assert hasattr(basketball, method), f"basketball missing {method}"


def test_nhl_importable():
    from sportly import nhl
    from sportly.nhl import NHLClient
    assert callable(NHLClient)


def test_exceptions_importable():
    from sportly.exceptions import (
        SportlyError, NotFoundError, RateLimitError,
        UpstreamError, ParseError, AuthenticationError,
    )


def test_models_importable():
    from sportly.models import Team, Game, Article, Standings, Athlete, Competitor
