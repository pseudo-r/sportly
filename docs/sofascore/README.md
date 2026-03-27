# sportly.sofascore — Sofascore API

> Base URL: `https://api.sofascore.com/api/v1/`  
> Multi-sport: football, basketball, tennis, ice-hockey, baseball, and more  
> ⚠️ **Requires `curl_cffi`** — Akamai WAF blocks standard `httpx`/`requests`

---

## Install

```bash
# Include the sofascore extra (adds curl_cffi)
pip install sportly[sofascore]

# Or install curl_cffi manually
pip install sportly curl_cffi>=0.6
```

---

## Quick Start

```python
from sportly import sofascore

# Football matches today
games = sofascore.matches("football", "2026-03-26")
for g in games:
    print(g["homeTeam"]["name"], "vs", g["awayTeam"]["name"])

# Full match detail
event = sofascore.match(11352523)

# Statistics (possession, shots, xG)
stats = sofascore.match_stats(11352523)

# Confirmed lineups
lineups = sofascore.lineups(11352523)

# Momentum graph (football)
momentum = sofascore.momentum(11352523)

# Player profile
p = sofascore.player(814123)

# Team + squad
t = sofascore.team(4705)
squad = sofascore.squad(4705)
```

---

## WAF / TLS Fingerprinting

Sofascore uses Akamai Bot Manager with TLS fingerprinting. Standard Python HTTP clients return `403`.

`sportly.sofascore` uses [`curl_cffi`](https://github.com/yifeikong/curl-cffi) to impersonate Chrome at the TLS layer:

```python
from curl_cffi import requests
session = requests.Session(impersonate="chrome")
resp = session.get("https://api.sofascore.com/api/v1/event/11352523")
```

If `curl_cffi` is missing, you'll see:
```
ImportError: sportly.sofascore requires curl_cffi for TLS fingerprint bypass.
Install with: pip install sportly[sofascore]
```

---

## Sport Slugs (`sofascore.SPORTS`)

| Alias | API Slug |
|-------|----------|
| `"football"` | `football` |
| `"soccer"` | `football` |
| `"basketball"` | `basketball` |
| `"tennis"` | `tennis` |
| `"ice-hockey"` | `ice-hockey` |
| `"hockey"` | `ice-hockey` |
| `"baseball"` | `baseball` |
| `"american-football"` | `american-football` |
| `"esports"` | `esports` |

---

## Endpoints

### Scheduled Events

| Function | Description |
|----------|-------------|
| `sofascore.matches(sport, date)` | All events for sport on `YYYY-MM-DD` |

### Match / Event

| Function | Description |
|----------|-------------|
| `sofascore.match(event_id)` | Core event (teams, score, status, tournament) |
| `sofascore.match_stats(event_id)` | Match statistics (possession, shots, xG) |
| `sofascore.lineups(event_id)` | Confirmed lineups (formations, players) |
| `sofascore.incidents(event_id)` | Goals, cards, substitutions timeline |
| `sofascore.momentum(event_id)` | Momentum graph (football) or power curve (tennis) |
| `sofascore.point_by_point(event_id)` | Point-by-point data (tennis only) |

### Players

| Function | Description |
|----------|-------------|
| `sofascore.player(player_id)` | Player profile |
| `sofascore.player_seasons(player_id)` | Career stats by season |

### Teams

| Function | Description |
|----------|-------------|
| `sofascore.team(team_id)` | Team profile |
| `sofascore.squad(team_id)` | Team roster / squad list |

### Tournaments

| Function | Description |
|----------|-------------|
| `sofascore.tournaments(sport)` | All tournaments for a sport |
| `sofascore.popular(locale="US")` | Popular leagues/entities by locale |

---

## Response Examples

### `sofascore.match_stats()`

```json
{
  "statistics": [
    {
      "period": "ALL",
      "groups": [
        {
          "groupName": "Football",
          "statisticsItems": [
            {"name": "Ball possession", "home": "57%", "away": "43%"},
            {"name": "Expected goals", "home": "1.84", "away": "0.53"},
            {"name": "Total shots", "home": "14", "away": "7", "homeTotal": 14, "awayTotal": 7}
          ]
        }
      ]
    }
  ]
}
```

### `sofascore.lineups()`

```json
{
  "home": {
    "players": [
      {
        "player": {"id": 814123, "name": "Erling Haaland", "position": "F"},
        "position": "ST",
        "shirtNumber": 9,
        "statistics": {"rating": 8.7, "goals": 1}
      }
    ],
    "formation": "4-3-3"
  },
  "away": {...}
}
```

---

## Finding IDs

| Resource | How to find IDs |
|----------|----------------|
| Event/Match | `sofascore.matches("football", "YYYY-MM-DD")` → `events[].id` |
| Player | `sofascore.squad(team_id)` → `players[].player.id` |
| Team | `sofascore.tournaments("football")` → browse tournament → season → standings |
| Tournament | `sofascore.tournaments("football")` → `uniqueTournaments[].id` |

---

*Source: api.sofascore.com — unofficial use, not affiliated with Sofascore.*
