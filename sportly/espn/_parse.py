"""Pure parse functions for ESPN API responses.

All functions are stateless and accept raw dicts, returning sportly models.
Import these in endpoint modules rather than duplicating parse logic.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from sportly.models import Article, Athlete, Competitor, Game, GameStatus, Logo, Standings, StandingEntry, Team


def parse_team(raw: dict[str, Any]) -> Team:
    """Parse a raw ESPN team dict (handles both wrapped and unwrapped forms)."""
    t = raw.get("team", raw)
    logos = [Logo(**lg) for lg in t.get("logos", []) if isinstance(lg, dict)]
    return Team(
        id=str(t.get("id", "")),
        uid=t.get("uid", ""),
        slug=t.get("slug", ""),
        abbreviation=t.get("abbreviation", ""),
        displayName=t.get("displayName", t.get("name", "")),
        nickname=t.get("nickname", ""),
        location=t.get("location", ""),
        color=t.get("color", ""),
        alternateColor=t.get("alternateColor", ""),
        isActive=t.get("isActive", True),
        logos=logos,
        raw=t,
    )


def parse_game(raw: dict[str, Any]) -> Game:
    """Parse a raw ESPN event dict into a Game model."""
    st = raw.get("status", {})
    st_type = st.get("type", {})
    status = GameStatus(
        state=st_type.get("state", ""),
        detail=st_type.get("detail", ""),
        completed=st_type.get("completed", False),
        period=st.get("period"),
        clock=st.get("displayClock", ""),
    )
    competitions = raw.get("competitions", [{}])
    comp0 = competitions[0] if competitions else {}
    competitors = []
    for c in comp0.get("competitors", []):
        team_raw = c.get("team", {})
        competitors.append(Competitor(
            id=str(c.get("id", "")),
            team=parse_team(team_raw) if team_raw else None,
            homeAway=c.get("homeAway", ""),
            score=str(c.get("score", "")),
            winner=c.get("winner"),
        ))
    date: datetime | None = None
    if date_str := raw.get("date", ""):
        try:
            date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        except ValueError:
            pass
    return Game(
        id=str(raw.get("id", "")),
        uid=raw.get("uid", ""),
        name=raw.get("name", ""),
        shortName=raw.get("shortName", ""),
        date=date,
        status=status,
        competitors=competitors,
        raw=raw,
    )


def parse_article(raw: dict[str, Any]) -> Article | None:
    """Parse a raw ESPN article dict. Returns None if no headline found."""
    headline = raw.get("headline") or raw.get("title") or ""
    if not headline:
        return None
    pub: datetime | None = None
    if pub_str := raw.get("published", ""):
        try:
            pub = datetime.fromisoformat(pub_str.replace("Z", "+00:00"))
        except ValueError:
            pass
    return Article(
        id=str(raw.get("dataSourceIdentifier") or raw.get("id") or ""),
        headline=headline[:500],
        description=raw.get("description") or raw.get("abstract") or "",
        published=pub,
        type=str(raw.get("type", "")),
        images=raw.get("images", []),
        links=raw.get("links", {}),
    )


def parse_athlete(raw: dict[str, Any]) -> Athlete:
    """Parse a raw ESPN athlete dict."""
    team_raw = raw.get("team")
    return Athlete(
        id=str(raw.get("id", "")),
        fullName=raw.get("fullName", raw.get("displayName", "")),
        displayName=raw.get("displayName", ""),
        shortName=raw.get("shortName", ""),
        position=_safe_str(raw.get("position")),
        jersey=raw.get("jersey", ""),
        active=raw.get("active", True),
        headshot=_safe_str(raw.get("headshot")),
        team=parse_team(team_raw) if isinstance(team_raw, dict) else None,
        raw=raw,
    )


def parse_standings(data: dict[str, Any]) -> Standings:
    """Parse a raw ESPN standings response."""
    season: int | None = None
    if isinstance(season_data := data.get("season"), dict):
        season = season_data.get("year")
    entries: list[StandingEntry] = []
    for group in data.get("children", data.get("standings", {}).get("entries", [])):
        if isinstance(group, dict):
            for entry in group.get("standings", {}).get("entries", []):
                entries.append(parse_standing_entry(entry))
    return Standings(name=data.get("name", ""), season=season, entries=entries, raw=data)


def parse_standing_entry(raw: dict[str, Any]) -> StandingEntry:
    """Parse one row from an ESPN standings response."""
    team_raw = raw.get("team", {})
    stats = {s["name"]: s.get("value", 0) for s in raw.get("stats", []) if "name" in s}
    return StandingEntry(
        team=parse_team(team_raw) if team_raw else None,
        wins=int(stats.get("wins", 0)),
        losses=int(stats.get("losses", 0)),
        winPercent=float(stats.get("winPercent", 0.0)),
        gamesBehind=stats.get("gamesBehind"),
        raw=raw,
    )


def _safe_str(val: Any) -> str:
    if isinstance(val, dict):
        return val.get("href") or val.get("abbreviation") or ""
    return str(val) if val else ""
