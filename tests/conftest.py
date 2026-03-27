"""Shared pytest fixtures for sportly tests."""

from __future__ import annotations

from unittest.mock import MagicMock
from typing import Any

import pytest

from sportly.client import SportlyClient, set_client


class MockSportlyClient(SportlyClient):
    """A SportlyClient that never makes real HTTP calls."""

    def __init__(self) -> None:
        super().__init__()
        self._responses: dict[str, dict[str, Any]] = {}

    def register(self, url_fragment: str, response: dict[str, Any]) -> None:
        """Register a canned response for a URL substring."""
        self._responses[url_fragment] = response

    def get(self, url: str, *, params: dict[str, Any] | None = None) -> dict[str, Any]:  # type: ignore[override]
        for fragment, response in self._responses.items():
            if fragment in url:
                return response
        raise ValueError(f"No mock registered for URL: {url}")


@pytest.fixture()
def mock_client() -> MockSportlyClient:
    """Return a MockSportlyClient and install it as the global default."""
    client = MockSportlyClient()
    set_client(client)
    yield client
    # Reset after test
    set_client(SportlyClient())


# ── Canned fixtures ───────────────────────────────────────────────────────────

@pytest.fixture()
def nba_teams_payload() -> dict[str, Any]:
    return {
        "sports": [{
            "leagues": [{
                "teams": [
                    {"team": {
                        "id": "13",
                        "uid": "s:40~l:46~t:13",
                        "slug": "los-angeles-lakers",
                        "abbreviation": "LAL",
                        "displayName": "Los Angeles Lakers",
                        "nickname": "Lakers",
                        "location": "Los Angeles",
                        "color": "552583",
                        "alternateColor": "FDB927",
                        "isActive": True,
                        "logos": [{"href": "https://a.espncdn.com/i/teamlogos/nba/500/lal.png", "rel": ["full", "default"]}],
                    }},
                    {"team": {
                        "id": "2",
                        "uid": "s:40~l:46~t:2",
                        "slug": "boston-celtics",
                        "abbreviation": "BOS",
                        "displayName": "Boston Celtics",
                        "nickname": "Celtics",
                        "location": "Boston",
                        "color": "007A33",
                        "alternateColor": "BA9653",
                        "isActive": True,
                        "logos": [],
                    }},
                ]
            }]
        }]
    }


@pytest.fixture()
def nba_scoreboard_payload() -> dict[str, Any]:
    return {
        "events": [
            {
                "id": "401671803",
                "uid": "s:40~l:46~e:401671803",
                "name": "Los Angeles Lakers vs Boston Celtics",
                "shortName": "LAL vs BOS",
                "date": "2024-12-25T20:00:00Z",
                "status": {
                    "type": {
                        "state": "post",
                        "completed": True,
                        "detail": "Final",
                    },
                    "period": 4,
                    "displayClock": "0:00",
                },
                "competitions": [{
                    "competitors": [
                        {
                            "id": "13",
                            "homeAway": "home",
                            "score": "110",
                            "winner": True,
                            "team": {
                                "id": "13",
                                "abbreviation": "LAL",
                                "displayName": "Los Angeles Lakers",
                            },
                        },
                        {
                            "id": "2",
                            "homeAway": "away",
                            "score": "105",
                            "winner": False,
                            "team": {
                                "id": "2",
                                "abbreviation": "BOS",
                                "displayName": "Boston Celtics",
                            },
                        },
                    ]
                }],
            }
        ]
    }


@pytest.fixture()
def nba_news_payload() -> dict[str, Any]:
    return {
        "articles": [
            {
                "dataSourceIdentifier": "abc123",
                "headline": "LeBron James scores 30 points",
                "description": "Lakers defeat Celtics on Christmas Day.",
                "published": "2024-12-25T23:00:00Z",
                "type": "Story",
                "images": [{"url": "https://a.espncdn.com/photo/2024/1225/lbj.jpg"}],
                "links": {"web": {"href": "https://www.espn.com/nba/story/abc123"}},
            }
        ]
    }


@pytest.fixture()
def epl_standings_payload() -> dict[str, Any]:
    return {
        "name": "English Premier League",
        "season": {"year": 2024},
        "children": [
            {
                "standings": {
                    "entries": [
                        {
                            "team": {
                                "id": "359",
                                "abbreviation": "MCI",
                                "displayName": "Manchester City",
                            },
                            "stats": [
                                {"name": "wins", "value": 20},
                                {"name": "losses", "value": 3},
                                {"name": "winPercent", "value": 0.769},
                                {"name": "gamesBehind", "value": 0.0},
                            ],
                        }
                    ]
                }
            }
        ],
    }
