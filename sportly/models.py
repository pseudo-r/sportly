"""Pydantic data models returned by all sportly methods.

All models use ``model_config = ConfigDict(extra="allow")`` so that
new fields added by upstream APIs are preserved rather than dropped.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class _Base(BaseModel):
    """Shared config for all sportly models."""

    model_config = ConfigDict(extra="allow", populate_by_name=True)


# ── Teams ─────────────────────────────────────────────────────────────────────


class Logo(BaseModel):
    model_config = ConfigDict(extra="allow")
    href: str = ""
    width: int | None = None
    height: int | None = None
    rel: list[str] = Field(default_factory=list)


class Team(_Base):
    """A sports team.

    Attributes
    ----------
    id:       ESPN team ID (string).
    uid:      Full ESPN UID, e.g. ``"s:40~l:46~t:13"``.
    slug:     URL-safe slug, e.g. ``"los-angeles-lakers"``.
    abbr:     Short abbreviation, e.g. ``"LAL"``.
    name:     Full display name, e.g. ``"Los Angeles Lakers"``.
    nickname: Short name, e.g. ``"Lakers"``.
    location: City / region, e.g. ``"Los Angeles"``.
    color:    Primary hex colour (no ``#``).
    alt_color: Alternate hex colour.
    is_active: Whether the team is currently active.
    logos:    List of logo objects.
    raw:      Full raw dict from the upstream API.
    """

    id: str = ""
    uid: str = ""
    slug: str = ""
    abbr: str = Field("", alias="abbreviation")
    name: str = Field("", alias="displayName")
    nickname: str = ""
    location: str = ""
    color: str = ""
    alt_color: str = Field("", alias="alternateColor")
    is_active: bool = Field(True, alias="isActive")
    logos: list[Logo] = Field(default_factory=list)
    raw: dict[str, Any] = Field(default_factory=dict)


# ── Events / Games ────────────────────────────────────────────────────────────


class Competitor(_Base):
    """One side of a game (home or away)."""

    id: str = ""
    team: Team | None = None
    home_away: str = Field("", alias="homeAway")
    score: str = ""
    winner: bool | None = None


class GameStatus(_Base):
    """Current game status."""

    state: str = ""       # "pre" | "in" | "post"
    detail: str = ""      # e.g. "Final", "Q3 4:23", "7:30 PM ET"
    completed: bool = False
    period: int | None = None
    clock: str = ""


class Game(_Base):
    """A single game / event.

    Attributes
    ----------
    id:          ESPN event ID.
    name:        Long game name, e.g. ``"Los Angeles Lakers vs Boston Celtics"``.
    short_name:  Short form, e.g. ``"LAL vs BOS"``.
    date:        UTC tip-off / kick-off time.
    status:      Current game status.
    competitors: Home and away team info including scores.
    raw:         Full raw dict from the upstream API.
    """

    id: str = ""
    uid: str = ""
    name: str = ""
    short_name: str = Field("", alias="shortName")
    date: datetime | None = None
    status: GameStatus = Field(default_factory=GameStatus)
    competitors: list[Competitor] = Field(default_factory=list)
    raw: dict[str, Any] = Field(default_factory=dict)


# ── News ─────────────────────────────────────────────────────────────────────


class Article(_Base):
    """A news article."""

    id: str = ""
    headline: str = ""
    description: str = ""
    published: datetime | None = None
    type: str = ""
    images: list[dict[str, Any]] = Field(default_factory=list)
    links: dict[str, Any] = Field(default_factory=dict)

    @property
    def thumbnail(self) -> str | None:
        """Return the first image URL, if any."""
        for img in self.images:
            return img.get("url") or img.get("href")
        return None


# ── Standings ─────────────────────────────────────────────────────────────────


class StandingEntry(_Base):
    """One team row in the standings table."""

    team: Team | None = None
    wins: int = 0
    losses: int = 0
    win_pct: float = Field(0.0, alias="winPercent")
    games_behind: float | None = Field(None, alias="gamesBehind")
    raw: dict[str, Any] = Field(default_factory=dict)


class Standings(_Base):
    """League standings."""

    name: str = ""
    season: int | None = None
    entries: list[StandingEntry] = Field(default_factory=list)
    raw: dict[str, Any] = Field(default_factory=dict)


# ── Athlete ───────────────────────────────────────────────────────────────────


class Athlete(_Base):
    """An athlete / player."""

    id: str = ""
    full_name: str = Field("", alias="fullName")
    display_name: str = Field("", alias="displayName")
    short_name: str = Field("", alias="shortName")
    position: str = ""
    jersey: str = ""
    team: Team | None = None
    headshot: str = ""
    is_active: bool = Field(True, alias="active")
    raw: dict[str, Any] = Field(default_factory=dict)
