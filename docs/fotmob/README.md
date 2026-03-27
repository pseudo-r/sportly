# sportly.fotmob — FotMob API

> Base URL: `https://www.fotmob.com/api/`  
> No authentication required · No versioning · All endpoints under `/api/`  
> Unique data: **xG, xA, momentum graphs, player ratings, shot maps**

---

## Install

```bash
pip install sportly
```

---

## Quick Start

```python
from sportly import fotmob

# Today's matches
day = fotmob.matches("20260326")
for league in day["leagues"]:
    for match in league["matches"]:
        print(match["home"]["name"], "vs", match["away"]["name"])

# Match detail (xG, lineups, incidents, player ratings)
m = fotmob.match(4310531)

# Premier League table
epl = fotmob.league(47)
table = epl["table"][0]["data"]["table"]["all"]
for row in table:
    print(row["name"], row["pts"])

# Man City squad + recent results
city = fotmob.team(8456)

# De Bruyne stats
player = fotmob.player(174543)

# Search
results = fotmob.search("haaland")

print(fotmob.LEAGUES)  # popular league IDs
```

---

## League IDs (`fotmob.LEAGUES`)

| League | ID |
|--------|----|
| Premier League | 47 |
| La Liga | 87 |
| Bundesliga | 54 |
| Serie A | 55 |
| Ligue 1 | 53 |
| Eredivisie | 57 |
| Champions League | 42 |
| Europa League | 73 |
| Conference League | 10007 |
| MLS | 130 |
| Brasileirao | 268 |
| Liga MX | 208 |
| Copa America | 322 |
| World Cup | 77 |

---

## Endpoints

| Function | Description |
|----------|-------------|
| `fotmob.matches(date)` | All matches for date (`YYYYMMDD`) → `{leagues[].matches[]}` |
| `fotmob.match(match_id)` | Full match: lineups, incidents, stats, xG, player ratings |
| `fotmob.league(league_id)` | League: standings, recent/upcoming fixtures |
| `fotmob.team(team_id)` | Team: squad, season stats, fixture history |
| `fotmob.player(player_id)` | Player: career stats, season stats, recent matches |
| `fotmob.search(term)` | Search teams, players, tournaments |
| `fotmob.all_leagues()` | Full directory of all tracked competitions |
| `fotmob.tv_listings(date=None)` | Broadcast schedule |
| `fotmob.world_news()` | Global football news feed |
| `fotmob.transfers()` | Transfer rumours and confirmed moves |

---

## Match Detail Response Shape

```json
{
  "general": {
    "matchId": 4310531,
    "homeTeam": {"name": "Manchester City", "id": 8456},
    "awayTeam": {"name": "Arsenal", "id": 9825}
  },
  "header": {
    "status": {"finished": true, "started": true},
    "teams": [
      {"id": 8456, "score": 2, "name": "Manchester City"},
      {"id": 9825, "score": 1, "name": "Arsenal"}
    ]
  },
  "content": {
    "stats": {
      "Periods": {
        "All": [
          {"title": "Expected goals", "stats": [
            {"title": "xG", "home": "1.84", "away": "0.65"}
          ]}
        ]
      }
    },
    "momentum": {"data": [...]},
    "lineup": {...},
    "playerRatings": [
      {"playerId": 174543, "rating": {"num": "8.7"}}
    ]
  }
}
```

---

## Finding IDs

**League IDs:** Use `fotmob.all_leagues()` or browse `fotmob.LEAGUES`.

**Match IDs:** From `fotmob.matches("YYYYMMDD")` → `leagues[].matches[].id`

**Team IDs:** From `fotmob.league(47)` → `table[].data.table.all[].id`

**Player IDs:** From `fotmob.team(8456)` → `squad[].members[].id`

```python
# Get all EPL matches today, then full detail for first match
day = fotmob.matches("20260326")
epl_matches = next(l for l in day["leagues"] if l["id"] == 47)["matches"]
first_match = fotmob.match(epl_matches[0]["id"])
```

---

*Source: fotmob.com/api — unofficial use, not affiliated with FotMob.*
