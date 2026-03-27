"""fantasy.endpoints._client — ESPN Fantasy API HTTP client."""
from __future__ import annotations
from typing import Any

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential
from sportly.exceptions import NotFoundError, RateLimitError, SportlyError

BASE_URL = "https://lm-api-reads.fantasy.espn.com/apis/v3/games"

GAME_CODES: dict[str, str] = {
    "ffl": "Fantasy Football",
    "fba": "Fantasy Basketball",
    "flb": "Fantasy Baseball",
    "fhl": "Fantasy Hockey",
}

VIEWS = {
    "mSettings", "mTeam", "mRoster", "mMatchupScore", "mMatchup",
    "mScoreboard", "mStandings", "mSchedule", "mBoxscore", "mLiveScoring",
    "mDraftDetail", "mTransactions2", "mStatus", "kona_player_info",
    "proTeamSchedules_wl",
}


class FantasyClient:
    """Thin HTTP client for ``lm-api-reads.fantasy.espn.com``."""

    def __init__(self, timeout: float = 10.0, cookies: dict[str, str] | None = None) -> None:
        self._http = httpx.Client(
            headers={"Accept": "application/json"},
            cookies=cookies or {},
            timeout=timeout,
        )

    @retry(
        retry=retry_if_exception_type(httpx.TransportError),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=0.5, min=0.5, max=8),
        reraise=True,
    )
    def get(self, path: str, *, headers: dict | None = None, **params: Any) -> Any:
        url = f"{BASE_URL}/{path.lstrip('/')}"
        try:
            resp = self._http.get(
                url,
                params={k: v for k, v in params.items() if v is not None},
                headers=headers or {},
            )
        except httpx.TransportError as exc:
            raise SportlyError(str(exc)) from exc
        if resp.status_code == 404:
            raise NotFoundError(f"Not found: {url}", status_code=404, url=url)
        if resp.status_code == 429:
            raise RateLimitError("ESPN Fantasy rate limited", status_code=429)
        resp.raise_for_status()
        return resp.json()

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> "FantasyClient":
        return self

    def __exit__(self, *_: Any) -> None:
        self.close()


_default: FantasyClient | None = None


def get_client(cookies: dict[str, str] | None = None) -> FantasyClient:
    """Return a :class:`FantasyClient` — creates a new one only if cookies are provided."""
    global _default
    if cookies:
        return FantasyClient(cookies=cookies)
    if _default is None:
        _default = FantasyClient()
    return _default
