# Changelog

All notable changes to **sportly** will be documented here.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)  
Versioning: [Semantic Versioning](https://semver.org/)

---

## [Unreleased]

---

## [1.1.1] — 2026-03-27

### Added
- **`sportly.nhl.endpoints`** subpackage — `games` (boxscore, play_by_play, landing), `schedule` (schedule, weekly), `teams` (franchises, roster, standings, player)
- **`sportly.nhl`** public API expanded from 2 functions to 9: `game()`, `play_by_play()`, `landing()`, `roster()`, `standings()`, `player()`, `weekly()`
- **`FUNDING.yml`** — GitHub Sponsors button (Buy Me a Coffee, GitHub Sponsors, PayPal)
- `ruff.toml` — centralised lint config with `per-file-ignores` for test helpers

### Fixed
- Ruff violations across all modules: `SIM108` (cli.py), `SIM105` (espn/_parse.py), `B905` (nba/_client.py), `F401` (fotmob, mlb, nba `__init__`), `ARG005` / `E741` in test files

### Changed
- `publish.yml` upgraded to PyPI **OIDC Trusted Publishing** — no `PYPI_API_TOKEN` secret required
- Repository "About" description and topics updated to reflect all 8 sources

---

## [1.1.0] — 2026-03-26

### Added

#### New Data Sources
- **`sportly.mlb`** — MLB Stats API (`statsapi.mlb.com/api/v1`)
  - `teams()`, `team()`, `roster()`, `team_stats()`
  - `schedule()`, `game_schedule()` with `hydrate=` param support
  - `player()`, `player_stats()`, `player_gamelog()`, `search()`
  - `boxscore()`, `linescore()`, `play_by_play()`, `live_feed()`, `win_probability()`, `decisions()`, `game_content()`
  - `standings()`, `leaders()`, `transactions()`, `venues()`, `draft()`
  - `TEAM_IDS` (30 teams), `SPORT_ID`, `LEAGUE_AL`, `LEAGUE_NL`
- **`sportly.nba`** — NBA Stats API (`stats.nba.com`)
  - WAF headers injected automatically (Origin, Referer, x-nba-stats-*)
  - `parse_result_sets()`: converts NBA rows-as-arrays → dicts
  - `scoreboard()`, `boxscore()`, `play_by_play()`, `win_probability()`
  - `teams()`, `team_stats()`, `roster()`
  - `player()`, `career_stats()`, `game_log()`, `shot_chart()`
  - `standings()`, `leaders()`, `draft()`
  - `TEAM_IDS` (30 teams), `PLAYER_IDS` (10 notable players)
- **`sportly.nfl`** — NFL via ESPN public infrastructure (no OAuth required)
  - `scoreboard()` with `week=`, `season=`, `season_type=` params
  - `teams()`, `team()`, `roster()`, `team_schedule()`, `depth_chart()`
  - `athlete()`, `athlete_stats()`, `athlete_gamelog()`, `athlete_news()`
  - `standings()`, `injuries()`, `transactions()`, `news()`, `play_by_play()`, `odds()`
  - `qbr()` — ESPN QBR leaderboard
  - `TEAM_IDS` (32 teams, ESPN IDs)
- **`sportly.fantasy`** — ESPN Fantasy API v3 (`lm-api-reads.fantasy.espn.com`)
  - Public leagues: no auth. Private leagues: cookie auth (`espn_s2` + `SWID`)
  - `league()` with arbitrary view combinations
  - `teams()`, `roster()`, `standings()`, `draft()`
  - `live_scoring()`, `transactions()`, `players()`, `game_meta()`, `season_meta()`
  - `GAME_CODES`: `ffl`, `fba`, `flb`, `fhl`
- **`sportly.fotmob`** — FotMob web API (`fotmob.com/api`)
  - `matches()`, `match()`, `league()`, `team()`, `player()`, `search()`
  - `all_leagues()`, `tv_listings()`, `world_news()`, `transfers()`
  - `LEAGUES`: 23 popular league IDs including CL (42), PL (47), BL (54)
- **`sportly.sofascore`** — Sofascore API (`api.sofascore.com/api/v1`)
  - Requires `pip install sportly[sofascore]` (adds `curl_cffi` for TLS bypass)
  - `matches()`, `match()`, `match_stats()`, `lineups()`, `incidents()`, `momentum()`
  - `player()`, `player_seasons()`, `team()`, `squad()`
  - `tournaments()`, `popular()`
  - `SPORTS` aliases: `soccer → football`, `hockey → ice-hockey`

#### CLI Expansion (`sportly <cmd>`)
- `sportly mlb schedule|teams|team|roster|player|boxscore|standings|leaders|transactions`
- `sportly nba scoreboard|teams|player|career|leaders|standings|shot-chart`
- `sportly nfl scoreboard|teams|team|injuries|news|standings|play-by-play|depth-chart|qbr`
- `sportly fotmob matches|match|league|team|player|search|leagues`
- `sportly info` now lists all 8 sources

#### Packaging
- `pyproject.toml`: `sofascore` and `all` optional extras (`curl_cffi>=0.6`)
- Expanded `keywords` to include nba, mlb, nfl, fotmob, sofascore

#### Docs
- `docs/mlb/README.md` — full endpoint reference, team IDs, hydrate examples
- `docs/nba/README.md` — WAF headers, resultSets shape, shot chart guide
- `docs/nfl/README.md` — ESPN domains used, QBR, native NFL API note
- `docs/fantasy/README.md` — auth guide, all 14 views documented
- `docs/fotmob/README.md` — league ID table, match response shape, ID discovery
- `docs/sofascore/README.md` — curl_cffi install, sports slugs, endpoint ref

#### CI/CD
- `ci.yml`: fixed branch trigger `main → master`, replaced missing docker job with lint job
- `publish.yml`: new PyPI release workflow (triggered on GitHub Release)

### Tests
- 104 tests total (all mocked, no network required)
- Added: `test_mlb.py` (18), `test_nba.py` (13), `test_nfl.py` (5), `test_fantasy.py` (6), `test_fotmob.py` (7), `test_sofascore.py` (10)

---

## [1.0.0] — 2026-03-26

### Added
- Pure Python SDK — `pip install sportly`, no web framework required
- **17 ESPN sport modules**: basketball, football, soccer, hockey, baseball, cricket,
  tennis, golf, mma, racing, lacrosse, volleyball, water polo, field hockey, rugby,
  rugby league, australian football
- **6 ESPN API domains** covered: site v2, standalone v2 (standings), core v2,
  web/common v3, CDN, Now
- Common methods per sport: `teams`, `team`, `roster`, `scoreboard`, `game`,
  `news`, `standings`, `rankings`, `injuries`, `transactions`, `leaders`
- Athlete methods: `athlete`, `athlete_overview`, `athlete_stats`, `athlete_gamelog`,
  `athlete_splits`, `stats_leaders`
- Advanced methods: `odds`, `play_by_play`, `win_probability`, `cdn_game`, `now_news`
- Native NHL Web API client (`sportly.nhl`)
- Pydantic v2 models: `Team`, `Game`, `Article`, `Standings`, `Athlete`
- CLI: `sportly info`, `sportly espn <sport> <method>`, `sportly nhl <cmd>`
- Full test suite (mocked, no network required)
- GitHub Actions CI (Python 3.12 + 3.13)
- Per-sport documentation in `docs/espn/`
