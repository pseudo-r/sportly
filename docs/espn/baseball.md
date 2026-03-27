# ⚾ Baseball

> Baseball from Major League Baseball (MLB), college, winter leagues, and international tournaments.

**Sport slug:** `baseball`  
**Base URL (v2):** `https://sports.core.api.espn.com/v2/sports/baseball/`  
**Base URL (v3):** `https://sports.core.api.espn.com/v3/sports/baseball/`

---

## Leagues & Competitions

| Abbreviation | League Name | Slug | Full URL |
| --- | --- | --- | --- |
| `CBWS` | Caribbean Series | `caribbean-series` | `https://sports.core.api.espn.com/v2/sports/baseball/leagues/caribbean-series` |
| `CBASE` | NCAA Baseball | `college-baseball` | `https://sports.core.api.espn.com/v2/sports/baseball/leagues/college-baseball` |
| `CSOFT` | NCAA Softball | `college-softball` | `https://sports.core.api.espn.com/v2/sports/baseball/leagues/college-softball` |
| `DOMWL` | Dominican Winter League | `dominican-winter-league` | `https://sports.core.api.espn.com/v2/sports/baseball/leagues/dominican-winter-league` |
| `LITTLE LEAGUE BASEBALL WORLD SERIES` | Little League Baseball | `llb` | `https://sports.core.api.espn.com/v2/sports/baseball/leagues/llb` |
| `LITTLE LEAGUE SOFTBALL WORLD SERIES` | Little League Softball | `lls` | `https://sports.core.api.espn.com/v2/sports/baseball/leagues/lls` |
| `LMB` | Mexican League | `mexican-winter-league` | `https://sports.core.api.espn.com/v2/sports/baseball/leagues/mexican-winter-league` |
| `MLB` | Major League Baseball | `mlb` | `https://sports.core.api.espn.com/v2/sports/baseball/leagues/mlb` |
| `OLYBB` | Olympics Men's Baseball | `olympics-baseball` | `https://sports.core.api.espn.com/v2/sports/baseball/leagues/olympics-baseball` |
| `PUERT` | Puerto Rican Winter League | `puerto-rican-winter-league` | `https://sports.core.api.espn.com/v2/sports/baseball/leagues/puerto-rican-winter-league` |
| `VENWL` | Venezuelan Winter League | `venezuelan-winter-league` | `https://sports.core.api.espn.com/v2/sports/baseball/leagues/venezuelan-winter-league` |
| `WBBC` | World Baseball Classic | `world-baseball-classic` | `https://sports.core.api.espn.com/v2/sports/baseball/leagues/world-baseball-classic` |

---

## API Endpoints

> All endpoints below follow the pattern:  
> `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}<sub-path>`  
> Replace `{league}` with a league slug from the table above.

### Common Query Parameters

Most list endpoints support: `page` (int), `limit` (int). Additional filters are documented per endpoint.

### Seasons & Calendar

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/calendar` | `getCalendars` | `dates`, `page`, `limit`, `dates`, `groups`, `smartdates`, `advance`, `utcOffset`, `weeks`, `seasontype` |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/seasons` | `getSeasons` | `page`, `limit`, `utcOffset`, `dates`, `start`, `end`, `eventsback`, `eventsforward`, `eventsrange`, `eventcompleted`, `groups`, `profile`, `competitions.types`, `types`, `season`, `weeks`, `tournamentId`, `dates`, `sort`, `type`, `date`, `group`, `position`, `week`, `qualified`, `types`, `limit`, `page`, `sort`, `position`, `status`, `sort`, `sortByRanks`, `stats`, `groupId`, `position`, `qualified`, `rookie`, `international`, `category`, `type`, `sort`, `sortByRanks`, `stats`, `groupId`, `qualified`, `category`, `sort`, `groupId`, `allStar`, `group`, `gender`, `types`, `country`, `association`, `lastNameInitial`, `lastName`, `active`, `statuses`, `sort`, `position`, `dates`, `groups`, `smartdates`, `advance`, `utcOffset`, `weeks`, `seasontype` |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/seasons/{season}/athletes` | `getAthletes` | `active`, `sort`, `page`, `limit`, `seasontypes`, `played`, `teamtypes`, `group`, `gender`, `types`, `country`, `association`, `lastNameInitial`, `lastName`, `active`, `statuses`, `sort`, `position` |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/seasons/{season}/draft` | `getDraftByYear` | `page`, `limit`, `available`, `position`, `team`, `sort`, `filter` |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/seasons/{season}/freeagents` | `getFreeAgents` | `page`, `limit`, `types`, `oldteams`, `newteams`, `position`, `sort` |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/seasons/{season}/manufacturers` | `getManufacturers` | `page`, `limit` |

