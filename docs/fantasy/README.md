# sportly.fantasy — ESPN Fantasy API

> Base URL: `https://lm-api-reads.fantasy.espn.com/apis/v3/games/{gameCode}/`  
> **v3 on `lm-api-reads` only** — v1 and v2 are decommissioned.  
> Public leagues: no auth. Private leagues: `espn_s2` + `SWID` cookies.

---

## Install

```bash
pip install sportly
```

---

## Quick Start

```python
from sportly import fantasy

# Public league teams + rosters (no auth)
data = fantasy.league("ffl", league_id=336358, season=2025, views=["mTeam", "mRoster"])

# Private league (requires cookies)
roster = fantasy.roster(
    "ffl",
    league_id=123456,
    season=2025,
    cookies={"espn_s2": "AEB...", "SWID": "{B2C3...}"},
)

# Draft picks
draft = fantasy.draft("ffl", league_id=336358, season=2025)
picks = draft["picks"]

# Live scoring, matchup week 5
live = fantasy.live_scoring("ffl", league_id=336358, season=2025, scoring_period_id=5)

# Season metadata
meta = fantasy.game_meta("ffl")
print(meta["currentSeasonId"])  # 2026
```

---

## Game Codes

| Code | Sport |
|------|-------|
| `ffl` | Fantasy Football |
| `fba` | Fantasy Basketball |
| `flb` | Fantasy Baseball |
| `fhl` | Fantasy Hockey |

---

## Authentication

### Public Leagues
No authentication needed. Omit `cookies`.

### Private Leagues
Pass `cookies={"espn_s2": "...", "SWID": "{...}"}` to any function.

**Finding your credentials (browser):**
1. Log into ESPN Fantasy → `espn.com/fantasy`
2. Open DevTools → Application → Cookies → `espn.com`
3. Copy `espn_s2` value and `SWID` value

---

## Endpoints

### League Data

| Function | Description |
|----------|-------------|
| `fantasy.league(game_code, *, league_id, season, views=None, cookies=None)` | Raw league fetch by view(s) |
| `fantasy.teams(game_code, *, league_id, season, cookies=None)` | All fantasy teams (names, owners, records) |
| `fantasy.roster(game_code, *, league_id, season, scoring_period_id=None, cookies=None)` | All team rosters |
| `fantasy.standings(game_code, *, league_id, season, cookies=None)` | Teams with W/L/PF/PA |
| `fantasy.draft(game_code, *, league_id, season, cookies=None)` | Full draft board (picks + player IDs) |
| `fantasy.live_scoring(game_code, *, league_id, season, scoring_period_id, cookies=None)` | Live matchup scores |
| `fantasy.transactions(game_code, *, league_id, season, cookies=None)` | Waiver claims, trades, FA adds |
| `fantasy.players(game_code, *, season, active_only=True, cookies=None)` | Full player pool |

### Metadata

| Function | Description |
|----------|-------------|
| `fantasy.game_meta(game_code, cookies=None)` | Game info (currentSeasonId, name, active) |
| `fantasy.season_meta(game_code, season, cookies=None)` | Season info (dates, current scoring period) |

---

## Views Reference

Multiple views can be combined in one call to reduce requests:

| View | Data |
|------|------|
| `mSettings` | League rules, scoring settings, roster slots |
| `mTeam` | Team names, owners, overall record |
| `mRoster` | Team rosters with lineup slots |
| `mMatchup` | Matchup schedule |
| `mMatchupScore` | Matchup scores (completed periods) |
| `mLiveScoring` | Live player scores |
| `mBoxscore` | Detailed boxscore |
| `mStandings` | Standings |
| `mSchedule` | Full season schedule |
| `mDraftDetail` | Draft picks (playerId, round, pick number) |
| `mTransactions2` | Transaction history |
| `mStatus` | League status and active season info |
| `kona_player_info` | Player pool with projections |
| `proTeamSchedules_wl` | NFL/NBA bye week info |

```python
# Efficient multi-view call (teams + rosters in one request)
data = fantasy.league("ffl", league_id=YOUR_ID, season=2025,
                       views=["mTeam", "mRoster", "mStandings"])
```

---

## Response Structure

```json
{
  "id": 336358,
  "teams": [
    {
      "id": 1,
      "name": "Team Alpha",
      "abbrev": "ALPH",
      "record": {"overall": {"wins": 10, "losses": 3, "pointsFor": 1420.5}},
      "roster": {"entries": [{"playerId": 2544, "lineupSlotId": 2}]}
    }
  ],
  "draftDetail": {"picks": [{"playerId": 2544, "roundId": 1, "pickVoteCount": 0}]},
  "schedule": [{"id": "1", "matchupPeriodId": 1, "home": {...}, "away": {...}}]
}
```

---

*Source: lm-api-reads.fantasy.espn.com — unofficial use, not affiliated with ESPN.*
