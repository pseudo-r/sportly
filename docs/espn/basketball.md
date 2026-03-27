# 🏀 Basketball

> Basketball from the NBA, WNBA, college, and international leagues (FIBA, NBL).

**Sport slug:** `basketball`  
**Base URL (v2):** `https://sports.core.api.espn.com/v2/sports/basketball/`  
**Base URL (v3):** `https://sports.core.api.espn.com/v3/sports/basketball/`

---

## Leagues & Competitions

| Abbreviation | League Name | Slug | Full URL |
| --- | --- | --- | --- |
| `FIBA` | FIBA World Cup | `fiba` | `https://sports.core.api.espn.com/v2/sports/basketball/leagues/fiba` |
| `NCAAM` | NCAA Men's Basketball | `mens-college-basketball` | `https://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball` |
| `OLYMPICS` | Olympics Men's Basketball | `mens-olympics-basketball` | `https://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-olympics-basketball` |
| `NBA` | National Basketball Association | `nba` | `https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba` |
| `NBA G LEAGUE` | NBA G League | `nba-development` | `https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba-development` |
| `NBACC` | NBA California Classic Summer League | `nba-summer-california` | `https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba-summer-california` |
| `NBAGS` | Golden State Summer League | `nba-summer-golden-state` | `https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba-summer-golden-state` |
| `NBALV` | Las Vegas Summer League | `nba-summer-las-vegas` | `https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba-summer-las-vegas` |
| `NBAOR` | Orlando Summer League | `nba-summer-orlando` | `https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba-summer-orlando` |
| `NBAGS` | Sacramento Summer League | `nba-summer-sacramento` | `https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba-summer-sacramento` |
| `NBAUT` | Salt Lake City Summer League | `nba-summer-utah` | `https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba-summer-utah` |
| `NBL` | National Basketball League | `nbl` | `https://sports.core.api.espn.com/v2/sports/basketball/leagues/nbl` |
| `WNBA` | Women's National Basketball Association | `wnba` | `https://sports.core.api.espn.com/v2/sports/basketball/leagues/wnba` |
| `NCAAW` | NCAA Women's Basketball | `womens-college-basketball` | `https://sports.core.api.espn.com/v2/sports/basketball/leagues/womens-college-basketball` |
| `OLYMPICS` | Olympics Women's Basketball | `womens-olympics-basketball` | `https://sports.core.api.espn.com/v2/sports/basketball/leagues/womens-olympics-basketball` |

---

## API Endpoints

> All endpoints below follow the pattern:  
> `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}<sub-path>`  
> Replace `{league}` with a league slug from the table above.

### Common Query Parameters

Most list endpoints support: `page` (int), `limit` (int). Additional filters are documented per endpoint.

### Seasons & Calendar

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/calendar` | `getCalendars` | `dates`, `page`, `limit`, `dates`, `groups`, `smartdates`, `advance`, `utcOffset`, `weeks`, `seasontype` |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/seasons` | `getSeasons` | `page`, `limit`, `utcOffset`, `dates`, `start`, `end`, `eventsback`, `eventsforward`, `eventsrange`, `eventcompleted`, `groups`, `profile`, `competitions.types`, `types`, `season`, `weeks`, `tournamentId`, `dates`, `sort`, `type`, `date`, `group`, `position`, `week`, `qualified`, `types`, `limit`, `page`, `sort`, `position`, `status`, `sort`, `sortByRanks`, `stats`, `groupId`, `position`, `qualified`, `rookie`, `international`, `category`, `type`, `sort`, `sortByRanks`, `stats`, `groupId`, `qualified`, `category`, `sort`, `groupId`, `allStar`, `group`, `gender`, `types`, `country`, `association`, `lastNameInitial`, `lastName`, `active`, `statuses`, `sort`, `position`, `dates`, `groups`, `smartdates`, `advance`, `utcOffset`, `weeks`, `seasontype` |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/seasons/{season}/athletes` | `getAthletes` | `active`, `sort`, `page`, `limit`, `seasontypes`, `played`, `teamtypes`, `group`, `gender`, `types`, `country`, `association`, `lastNameInitial`, `lastName`, `active`, `statuses`, `sort`, `position` |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/seasons/{season}/draft` | `getDraftByYear` | `page`, `limit`, `available`, `position`, `team`, `sort`, `filter` |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/seasons/{season}/freeagents` | `getFreeAgents` | `page`, `limit`, `types`, `oldteams`, `newteams`, `position`, `sort` |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/seasons/{season}/manufacturers` | `getManufacturers` | `page`, `limit` |