### Teams

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/teams` | `getTeams` | `page`, `limit`, `utcOffset`, `dates`, `start`, `end`, `eventsback`, `eventsforward`, `eventsrange`, `eventcompleted`, `groups`, `profile`, `competitions.types`, `types`, `season`, `weeks`, `tournamentId`, `active`, `national`, `start`, `group`, `dates`, `recent`, `types`, `winnertype`, `date`, `eventsback`, `excludestatuses`, `includestatuses`, `dates`, `groups`, `smartdates`, `advance`, `utcOffset`, `weeks`, `seasontype` |

### Athletes / Players

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/athletes` | `getAthletes` | `page`, `limit`, `group`, `gender`, `types`, `country`, `association`, `lastNameInitial`, `lastName`, `active`, `statuses`, `sort`, `position` |

### Events / Games

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/events/{event}` | `getEvent` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/events/{event}/competitions/{competition}` | `getCompetition` | `page`, `limit`, `date`, `group`, `position`, `week`, `qualified`, `types`, `limit`, `page`, `types`, `period`, `sort`, `source`, `showsubplays` |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/events/{event}/competitions/{competition}/broadcasts` | `getBroadcasts` | `lang`, `region`, `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/events/{event}/competitions/{competition}/competitors/{competitor}` | `getCompetitor` | `page`, `limit`, `date`, `group`, `position`, `week`, `qualified`, `types`, `limit`, `page` |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/events/{event}/competitions/{competition}/odds` | `getCompetitionOdds` | `provider.priority`, `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/events/{event}/competitions/{competition}/officials` | `getOfficials` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/events/{event}/competitions/{competition}/plays/{play}/personnel` | `getPersonnel` | `page`, `limit` |

### News & Media

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/media` | `getMedia` | `page`, `limit` |

### Rankings & Awards

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/rankings` | `getRankings` | `page`, `limit` |

### Venues

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/venues` | `getVenues` | `page`, `limit` |

### Other

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/casinos` | `getCasinos` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/circuits` | `getCircuits` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/countries` | `getCountries` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/franchises` | `getFranchises` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/positions` | `getPositions` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/providers` | `getProviders` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/recruiting` | `getRecruitingSeasons` | `page`, `limit`, `sort`, `position`, `status` |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/season` | `getCurrentSeason` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/baseball/leagues/{league}/tournaments` | `getTournaments` | `majorsOnly`, `page`, `limit` |

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
GET https://site.api.espn.com/apis/site/v2/sports/baseball/{league}/{resource}
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
| `groups` | Divisions |
| `standings` | ⚠️ Stub only — see note below |
| `news` | Latest news |
| `athletes/{id}/news` | Athlete-specific news |
| `summary?event={id}` | Full game summary + boxscore |

> ⚠️ **Standings Note:** The `/apis/site/v2/` path returns only a stub for standings. Use `/apis/v2/` instead:
> `https://site.api.espn.com/apis/v2/sports/baseball/{league}/standings`

---

## CDN Game Data

> Rich game packages via `cdn.espn.com`. Requires `?xhr=1`.

```bash
curl "https://cdn.espn.com/core/mlb/game?xhr=1&gameId={EVENT_ID}"
curl "https://cdn.espn.com/core/mlb/boxscore?xhr=1&gameId={EVENT_ID}"
curl "https://cdn.espn.com/core/mlb/scoreboard?xhr=1"
```

---

## Athlete Data (common/v3)

> Works for MLB: `stats`, `gamelog`, `overview`, `splits`. Also supports `statistics/byathlete` with category filtering.

```bash
curl "https://site.web.api.espn.com/apis/common/v3/sports/baseball/mlb/athletes/{id}/overview"
curl "https://site.web.api.espn.com/apis/common/v3/sports/baseball/mlb/athletes/{id}/stats"
curl "https://site.web.api.espn.com/apis/common/v3/sports/baseball/mlb/athletes/{id}/gamelog"
curl "https://site.web.api.espn.com/apis/common/v3/sports/baseball/mlb/athletes/{id}/splits"

# Stats leaderboard with category filter
curl "https://site.web.api.espn.com/apis/common/v3/sports/baseball/mlb/statistics/byathlete?category=batting&sort=batting.homeRuns:desc&season=2024&seasontype=2"
```

---

## Example API Calls

```bash
# MLB scoreboard (today)
curl "https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard"

# MLB scoreboard for a specific date
curl "https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard?dates=20250920"

# MLB standings (use /apis/v2/ — /apis/site/v2/ only returns a stub)
curl "https://site.api.espn.com/apis/v2/sports/baseball/mlb/standings"

# New York Yankees roster
curl "https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/teams/10/roster"

# New York Yankees injuries
curl "https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/teams/10/injuries"

# College Baseball scoreboard
curl "https://site.api.espn.com/apis/site/v2/sports/baseball/college-baseball/scoreboard"

# Get all baseball leagues (core API)
curl "https://sports.core.api.espn.com/v2/sports/baseball/leagues"

# MLB teams (core API)
curl "https://sports.core.api.espn.com/v2/sports/baseball/leagues/mlb/teams?limit=50"

# MLB athletes (core API)
curl "https://sports.core.api.espn.com/v2/sports/baseball/leagues/mlb/athletes?limit=100&active=true"

# World Baseball Classic teams
curl "https://sports.core.api.espn.com/v2/sports/baseball/leagues/world-baseball-classic/teams"
```
