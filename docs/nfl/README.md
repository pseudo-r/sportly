# sportly.nfl — NFL Data via ESPN Public APIs

> NFL's native `api.nfl.com` requires OAuth 2.0. All reliable public NFL data  
> is served through **ESPN's public infrastructure** — the same endpoints powering  
> ESPN.com and the ESPN app.

---

## Quick Start

```python
from sportly import nfl

# Week 1 scoreboard
sb = nfl.scoreboard(week=1, season=2024)

# All 32 teams
teams = nfl.teams()

# Kansas City Chiefs schedule (ESPN ID: 12)
sched = nfl.team_schedule("12", season=2024)

# Play-by-play
pbp = nfl.play_by_play("401671827")

# Depth chart — Cowboys (ID: 6)
dc = nfl.depth_chart("6")

# Injuries league-wide
inj = nfl.injuries()

# QBR leaders
qbr = nfl.qbr(season=2024, week=1)

print(nfl.TEAM_IDS)  # {"KC": 12, "PHI": 21, ...}
```

---

## Constants

```python
nfl.SPORT   # "football"
nfl.LEAGUE  # "nfl"

nfl.TEAM_IDS = {
    "ARI": 22, "ATL": 1,  "BAL": 33, "BUF": 2,  "CAR": 29, "CHI": 3,
    "CIN": 4,  "CLE": 5,  "DAL": 6,  "DEN": 7,  "DET": 8,  "GB":  9,
    "HOU": 34, "IND": 11, "JAX": 30, "KC":  12, "LV":  13, "LAC": 24,
    "LAR": 14, "MIA": 15, "MIN": 16, "NE":  17, "NO":  18, "NYG": 19,
    "NYJ": 20, "PHI": 21, "PIT": 23, "SF":  25, "SEA": 26, "TB":  27,
    "TEN": 10, "WSH": 28,
}
```

---

## Endpoints

### Games / Schedule

| Function | Description |
|----------|-------------|
| `nfl.scoreboard(week=None, season=None, season_type=None, date=None)` | NFL scores |
| `nfl.game(game_id)` | Full game summary (boxscore + drives + scoring plays) |
| `nfl.cdn_game(game_id)` | CDN game package (drives, win probability) |
| `nfl.play_by_play(event_id, limit=300)` | Play-by-play log |
| `nfl.odds(event_id)` | Betting lines |

**`season_type`:** `1`=preseason, `2`=regular (default), `3`=postseason

### Teams

| Function | Description |
|----------|-------------|
| `nfl.teams(limit=32)` | All 32 NFL teams |
| `nfl.team(team_id)` | Single team by ESPN ID |
| `nfl.roster(team_id)` | Current team roster |
| `nfl.team_schedule(team_id, season=None, season_type=None)` | Full team schedule |
| `nfl.depth_chart(team_id)` | Positional depth chart |

### Athletes / Players

| Function | Description |
|----------|-------------|
| `nfl.athlete(athlete_id)` | Player profile by ESPN athlete ID |
| `nfl.athlete_stats(athlete_id, season=None)` | Season statistics |
| `nfl.athlete_gamelog(athlete_id)` | Game-by-game log |
| `nfl.athlete_news(athlete_id)` | Player news articles |

### League

| Function | Description |
|----------|-------------|
| `nfl.standings(season=None)` | NFL standings |
| `nfl.injuries()` | League-wide injury report |
| `nfl.transactions()` | Recent transactions |
| `nfl.news(limit=25)` | NFL news feed |
| `nfl.qbr(season=None, season_type=2, week=None)` | ESPN QBR leaderboard |

---

## ESPN Domains Used

| Domain | Data |
|--------|------|
| `site.api.espn.com/apis/site/v2/` | Scoreboard, teams, rosters, injuries, news |
| `sports.core.api.espn.com/v2/` | Athletes, stats, play-by-play, odds |
| `cdn.espn.com/core/` | CDN game packages (drives, win prob) |

---

## Native NFL API Note

The official `api.nfl.com` endpoints require OAuth 2.0 Bearer token:

```http
POST https://api.nfl.com/v1/reroute
Authorization: Bearer {token}
```

If you want to use the native API, see `Public-NFL-API` documentation. This module intentionally uses ESPN's public NFL data instead.

---

*Source: ESPN public APIs — unofficial use, not affiliated with NFL or ESPN.*