### Teams

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/teams` | `getTeams` | `page`, `limit`, `utcOffset`, `dates`, `start`, `end`, `eventsback`, `eventsforward`, `eventsrange`, `eventcompleted`, `groups`, `profile`, `competitions.types`, `types`, `season`, `weeks`, `tournamentId`, `active`, `national`, `start`, `group`, `dates`, `recent`, `types`, `winnertype`, `date`, `eventsback`, `excludestatuses`, `includestatuses`, `dates`, `groups`, `smartdates`, `advance`, `utcOffset`, `weeks`, `seasontype` |

### Athletes / Players

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/athletes` | `getAthletes` | `page`, `limit`, `group`, `gender`, `types`, `country`, `association`, `lastNameInitial`, `lastName`, `active`, `statuses`, `sort`, `position` |

### Events / Games

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/events/{event}` | `getEvent` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/events/{event}/competitions/{competition}` | `getCompetition` | `page`, `limit`, `date`, `group`, `position`, `week`, `qualified`, `types`, `limit`, `page`, `types`, `period`, `sort`, `source`, `showsubplays` |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/events/{event}/competitions/{competition}/broadcasts` | `getBroadcasts` | `lang`, `region`, `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/events/{event}/competitions/{competition}/competitors/{competitor}` | `getCompetitor` | `page`, `limit`, `date`, `group`, `position`, `week`, `qualified`, `types`, `limit`, `page` |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/events/{event}/competitions/{competition}/odds` | `getCompetitionOdds` | `provider.priority`, `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/events/{event}/competitions/{competition}/officials` | `getOfficials` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/events/{event}/competitions/{competition}/plays/{play}/personnel` | `getPersonnel` | `page`, `limit` |

### News & Media

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/media` | `getMedia` | `page`, `limit` |

### Rankings & Awards

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/rankings` | `getRankings` | `page`, `limit` |

### Venues

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/venues` | `getVenues` | `page`, `limit` |

