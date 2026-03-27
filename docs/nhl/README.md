# NHL Web API

> Part of the [sportly](https://github.com/pseudo-r/sportly) Python SDK — native integration with the official NHL Web API.

[![PyPI](https://img.shields.io/pypi/v/sportly)](https://pypi.org/project/sportly/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Install

```bash
pip install sportly
```

## Quick Start

```python
from sportly import nhl

# All franchises
teams = nhl.teams()

# Today's schedule
today = nhl.schedule()

# Specific date
games = nhl.schedule("2024-04-15")

# Game boxscore
box = nhl.game("2024020001")

# Play-by-play
pbp = nhl.play_by_play("2024020001")
```

## CLI

```bash
sportly nhl teams
sportly nhl schedule
sportly nhl schedule --date 2024-04-15
sportly nhl game 2024020001
sportly nhl play-by-play 2024020001
```

---

## API Reference

**Base URL:** `https://api-web.nhle.com/v1`

No authentication required.

### Franchises

| Method | Endpoint | Description |
|--------|----------|-------------|
| `nhl.teams()` | `GET /franchise` | All NHL franchise records |

**Response shape:**
```json
{
  "data": [
    {
      "id": 1,
      "fullName": "Montreal Canadiens",
      "teamAbbrev": "MTL",
      "teamCommonName": "Canadiens",
      "teamPlaceName": "Montréal"
    }
  ]
}
```

### Schedule

| Method | Endpoint | Description |
|--------|----------|-------------|
| `nhl.schedule()` | `GET /schedule/now` | Today's schedule (server time) |
| `nhl.schedule("2024-04-15")` | `GET /schedule/2024-04-15` | Schedule for a specific date (`YYYY-MM-DD`) |

**Response shape:**
```json
{
  "gameWeek": [
    {
      "date": "2024-04-15",
      "games": [
        {
          "id": 2024020001,
          "gameType": 2,
          "gameDate": "2024-04-15",
          "startTimeUTC": "2024-04-16T00:00:00Z",
          "homeTeam": { "abbrev": "TOR", "score": 3 },
          "awayTeam": { "abbrev": "BOS", "score": 2 },
          "gameState": "FINAL"
        }
      ]
    }
  ],
  "currentDate": "2024-04-15"
}
```

### Games

| Method | Endpoint | Description |
|--------|----------|-------------|
| `nhl.game(game_id)` | `GET /gamecenter/{gameId}/boxscore` | Full boxscore |
| `nhl.play_by_play(game_id)` | `GET /gamecenter/{gameId}/play-by-play` | All plays with coordinates |

**Finding a `game_id`:**
```python
# Pull game IDs from the schedule
games = nhl.schedule("2024-04-15")
for week in games["gameWeek"]:
    for game in week["games"]:
        print(game["id"])   # e.g. 2024020442
```

**Boxscore response shape:**
```json
{
  "id": 2024020001,
  "homeTeam": {
    "abbrev": "TOR",
    "name": { "default": "Toronto Maple Leafs" },
    "score": 3,
    "sog": 28
  },
  "awayTeam": { "abbrev": "BOS", "score": 2, "sog": 24 },
  "periodDescriptor": { "number": 3, "periodType": "REG" },
  "clock": { "timeRemaining": "00:00", "inIntermission": false },
  "playerByGameStats": {
    "homeTeam": {
      "forwards": [{ "name": {"default": "Auston Matthews"}, "goals": 1, "assists": 1 }],
      "defense": [],
      "goalies": [{ "name": {"default": "Ilya Samsonov"}, "savePctg": 0.923 }]
    }
  }
}
```

**Play-by-play response shape:**
```json
{
  "plays": [
    {
      "eventId": 1,
      "period": 1,
      "timeInPeriod": "10:23",
      "typeDescKey": "shot-on-goal",
      "details": {
        "xCoord": 45,
        "yCoord": -3,
        "shotType": "wrist",
        "shootingPlayerId": 8479318
      }
    }
  ],
  "rosterSpots": [
    {
      "playerId": 8479318,
      "firstName": { "default": "Auston" },
      "lastName": { "default": "Matthews" },
      "positionCode": "C",
      "sweaterNumber": 34
    }
  ]
}
```

---

## Game ID Format

```
SSSSTTGGGG
│   │││└── Game number (0001–1312)
│   │└──── Game type: 01=pre, 02=regular, 03=playoff
│   └───── Unused (always 0)
└───────── Season start year (e.g. 2024 = 2024–25 season)

Example: 2024020442 = Game #442 of the 2024-25 regular season
```

---

## Direct Client Usage

```python
from sportly.nhl._client import NHLClient
from sportly.client import SportlyClient

# With a custom client (e.g. for testing)
http = SportlyClient()
nhl = NHLClient(client=http)

teams = nhl.teams()
box   = nhl.game("2024020001")
pbp   = nhl.play_by_play("2024020001")
```

---

## Error Handling

```python
from sportly.exceptions import NotFoundError, RateLimitError

try:
    box = nhl.game("9999999999")
except NotFoundError:
    print("Game not found")
except RateLimitError:
    print("Rate limited — back off and retry")
```

---

## Related Resources

- [NHL API unofficial docs](https://github.com/Zmalski/NHL-API-Reference)
- [NHL Stats API (legacy)](https://statsapi.web.nhl.com/api/v1) — deprecated, use api-web.nhle.com
- [sportly.espn.hockey](../espn/hockey.md) — ESPN NHL wrapper (fewer fields, 17-sport consistency)

---

*Part of [sportly](https://github.com/pseudo-r/sportly) · MIT License*
