# 🏈 Football

> American and Canadian football, including the NFL, CFL, College Football, UFL, and XFL.

**Sport slug:** `football`  
**Base URL (v2):** `https://sports.core.api.espn.com/v2/sports/football/`  
**Base URL (v3):** `https://sports.core.api.espn.com/v3/sports/football/`

---

## Leagues & Competitions

| Abbreviation | League Name | Slug | Full URL |
| --- | --- | --- | --- |
| `CFL` | Canadian Football League | `cfl` | `https://sports.core.api.espn.com/v2/sports/football/leagues/cfl` |
| `NCAAF` | NCAA - Football | `college-football` | `https://sports.core.api.espn.com/v2/sports/football/leagues/college-football` |
| `NFL` | National Football League | `nfl` | `https://sports.core.api.espn.com/v2/sports/football/leagues/nfl` |
| `UFL` | United Football League | `ufl` | `https://sports.core.api.espn.com/v2/sports/football/leagues/ufl` |
| `XFL` | XFL | `xfl` | `https://sports.core.api.espn.com/v2/sports/football/leagues/xfl` |

---

## API Endpoints

> All endpoints below follow the pattern:  
> `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}<sub-path>`  
> Replace `{league}` with a league slug from the table above.

### Common Query Parameters

Most list endpoints support: `page` (int), `limit` (int). Additional filters are documented per endpoint.

### Seasons & Calendar

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/calendar` | `getCalendars` | `dates`, `page`, `limit`, `dates`, `groups`, `smartdates`, `advance`, `utcOffset`, `weeks`, `seasontype` |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/seasons` | `getSeasons` | `page`, `limit`, `utcOffset`, `dates`, `start`, `end`, `eventsback`, `eventsforward`, `eventsrange`, `eventcompleted`, `groups`, `profile`, `competitions.types`, `types`, `season`, `weeks`, `tournamentId`, `dates`, `sort`, `type`, `date`, `group`, `position`, `week`, `qualified`, `types`, `limit`, `page`, `sort`, `position`, `status`, `sort`, `sortByRanks`, `stats`, `groupId`, `position`, `qualified`, `rookie`, `international`, `category`, `type`, `sort`, `sortByRanks`, `stats`, `groupId`, `qualified`, `category`, `sort`, `groupId`, `allStar`, `group`, `gender`, `types`, `country`, `association`, `lastNameInitial`, `lastName`, `active`, `statuses`, `sort`, `position`, `dates`, `groups`, `smartdates`, `advance`, `utcOffset`, `weeks`, `seasontype` |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/seasons/{season}/athletes` | `getAthletes` | `active`, `sort`, `page`, `limit`, `seasontypes`, `played`, `teamtypes`, `group`, `gender`, `types`, `country`, `association`, `lastNameInitial`, `lastName`, `active`, `statuses`, `sort`, `position` |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/seasons/{season}/draft` | `getDraftByYear` | `page`, `limit`, `available`, `position`, `team`, `sort`, `filter` |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/seasons/{season}/freeagents` | `getFreeAgents` | `page`, `limit`, `types`, `oldteams`, `newteams`, `position`, `sort` |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/seasons/{season}/manufacturers` | `getManufacturers` | `page`, `limit` |

### Teams

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/teams` | `getTeams` | `page`, `limit`, `utcOffset`, `dates`, `start`, `end`, `eventsback`, `eventsforward`, `eventsrange`, `eventcompleted`, `groups`, `profile`, `competitions.types`, `types`, `season`, `weeks`, `tournamentId`, `active`, `national`, `start`, `group`, `dates`, `recent`, `types`, `winnertype`, `date`, `eventsback`, `excludestatuses`, `includestatuses`, `dates`, `groups`, `smartdates`, `advance`, `utcOffset`, `weeks`, `seasontype` |

### Athletes / Players

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/athletes` | `getAthletes` | `page`, `limit`, `group`, `gender`, `types`, `country`, `association`, `lastNameInitial`, `lastName`, `active`, `statuses`, `sort`, `position` |

### Events / Games

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/events/{event}` | `getEvent` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/events/{event}/competitions/{competition}` | `getCompetition` | `page`, `limit`, `date`, `group`, `position`, `week`, `qualified`, `types`, `limit`, `page`, `types`, `period`, `sort`, `source`, `showsubplays` |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/events/{event}/competitions/{competition}/broadcasts` | `getBroadcasts` | `lang`, `region`, `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/events/{event}/competitions/{competition}/competitors/{competitor}` | `getCompetitor` | `page`, `limit`, `date`, `group`, `position`, `week`, `qualified`, `types`, `limit`, `page` |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/events/{event}/competitions/{competition}/odds` | `getCompetitionOdds` | `provider.priority`, `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/events/{event}/competitions/{competition}/officials` | `getOfficials` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/events/{event}/competitions/{competition}/plays/{play}/personnel` | `getPersonnel` | `page`, `limit` |

### News & Media

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/media` | `getMedia` | `page`, `limit` |

### Rankings & Awards

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/rankings` | `getRankings` | `page`, `limit` |

### Venues

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/venues` | `getVenues` | `page`, `limit` |

