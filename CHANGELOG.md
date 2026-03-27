# Changelog

All notable changes to **sportly** will be documented here.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)  
Versioning: [Semantic Versioning](https://semver.org/)

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
- Native NHL Web API client (`sportly.nhl`): `teams`, `schedule`, `game`, `play_by_play`
- Pydantic v2 models: `Team`, `Game`, `Article`, `Standings`, `Athlete`
- CLI: `sportly info`, `sportly espn <sport> <method>`, `sportly nhl <cmd>`
- Full test suite (mocked, no network required)
- GitHub Actions CI (Python 3.12 + 3.13, ruff, pytest, Docker)
- Dockerfile (non-root, minimal, CLI entrypoint)
- Per-sport documentation in `docs/espn/`
