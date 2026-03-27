"""Tests for sportly.nhl client (mocked)."""

from __future__ import annotations

import pytest

from sportly.nhl import NHLClient
from sportly.client import SportlyClient, set_client
from tests.conftest import MockSportlyClient


@pytest.fixture()
def nhl_client(mock_client):
    return NHLClient(client=mock_client)


class TestNHLTeams:
    def test_returns_list(self, nhl_client, mock_client):
        mock_client.register("/franchise", {"data": [
            {"id": 1, "fullName": "Montreal Canadiens"},
            {"id": 2, "fullName": "Toronto Maple Leafs"},
        ]})
        teams = nhl_client.teams()
        assert isinstance(teams, list)
        assert len(teams) == 2
        assert teams[0]["fullName"] == "Montreal Canadiens"


class TestNHLSchedule:
    def test_schedule_today(self, nhl_client, mock_client):
        mock_client.register("/schedule/now", {"gameWeek": []})
        result = nhl_client.schedule()
        assert isinstance(result, dict)

    def test_schedule_by_date(self, nhl_client, mock_client):
        mock_client.register("/schedule/2024-04-15", {"gameWeek": [{"games": []}]})
        result = nhl_client.schedule("2024-04-15")
        assert isinstance(result, dict)