### Other

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/casinos` | `getCasinos` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/circuits` | `getCircuits` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/countries` | `getCountries` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/franchises` | `getFranchises` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/positions` | `getPositions` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/providers` | `getProviders` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/recruiting` | `getRecruitingSeasons` | `page`, `limit`, `sort`, `position`, `status` |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/season` | `getCurrentSeason` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/football/leagues/{league}/tournaments` | `getTournaments` | `majorsOnly`, `page`, `limit` |

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
GET https://site.api.espn.com/apis/site/v2/sports/football/{league}/{resource}
```

| Resource | Description |
|----------|-------------|
| `scoreboard` | Live scores & schedules |
| `scoreboard?week={n}&seasontype=2` | Scores for a specific week |
| `scoreboard?dates={YYYYMMDD}` | Scores for a specific date |
| `teams` | All teams |
| `teams/{id}` | Single team |
| `teams/{id}/roster` | Team roster |
| `teams/{id}/schedule` | Team schedule |
| `teams/{id}/record` | Team record |
| `teams/{id}/news` | Team news |
| `teams/{id}/depthcharts` | Depth charts |
| `teams/{id}/injuries` | Team injury report |
| `teams/{id}/leaders` | Team statistical leaders |
| `injuries` | **League-wide** injury report (all teams) |
| `transactions` | Recent signings, trades, waivers |
| `statistics` | League statistical leaders |
| `groups` | Conferences and divisions |
| `draft` | Draft board (NFL only) |
| `standings` | ⚠️ Stub only — see note below |
| `news` | Latest news |
| `athletes/{id}/news` | Athlete-specific news |
| `summary?event={id}` | Full game summary + boxscore |
| `rankings` | Poll rankings (college-football only) |

> ⚠️ **Standings Note:** The `/apis/site/v2/` path returns only a stub for standings. Use `/apis/v2/` instead:
> `https://site.api.espn.com/apis/v2/sports/football/{league}/standings`

---

## CDN Game Data

> Rich game packages via `cdn.espn.com`. Requires `?xhr=1`. Contains drives, play-by-play, win probability, scoring, and odds inside `gamepackageJSON`.

```bash
# NFL — full game package
curl "https://cdn.espn.com/core/nfl/game?xhr=1&gameId={EVENT_ID}"

# College football
curl "https://cdn.espn.com/core/college-football/game?xhr=1&gameId={EVENT_ID}"

# Specific views (nfl or college-football)
curl "https://cdn.espn.com/core/nfl/boxscore?xhr=1&gameId={EVENT_ID}"
curl "https://cdn.espn.com/core/nfl/playbyplay?xhr=1&gameId={EVENT_ID}"
curl "https://cdn.espn.com/core/nfl/matchup?xhr=1&gameId={EVENT_ID}"
curl "https://cdn.espn.com/core/nfl/scoreboard?xhr=1"
```

---

## Athlete Data (common/v3)

> Individual player stats, game logs, and splits via `site.web.api.espn.com`. Works for NFL; also applies to college-football.

```bash
# Player overview (stats + next game + rotowire notes)
curl "https://site.web.api.espn.com/apis/common/v3/sports/football/nfl/athletes/{id}/overview"

# Season stats
curl "https://site.web.api.espn.com/apis/common/v3/sports/football/nfl/athletes/{id}/stats"

# Game log
curl "https://site.web.api.espn.com/apis/common/v3/sports/football/nfl/athletes/{id}/gamelog"

# Home/Away/Opponent splits
curl "https://site.web.api.espn.com/apis/common/v3/sports/football/nfl/athletes/{id}/splits"

# Stats leaderboard (all athletes ranked)
curl "https://site.web.api.espn.com/apis/common/v3/sports/football/nfl/statistics/byathlete"
```

---

## Specialized Endpoints

### QBR (Total Quarterback Rating)

```bash
# Season totals QBR (NFL)
GET https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{year}/types/2/groups/1/qbr/0

# Weekly QBR (NFL)
GET https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/{year}/types/2/weeks/{week}/qbr/0

# College Football QBR (NCAAF)
GET https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/{year}/types/2/groups/80/qbr/0
```

> **Split values:** `0` = totals, `1` = home, `2` = away

### Recruiting

```bash
# Top recruiting class by year (NCAAF)
GET https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/{year}/recruits

# Recruiting class by team
GET https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/{year}/classes/{teamId}
```

### Power Index (SP+)

```bash
# Season SP+ ratings
GET https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/{year}/powerindex

# SP+ leaders
GET https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/{year}/powerindex/leaders
```

---

## Example API Calls

```bash
# NFL scoreboard (all games this week)
curl "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"

# NFL Week 1 scores
curl "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?week=1&seasontype=2"

# NFL standings (use /apis/v2/ — /apis/site/v2/ only returns a stub)
curl "https://site.api.espn.com/apis/v2/sports/football/nfl/standings"

# Dallas Cowboys roster
curl "https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/6/roster"

# Dallas Cowboys depth chart
curl "https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/6/depthcharts"

# Dallas Cowboys injury report
curl "https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/6/injuries"

# College Football scoreboard
curl "https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?week=1&seasontype=2&groups=80"

# Get all NFL leagues
curl "https://sports.core.api.espn.com/v2/sports/football/leagues"

# NFL teams (core API)
curl "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/teams?limit=50"

# NFL current season events
curl "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/events"

# NFL athletes (core API)
curl "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/athletes?limit=100&active=true"

# NFL standings (core API)
curl "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/standings"

# CFL teams
curl "https://sports.core.api.espn.com/v2/sports/football/leagues/cfl/teams"
```
