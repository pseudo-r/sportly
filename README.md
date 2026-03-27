# sportly

> Python SDK for ESPN and NHL sports data — batteries-included.

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
```

Requires Python 3.12+.

---

## Quick Start

```python
from sportly.espn import basketball, football, soccer, hockey

# NBA teams
teams = basketball.teams("nba")

# Today's NBA scoreboard
games = basketball.scoreboard("nba")

# EPL standings
table = soccer.standings("eng.1")

# NFL injury report
injuries = football.injuries("nfl")

# NHL schedule (native NHL API)
from sportly import nhl
today = nhl.schedule()
```

### CLI

```bash
sportly info
sportly espn basketball teams --league nba
sportly espn football scoreboard --league nfl
sportly espn soccer standings --league eng.1
sportly nhl teams
sportly nhl schedule --date 2024-04-15
```

---

## Sports Coverage

17 sports · 139+ leagues · 6 ESPN API domains

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
| `nhl` (native) | — | Official NHL Web API |

---

## Available Methods (per sport module)

| Method | Description |
|--------|-------------|
| `teams(league)` | All teams |
| `team(id, league)` | Single team |
| `roster(team_id, league)` | Team roster |
| `scoreboard(league, date)` | Live scores / schedule |
| `game(id, league)` | Game summary |
| `news(league, limit)` | Latest news |
| `standings(league, season)` | League table |
| `rankings(league)` | Poll rankings (college) |
| `injuries(league)` | Injury report |
| `transactions(league)` | Signings / trades |
| `leaders(league, season)` | Statistical leaders |
| `athlete(id, league)` | Athlete profile |
| `athlete_overview(id, league)` | Stats snapshot + next game |
| `athlete_stats(id, league)` | Season statistics |
| `athlete_gamelog(id, league)` | Game-by-game log |
| `athlete_splits(id, league)` | Home/away/opponent splits |
| `stats_leaders(league, category)` | Stats leaderboard |
| `odds(event_id, league)` | Betting odds |
| `play_by_play(event_id, league)` | Play-by-play |
| `win_probability(event_id, league)` | Win probability |
| `cdn_game(game_id)` | Full CDN game package |
| `now_news(limit, league)` | Real-time ESPN news |

---

## ESPN API Domains

| Domain | Use |
|--------|-----|
| `site.api.espn.com/apis/site/v2/` | Scores, teams, news, injuries, transactions |
| `site.api.espn.com/apis/v2/` | Standings (site/v2 returns a stub) |
| `sports.core.api.espn.com/v2/` | Athletes, stats, odds, play-by-play |
| `site.web.api.espn.com/apis/common/v3/` | Athlete stats, gamelog, splits |
| `cdn.espn.com/core/` | Full game packages (xhr=1) |
| `now.core.api.espn.com/v1/` | Real-time news feed |

> **Disclaimer:** This SDK uses undocumented public ESPN APIs. Not affiliated with ESPN. Use responsibly.

---

## Documentation

See [`docs/`](docs/) for sport-specific reference docs:

- [ESPN Overview](docs/espn/index.md)
- [Basketball](docs/espn/basketball.md) • [Football](docs/espn/football.md) • [Soccer](docs/espn/soccer.md)
- [Hockey](docs/espn/hockey.md) • [Baseball](docs/espn/baseball.md) • [Cricket](docs/espn/cricket.md)
- [Tennis](docs/espn/tennis.md) • [Golf](docs/espn/golf.md) • [MMA](docs/espn/mma.md)
- [Racing](docs/espn/racing.md) • [Lacrosse](docs/espn/lacrosse.md) • [Rugby](docs/espn/rugby.md)
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

*Last updated: March 2026 · 17 sports · 139+ leagues · 6 ESPN API domains*
