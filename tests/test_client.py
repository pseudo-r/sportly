"""Tests for SportlyClient error handling."""

from __future__ import annotations

import httpx
import pytest

from sportly.client import SportlyClient
from sportly.exceptions import NotFoundError, RateLimitError, SportlyError, UpstreamError


class TestClientErrorMapping:
    """Verify HTTP status codes map to the correct exception types."""

    def _client_with_response(self, status_code: int, body: str = "{}") -> SportlyClient:
        """Return a SportlyClient that always responds with the given status."""
        transport = httpx.MockTransport(
            lambda request: httpx.Response(status_code, content=body.encode())
        )
        client = SportlyClient()
        client._http = httpx.Client(transport=transport)
        return client

    def test_404_raises_not_found(self):
        c = self._client_with_response(404)
        with pytest.raises(NotFoundError):
            c.get("https://example.com/api")

    def test_429_raises_rate_limit(self):
        c = self._client_with_response(429)
        with pytest.raises(RateLimitError):
            c.get("https://example.com/api")

    def test_500_raises_upstream_error(self):
        c = self._client_with_response(500)
        with pytest.raises(UpstreamError):
            c.get("https://example.com/api")

    def test_400_raises_sportly_error(self):
        c = self._client_with_response(400)
        with pytest.raises(SportlyError):
            c.get("https://example.com/api")

    def test_200_returns_dict(self):
        c = self._client_with_response(200, '{"hello": "world"}')
        result = c.get("https://example.com/api")
        assert result == {"hello": "world"}