### Other

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/casinos` | `getCasinos` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/circuits` | `getCircuits` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/countries` | `getCountries` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/franchises` | `getFranchises` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/positions` | `getPositions` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/providers` | `getProviders` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/recruiting` | `getRecruitingSeasons` | `page`, `limit`, `sort`, `position`, `status` |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/season` | `getCurrentSeason` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/basketball/leagues/{league}/tournaments` | `getTournaments` | `majorsOnly`, `page`, `limit` |

---

## V3 Endpoints

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v3/sports/{sport}/athletes` | `getAthletes` | `page`, `limit`, `_hoist`, `_help`, `_trace`, `_nocache`, `enable`, `disable`, `pq`, `q`, `page`, `limit`, `lang`, `region`, `utcOffset`, `dates`, `weeks`, `advance`, `event.recurring`, `ids`, `type`, `types`, `seasontypes`, `calendar.type`, `calendar.groups`, `status`, `statuses`, `groups`, `provider`, `provider.priority`, `site`, `league.type`, `split`, `splits`, `record.splits`, `record.seasontype`, `statistic.splits`, `statistic.seasontype`, `statistic.qualified`, `statistic.context`, `sort`, `roster.positions`, `roster.athletes`, `team.athletes`, `powerindex.rundatetimekey`, `eventsback`, `eventsforward`, `eventsrange`, `eventstates`, `eventresults`, `seek`, `tournaments`, `competitions`, `competition.types`, `teams`, `situation.play`, `oldteams`, `newteams`, `played`, `period`, `position`, `filter`, `available`, `active`, `ids.sportware`, `profile`, `opponent`, `eventId`, `homeAway`, `season`, `athlete.position`, `postalCode`, `award.type`, `notes.type`, `tidbit.type`, `networks`, `bets.promotion`, `guids`, `competitors`, `source` |
| `https://sports.core.api.espn.com/v3/sports/{sport}/{league}` | `getLeague` | `page`, `limit`, `_hoist`, `_help`, `_trace`, `_nocache`, `enable`, `disable`, `pq`, `q`, `page`, `limit`, `lang`, `region`, `utcOffset`, `dates`, `weeks`, `advance`, `event.recurring`, `ids`, `type`, `types`, `seasontypes`, `calendar.type`, `calendar.groups`, `status`, `statuses`, `groups`, `provider`, `provider.priority`, `site`, `league.type`, `split`, `splits`, `record.splits`, `record.seasontype`, `statistic.splits`, `statistic.seasontype`, `statistic.qualified`, `statistic.context`, `sort`, `roster.positions`, `roster.athletes`, `team.athletes`, `powerindex.rundatetimekey`, `eventsback`, `eventsforward`, `eventsrange`, `eventstates`, `eventresults`, `seek`, `tournaments`, `competitions`, `competition.types`, `teams`, `situation.play`, `oldteams`, `newteams`, `played`, `period`, `position`, `filter`, `available`, `active`, `ids.sportware`, `profile`, `opponent`, `eventId`, `homeAway`, `season`, `athlete.position`, `postalCode`, `award.type`, `notes.type`, `tidbit.type`, `networks`, `bets.promotion`, `guids`, `competitors`, `source` |
| `https://sports.core.api.espn.com/v3/sports/{sport}/{league}/seasons/{season}` | `getSeason` | `page`, `limit`, `_hoist`, `_help`, `_trace`, `_nocache`, `enable`, `disable`, `pq`, `q`, `page`, `limit`, `lang`, `region`, `utcOffset`, `dates`, `weeks`, `advance`, `event.recurring`, `ids`, `type`, `types`, `seasontypes`, `calendar.type`, `calendar.groups`, `status`, `statuses`, `groups`, `provider`, `provider.priority`, `site`, `league.type`, `split`, `splits`, `record.splits`, `record.seasontype`, `statistic.splits`, `statistic.seasontype`, `statistic.qualified`, `statistic.context`, `sort`, `roster.positions`, `roster.athletes`, `team.athletes`, `powerindex.rundatetimekey`, `eventsback`, `eventsforward`, `eventsrange`, `eventstates`, `eventresults`, `seek`, `tournaments`, `competitions`, `competition.types`, `teams`, `situation.play`, `oldteams`, `newteams`, `played`, `period`, `position`, `filter`, `available`, `active`, `ids.sportware`, `profile`, `opponent`, `eventId`, `homeAway`, `season`, `athlete.position`, `postalCode`, `award.type`, `notes.type`, `tidbit.type`, `networks`, `bets.promotion`, `guids`, `competitors`, `source` |

---

## Site API Endpoints

> These use `site.api.espn.com` and return user-friendly data (scores, rosters, news, etc.)

```
GET https://site.api.espn.com/apis/site/v2/sports/basketball/{league}/{resource}
```

| Resource | Description |
|----------|-------------|
| `scoreboard` | Live scores & schedules |
| `scoreboard?dates={YYYYMMDD}` | Scores for a specific date |
| `teams` | All teams |
| `teams/{id}` | Single team |
| `teams/{id}/roster` | Team roster |
| `teams/{id}/schedule` | Team schedule |
| `teams/{id}/record` | Team record |
| `teams/{id}/news` | Team news |
| `teams/{id}/injuries` | Team injury report |
| `teams/{id}/leaders` | Team statistical leaders |
| `teams/{id}/depth-charts` | Depth charts |
| `injuries` | **League-wide** injury report (all teams) |
| `transactions` | Recent signings, trades, waivers |
| `statistics` | League statistical leaders |
| `groups` | Conferences and divisions |
| `draft` | Draft board (NBA only) |
| `standings` | ⚠️ Stub only — see note below |
| `news` | Latest news |
| `athletes/{id}/news` | Athlete-specific news |
| `summary?event={id}` | Full game summary + boxscore |
| `rankings` | Poll rankings (NCAA leagues only) |

