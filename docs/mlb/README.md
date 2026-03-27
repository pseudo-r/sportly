# sportly.mlb — MLB Stats API

> Base URL: `https://statsapi.mlb.com/api/v1/`  
> No authentication required · v1 only · `sportly` handles retries automatically

---

## Install

```bash
pip install sportly
```

---

## Quick Start

```python
from sportly import mlb

# Today's games
games = mlb.schedule()

# April 1, 2025 games with probable pitchers
games = mlb.schedule(date="2025-04-01", hydrate="team,linescore,probablePitcher")

# Shohei Ohtani profile
ohtani = mlb.player(660271)

# Home run leaders, 2025
leaders = mlb.leaders("homeRuns", season=2025)

# Dodgers roster
roster = mlb.roster(119)

# Game boxscore
box = mlb.boxscore(745444)

# AL + NL standings
records = mlb.standings(season=2025)

# Browse team IDs
print(mlb.TEAM_IDS)   # {"LAD": 119, "NYY": 147, ...}
```

---

## Team Constants

```python
mlb.SPORT_ID   # 1
mlb.LEAGUE_AL  # 103
mlb.LEAGUE_NL  # 104

mlb.TEAM_IDS = {
    "LAA": 108, "ARI": 109, "BAL": 110, "BOS": 111, "CHC": 112,
    "CIN": 113, "CLE": 114, "COL": 115, "DET": 116, "HOU": 117,
    "KC":  118, "LAD": 119, "WSH": 120, "NYM": 121, "ATH": 133,
    "PIT": 134, "SD":  135, "SEA": 136, "SF":  137, "STL": 138,
    "TB":  139, "TEX": 140, "TOR": 141, "MIN": 142, "PHI": 143,
    "ATL": 144, "CWS": 145, "MIA": 146, "NYY": 147, "MIL": 158,
}
```

---

## Endpoints

### Teams

| Function | Description |
|----------|-------------|
| `mlb.teams(season=None)` | All active MLB teams |
| `mlb.team(team_id, season=None)` | Single team by ID (e.g. `119` = Dodgers) |
| `mlb.roster(team_id, roster_type="active")` | Team roster. Types: `"active"`, `"40Man"`, `"fullRoster"` |
| `mlb.team_stats(team_id, stats="season", group="hitting")` | Team statistics |

### Schedule

| Function | Description |
|----------|-------------|
| `mlb.schedule()` | Today's games |
| `mlb.schedule(date="YYYY-MM-DD")` | Games on a specific date |
| `mlb.schedule(start_date=..., end_date=..., team_id=119)` | Date range / team filter |
| `mlb.game_schedule(team_id, start_date, end_date)` | Team season schedule |

**`hydrate` examples:**
```python
mlb.schedule(date="2025-04-01", hydrate="team,linescore,probablePitcher,broadcasts")
```

### Players

| Function | Description |
|----------|-------------|
| `mlb.player(person_id, hydrate=None)` | Player profile |
| `mlb.player_stats(person_id, stats="season", group="hitting", season=None)` | Player stats |
| `mlb.player_gamelog(person_id, season=None, group="hitting")` | Game-by-game log |
| `mlb.search(name)` | Search players by name |

**`stats` types:** `"season"`, `"career"`, `"yearByYear"`, `"gameLog"`  
**`group` types:** `"hitting"`, `"pitching"`, `"fielding"`

**Hydrate example:**
```python
# Ohtani with embedded season hitting stats
mlb.player(660271, hydrate='stats(group=[hitting],type=[season])')
```

### Games

| Function | Description |
|----------|-------------|
| `mlb.boxscore(game_pk)` | Full boxscore |
| `mlb.linescore(game_pk)` | Inning-by-inning linescore |
| `mlb.play_by_play(game_pk)` | Full play-by-play — `allPlays[].playEvents` |
| `mlb.live_feed(game_pk)` | Combined PBP + boxscore + linescore |
| `mlb.win_probability(game_pk)` | Win probability by play |
| `mlb.decisions(game_pk)` | W/L/Save pitcher decisions |
| `mlb.game_content(game_pk)` | Highlights and editorial content |

### League / Stats

| Function | Description |
|----------|-------------|
| `mlb.standings(season=None, standings_type="regularSeason")` | Division standings |
| `mlb.leaders(category, season=None, limit=10)` | Statistical leaders |
| `mlb.transactions(start_date, end_date, team_id=None)` | IL moves, trades, signings |
| `mlb.venues(venue_id=None, hydrate=None)` | Stadium info |
| `mlb.draft(year)` | Draft picks by year |

**Leader categories:** `"homeRuns"`, `"battingAverage"`, `"era"`, `"wins"`, `"strikeOuts"`, `"rbi"`, `"stolenBases"`

```python
# Stadium dimensions + GPS
[dodger_stadium] = mlb.venues(venue_id=22, hydrate="location,fieldInfo")
```

---

## Notable Player IDs

| Player | Person ID |
|--------|-----------|
| Shohei Ohtani | 660271 |
| Aaron Judge | 592450 |
| Mookie Betts | 605141 |
| Mike Trout | 545361 |
| Freddie Freeman | 518692 |

---

## Game Type Codes

| Code | Description |
|------|-------------|
| `S` | Spring Training |
| `R` | Regular Season |
| `F` | Wild Card |
| `D` | Division Series |
| `L` | LCS |
| `W` | World Series |

---

*Source: statsapi.mlb.com/api/v1/ — unofficial use, not affiliated with MLB.*
