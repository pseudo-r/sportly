# sportly.nba — NBA Stats API

> Base URL: `https://stats.nba.com/stats/`  
> No authentication — **7 WAF headers injected automatically** by `NBAClient`  
> Response format: `resultSets[{name, headers[], rowSet[[]]}]` → auto-parsed to dicts

---

## Install

```bash
pip install sportly
```

---

## Quick Start

```python
from sportly import nba

# Today's scoreboard
sb = nba.scoreboard("2025-03-26")
for game in sb["GameHeader"]:
    print(game["GAMECODE"], game["GAME_STATUS_TEXT"])

# League leaders
top_scorers = nba.leaders("PTS", season="2024-25")

# LeBron career stats
stats = nba.career_stats("2544")
for row in stats["SeasonTotalsRegularSeason"]:
    print(row["SEASON_ID"], row["PTS"])

# Curry shot chart
shots = nba.shot_chart("201939", "2024-25")
makes = [s for s in shots if s["SHOT_MADE_FLAG"] == 1]

# Full standings
records = nba.standings("2024-25")

print(nba.TEAM_IDS)    # {"LAL": "1610612747", ...}
print(nba.PLAYER_IDS)  # {"LeBron James": "2544", ...}
```

---

## WAF Headers (Injected Automatically)

The NBA Stats API is protected by Akamai WAF. `sportly.nba` sends these on every request:

```
Origin: https://www.nba.com
Referer: https://www.nba.com/
x-nba-stats-origin: stats
x-nba-stats-token: true
User-Agent: Chrome/122
Accept-Language: en-US,en;q=0.9
```

---

## Constants

```python
nba.LEAGUE_NBA     # "00"
nba.LEAGUE_WNBA    # "10"
nba.LEAGUE_GLEAGUE # "20"

nba.TEAM_IDS  = {"LAL": "1610612747", "BOS": "1610612738", ...}  # 30 teams

nba.PLAYER_IDS = {
    "LeBron James":            "2544",
    "Stephen Curry":           "201939",
    "Nikola Jokic":            "203999",
    "Giannis Antetokounmpo":   "203507",
    "Luka Doncic":             "1629029",
    "Victor Wembanyama":       "1641705",
    ...
}
```

---

## Endpoints

### Games

| Function | Description |
|----------|-------------|
| `nba.scoreboard(date)` | Today's scores → `{GameHeader, LineScore, TeamLeaders}` |
| `nba.boxscore(game_id)` | Traditional boxscore v3 |
| `nba.play_by_play(game_id)` | PBP actions v3 (`.game.actions[]`) |
| `nba.win_probability(game_id)` | Win probability by play |

**Game ID format:** 10-digit string, e.g. `"0022401045"`  
(Regular season format: `00{season_year}{game_number}`)

### Teams

| Function | Description |
|----------|-------------|
| `nba.teams(league_id="00")` | All NBA teams |
| `nba.team_stats(team_id, season, per_mode="PerGame")` | Season stats dashboard |
| `nba.roster(team_id, season)` | Current team roster |

### Players

| Function | Description |
|----------|-------------|
| `nba.player(player_id)` | Biographical info |
| `nba.career_stats(player_id, per_mode="PerGame")` | Career stats by season |
| `nba.game_log(player_id, season, season_type="Regular Season")` | Game-by-game log |
| `nba.shot_chart(player_id, season)` | Shot locations (X/Y + make/miss) |

**`per_mode` options:** `"PerGame"`, `"Totals"`, `"Per36"`, `"Per100Possessions"`  
**`season` format:** `"2024-25"`

```python
# Jokic 2024-25 per-game stats
stats = nba.career_stats("203999", per_mode="PerGame")
latest = stats["SeasonTotalsRegularSeason"][-1]
print(latest["PTS"], latest["REB"], latest["AST"])
```

### League

| Function | Description |
|----------|-------------|
| `nba.standings(season, season_type="Regular Season")` | Full standings |
| `nba.leaders(stat="PTS", season="2024-25")` | Statistical leaders |
| `nba.draft(season)` | Draft history by year |

**Stat categories:** `"PTS"`, `"REB"`, `"AST"`, `"STL"`, `"BLK"`, `"FG_PCT"`, `"FG3_PCT"`, `"FT_PCT"`

---

## resultSets Parser

NBA API returns rows as arrays. `parse_result_sets()` converts them:

```python
from sportly.nba._client import parse_result_sets

raw = client.get("leaguestandingsv3", ...)
# raw: {"resultSets": [{"name": "Standings", "headers": [...], "rowSet": [[...]]}]}

data = parse_result_sets(raw)
# data: {"Standings": [{"TeamName": "Celtics", "WINS": 64, ...}, ...]}
```

---

## Common resultSet Keys

| Endpoint | Key | Contents |
|----------|-----|----------|
| `scoreboardv2` | `GameHeader` | Game IDs, status, arena |
| `scoreboardv2` | `LineScore` | Team scores by period |
| `playercareerstats` | `SeasonTotalsRegularSeason` | Career per-season totals |
| `playergamelog` | `PlayerGameLog` | Per-game stats |
| `shotchartdetail` | `Shot_Chart_Detail` | Shot coords + results |
| `leaguestandingsv3` | `Standings` | Full standings table |
| `leagueleaders` | `LeagueLeaders` | Ranked players |
| `leagueteams` | `LeagueTeams` | All teams |

---

*Source: stats.nba.com — unofficial use, not affiliated with NBA.*