> ⚠️ **Standings Note:** The `/apis/site/v2/` path returns only a stub for standings. Use `/apis/v2/` instead:
> `https://site.api.espn.com/apis/v2/sports/basketball/{league}/standings`

---

## CDN Game Data

> Rich game packages via `cdn.espn.com`. Requires `?xhr=1`. Returns a `gamepackageJSON` object containing drives, plays, win probability, scoring, and odds.

```bash
# Full game package
curl "https://cdn.espn.com/core/nba/game?xhr=1&gameId={EVENT_ID}"

# Specific views
curl "https://cdn.espn.com/core/nba/boxscore?xhr=1&gameId={EVENT_ID}"
curl "https://cdn.espn.com/core/nba/playbyplay?xhr=1&gameId={EVENT_ID}"
curl "https://cdn.espn.com/core/nba/matchup?xhr=1&gameId={EVENT_ID}"
curl "https://cdn.espn.com/core/nba/scoreboard?xhr=1"
```

---

## Athlete Data (common/v3)

> Individual player stats, game logs, splits, and overview via `site.web.api.espn.com`.

```bash
# Player overview (stats snapshot + next game + rotowire)
curl "https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/{id}/overview"

# Season stats
curl "https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/{id}/stats"

# Game log
curl "https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/{id}/gamelog"

# Home/Away/Opponent splits
curl "https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/{id}/splits"

# Stats leaderboard (all athletes ranked)
curl "https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/statistics/byathlete"
```

> ✅ Works for: NBA, WNBA, mens-college-basketball, womens-college-basketball

---

## Specialized Endpoints

### Bracketology (NCAA Tournament)

```bash
# Live bracket projections
GET https://sports.core.api.espn.com/v2/tournament/{tournamentId}/seasons/{year}/bracketology

# Bracket snapshot at a specific iteration
GET https://sports.core.api.espn.com/v2/tournament/{tournamentId}/seasons/{year}/bracketology/{iteration}
```

> Common tournament IDs: `22` = NCAA Men's, `23` = NCAA Women's

### Power Index (BPI)

```bash
# Season BPI ratings
GET https://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/seasons/{year}/powerindex

# BPI leaders
GET https://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/seasons/{year}/powerindex/leaders

# BPI by team
GET https://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/seasons/{year}/powerindex/{teamId}
```

---

## Example API Calls

```bash
# NBA scoreboard (today)
curl "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard"

# NBA scoreboard for a specific date
curl "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/scoreboard?dates=20250320"

# NBA standings (use /apis/v2/ — /apis/site/v2/ only returns a stub)
curl "https://site.api.espn.com/apis/v2/sports/basketball/nba/standings"

# LA Lakers roster
curl "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/13/roster"

# LA Lakers injury report
curl "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/13/injuries"

# Men's College Basketball scoreboard
curl "https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/scoreboard?dates=20250320-20250323"

# Get all basketball leagues (core API)
curl "https://sports.core.api.espn.com/v2/sports/basketball/leagues"

# NBA teams (core API)
curl "https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/teams?limit=50"

# NBA athletes (core API)
curl "https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/athletes?limit=100&active=true"

# NBA standings (core API)
curl "https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/standings"

# WNBA teams
curl "https://sports.core.api.espn.com/v2/sports/basketball/leagues/wnba/teams"

# FIBA World Cup teams
curl "https://sports.core.api.espn.com/v2/sports/basketball/leagues/fiba/teams"
```
