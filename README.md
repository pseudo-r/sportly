# sportly

> Python SDK for multi-source sports data — ESPN, MLB, NBA, NFL, FotMob, Sofascore, ESPN Fantasy, and NHL.

[![PyPI version](https://badge.fury.io/py/sportly.svg)](https://badge.fury.io/py/sportly)
[![CI](https://github.com/pseudo-r/sportly/actions/workflows/ci.yml/badge.svg)](https://github.com/pseudo-r/sportly/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

---

## ☕ Support This Project

| Platform | Link |
|----------|------|
| ☕ Buy Me a Coffee | [buymeacoffee.com/pseudo_r](https://buymeacoffee.com/pseudo_r) |
| 💖 GitHub Sponsors | [github.com/sponsors/Kloverdevs](https://github.com/sponsors/Kloverdevs) |
| 💳 PayPal | [PayPal (CAD)](https://www.paypal.com/donate/?business=H5VPFZ2EHVNBU&no_recurring=0&currency_code=CAD) |

---

## 📱 Real-World Apps Built With sportly

| App | Store |
|-----|-------|
| 🏀 [Sportly: Basketball Live](https://play.google.com/store/apps/details?id=com.sportly.basketball) | [![Google Play](https://img.shields.io/badge/Google_Play-Basketball-3DDC84?logo=google-play&logoColor=white)](https://play.google.com/store/apps/details?id=com.sportly.basketball) |
| ⚽ [Sportly: Soccer Live](https://play.google.com/store/apps/details?id=com.sportly.soccer) | [![Google Play](https://img.shields.io/badge/Google_Play-Soccer-3DDC84?logo=google-play&logoColor=white)](https://play.google.com/store/apps/details?id=com.sportly.soccer) |
| 🏒 [Sportly: NHL & Hockey Live](https://play.google.com/store/apps/details?id=com.sportly.hockey) | [![Google Play](https://img.shields.io/badge/Google_Play-Hockey-3DDC84?logo=google-play&logoColor=white)](https://play.google.com/store/apps/details?id=com.sportly.hockey) |
| 🏈 [Sportly: American Football Live](https://play.google.com/store/apps/details?id=com.sportly.football) | [![Google Play](https://img.shields.io/badge/Google_Play-Football-3DDC84?logo=google-play&logoColor=white)](https://play.google.com/store/apps/details?id=com.sportly.football) |
| ⚾ [Sportly: Baseball Live](https://play.google.com/store/apps/details?id=com.sportly.baseball) | [![Google Play](https://img.shields.io/badge/Google_Play-Baseball-3DDC84?logo=google-play&logoColor=white)](https://play.google.com/store/apps/details?id=com.sportly.baseball) |

---

## Install

```bash
pip install sportly

# Include Sofascore support (curl_cffi TLS impersonation)
pip install sportly[sofascore]

# All optional extras
pip install sportly[all]
```

Requires Python 3.12+.

---

## Data Sources

| Module | Source | Auth | Special |
|--------|--------|------|---------|
| `sportly.espn` | ESPN (17 sports, 139+ leagues) | None | 6 ESPN API domains |
| `sportly.nhl` | NHL Web API + NHL Stats REST | None | Official NHL data |
| `sportly.mlb` | MLB Stats API (`statsapi.mlb.com`) | None | `hydrate=` embeds sub-resources |
| `sportly.nba` | NBA Stats API (`stats.nba.com`) | WAF headers (auto-injected) | `resultSets` row-parser built-in |
| `sportly.nfl` | ESPN public NFL infrastructure | None | Wraps existing ESPN domains |
| `sportly.fantasy` | ESPN Fantasy v3 (`lm-api-reads`) | Cookies (private leagues only) | Public leagues need no auth |
| `sportly.fotmob` | FotMob web API | None | xG, shot maps, player ratings |
| `sportly.sofascore` | Sofascore API v1 | `curl_cffi` TLS spoof | `pip install sportly[sofascore]` |

---

## Quick Start

```python
# ── ESPN ──────────────────────────────────────────────────────────────
from sportly.espn import basketball, football, soccer, hockey

# NBA teams
teams = basketball.teams("nba")
# EPL standings
table = soccer.standings("eng.1")
# NHL scores
scores = hockey.scoreboard("nhl")

# ── MLB ───────────────────────────────────────────────────────────────
from sportly import mlb

games  = mlb.schedule()                          # today
ohtani = mlb.player(660271)                      # Shohei Ohtani
hr     = mlb.leaders("homeRuns", season=2025)    # HR leaders
box    = mlb.boxscore(745444)                    # game boxscore

# ── NBA ───────────────────────────────────────────────────────────────
from sportly import nba

sb     = nba.scoreboard("2025-03-26")
shots  = nba.shot_chart("201939", "2024-25")     # Curry
top    = nba.leaders("PTS", season="2024-25")
st     = nba.standings("2024-25")

# ── NFL ───────────────────────────────────────────────────────────────
from sportly import nfl

sb     = nfl.scoreboard(week=1, season=2024)
dc     = nfl.depth_chart("6")                    # Cowboys
inj    = nfl.injuries()
qbr    = nfl.qbr(season=2024)

# ── ESPN Fantasy ──────────────────────────────────────────────────────
from sportly import fantasy

teams  = fantasy.teams("ffl", league_id=336358, season=2025)
draft  = fantasy.draft("ffl", league_id=336358, season=2025)
# Private league:
data   = fantasy.league("ffl", league_id=123456, season=2025,
                         cookies={"espn_s2": "...", "SWID": "{...}"})

# ── FotMob ────────────────────────────────────────────────────────────
from sportly import fotmob

day    = fotmob.matches("20260326")              # today's matches
epl    = fotmob.league(47)                       # Premier League
m      = fotmob.match(4310531)                   # xG, lineups, ratings

# ── Sofascore ─────────────────────────────────────────────────────────
from sportly import sofascore                    # requires pip install sportly[sofascore]

games  = sofascore.matches("football", "2026-03-26")
stats  = sofascore.match_stats(11352523)         # xG, possession
lineup = sofascore.lineups(11352523)

# ── NHL ───────────────────────────────────────────────────────────────
from sportly import nhl

today  = nhl.schedule()
games  = nhl.scoreboard()
roster = nhl.roster("TOR")
```

---

## CLI

```bash
sportly info

# ESPN
sportly espn basketball teams --league nba
sportly espn football scoreboard --league nfl
sportly espn soccer standings --league eng.1

# NHL
sportly nhl teams
sportly nhl schedule --date 2024-04-15
```

---

## ESPN Coverage (17 sports · 139+ leagues)

| Module | Default League | Notable Leagues |
|--------|---------------|-----------------| 
| `espn.basketball` | `nba` | WNBA, NCAA, NBL, FIBA |
| `espn.football` | `nfl` | NCAAF, CFL, XFL, UFL |
| `espn.soccer` | `eng.1` | 260+ leagues worldwide |
| `espn.hockey` | `nhl` | NCAA |
| `espn.baseball` | `mlb` | NCAA, WBC |
| `espn.cricket` | `icc-cricket` | ICC T20/ODI, IPL |
| `espn.tennis` | `atp` | WTA |
| `espn.golf` | `pga` | LPGA, LIV, DP World |
| `espn.mma` | `bellator` | LFA, Cage Warriors |
| `espn.racing` | `f1` | IndyCar, NASCAR |
| `espn.lacrosse` | `pll` | NLL, NCAA |
| `espn.volleyball` | `womens-college-volleyball` | NCAA |
| `espn.water_polo` | `mens-college-water-polo` | NCAA |
| `espn.field_hockey` | `womens-college-field-hockey` | NCAA |
| `espn.rugby` | `180659` (Six Nations) | 24 competitions |
| `espn.rugby_league` | `3` | NRL, Super League |
| `espn.australian_football` | `afl` | AFL |

---

## ESPN Methods (per sport module)

| Method | Description |
|--------|-------------|
| `teams(league)` | All teams |
| `team(id, league)` | Single team |
| `roster(team_id, league)` | Team roster |
| `scoreboard(league, date)` | Live scores / schedule |
| `game(id, league)` | Game summary |
| `news(league, limit)` | Latest news |
| `standings(league, season)` | League table |
| `injuries(league)` | Injury report |
| `transactions(league)` | Signings / trades |
| `athlete(id, league)` | Athlete profile |
| `athlete_stats(id, league)` | Season statistics |
| `athlete_gamelog(id, league)` | Game-by-game log |
| `odds(event_id, league)` | Betting odds |
| `play_by_play(event_id, league)` | Play-by-play |
| `cdn_game(game_id)` | Full CDN game package |

---

## Documentation

- [ESPN Overview](docs/espn/index.md)
- [Basketball](docs/espn/basketball.md) · [Football](docs/espn/football.md) · [Soccer](docs/espn/soccer.md) · [Hockey](docs/espn/hockey.md)
- [MLB](docs/mlb/README.md) · [NBA](docs/nba/README.md) · [NFL](docs/nfl/README.md)
- [ESPN Fantasy](docs/fantasy/README.md) · [FotMob](docs/fotmob/README.md) · [Sofascore](docs/sofascore/README.md)
- [NHL (Native)](docs/nhl.md)

---

## Development

```bash
git clone https://github.com/pseudo-r/sportly
cd sportly
pip install -e .[dev]
pytest
```

## License

MIT — see [LICENSE](LICENSE)

> **Disclaimer:** This SDK uses undocumented public APIs. Not affiliated with ESPN, MLB, NBA, NFL, FotMob, Sofascore, or NHL.

*Last updated: March 2026 · v1.1.0 · 8 sources · 17+ sports · 139+ leagues*
