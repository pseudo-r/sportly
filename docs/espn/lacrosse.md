# 🥍 Lacrosse

> Lacrosse from the NLL, PLL, and NCAA.

**Sport slug:** `lacrosse`  
**Base URL (v2):** `https://sports.core.api.espn.com/v2/sports/lacrosse/`  
**Base URL (v3):** `https://sports.core.api.espn.com/v3/sports/lacrosse/`

---

## Leagues & Competitions

| Abbreviation | League Name | Slug | Full URL |
| --- | --- | --- | --- |
| `NCAAM LACROSSE` | NCAA Men's Lacrosse | `mens-college-lacrosse` | `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/mens-college-lacrosse` |
| `NLL` | National Lacrosse League | `nll` | `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/nll` |
| `PLL` | Premier Lacrosse League | `pll` | `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/pll` |
| `NCAAW LACROSSE` | NCAA Women's Lacrosse | `womens-college-lacrosse` | `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/womens-college-lacrosse` |

---

## API Endpoints

> All endpoints below follow the pattern:  
> `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}<sub-path>`  
> Replace `{league}` with a league slug from the table above.

### Common Query Parameters

Most list endpoints support: `page` (int), `limit` (int). Additional filters are documented per endpoint.

### Seasons & Calendar

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/calendar` | `getCalendars` | `dates`, `page`, `limit`, `dates`, `groups`, `smartdates`, `advance`, `utcOffset`, `weeks`, `seasontype` |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/seasons` | `getSeasons` | `page`, `limit`, `utcOffset`, `dates`, `start`, `end`, `eventsback`, `eventsforward`, `eventsrange`, `eventcompleted`, `groups`, `profile`, `competitions.types`, `types`, `season`, `weeks`, `tournamentId`, `dates`, `sort`, `type`, `date`, `group`, `position`, `week`, `qualified`, `types`, `limit`, `page`, `sort`, `position`, `status`, `sort`, `sortByRanks`, `stats`, `groupId`, `position`, `qualified`, `rookie`, `international`, `category`, `type`, `sort`, `sortByRanks`, `stats`, `groupId`, `qualified`, `category`, `sort`, `groupId`, `allStar`, `group`, `gender`, `types`, `country`, `association`, `lastNameInitial`, `lastName`, `active`, `statuses`, `sort`, `position`, `dates`, `groups`, `smartdates`, `advance`, `utcOffset`, `weeks`, `seasontype` |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/seasons/{season}/athletes` | `getAthletes` | `active`, `sort`, `page`, `limit`, `seasontypes`, `played`, `teamtypes`, `group`, `gender`, `types`, `country`, `association`, `lastNameInitial`, `lastName`, `active`, `statuses`, `sort`, `position` |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/seasons/{season}/draft` | `getDraftByYear` | `page`, `limit`, `available`, `position`, `team`, `sort`, `filter` |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/seasons/{season}/freeagents` | `getFreeAgents` | `page`, `limit`, `types`, `oldteams`, `newteams`, `position`, `sort` |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/seasons/{season}/manufacturers` | `getManufacturers` | `page`, `limit` |

### Teams

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/teams` | `getTeams` | `page`, `limit`, `utcOffset`, `dates`, `start`, `end`, `eventsback`, `eventsforward`, `eventsrange`, `eventcompleted`, `groups`, `profile`, `competitions.types`, `types`, `season`, `weeks`, `tournamentId`, `active`, `national`, `start`, `group`, `dates`, `recent`, `types`, `winnertype`, `date`, `eventsback`, `excludestatuses`, `includestatuses`, `dates`, `groups`, `smartdates`, `advance`, `utcOffset`, `weeks`, `seasontype` |

### Athletes / Players

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/athletes` | `getAthletes` | `page`, `limit`, `group`, `gender`, `types`, `country`, `association`, `lastNameInitial`, `lastName`, `active`, `statuses`, `sort`, `position` |

### Events / Games

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/events/{event}` | `getEvent` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/events/{event}/competitions/{competition}` | `getCompetition` | `page`, `limit`, `date`, `group`, `position`, `week`, `qualified`, `types`, `limit`, `page`, `types`, `period`, `sort`, `source`, `showsubplays` |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/events/{event}/competitions/{competition}/broadcasts` | `getBroadcasts` | `lang`, `region`, `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/events/{event}/competitions/{competition}/competitors/{competitor}` | `getCompetitor` | `page`, `limit`, `date`, `group`, `position`, `week`, `qualified`, `types`, `limit`, `page` |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/events/{event}/competitions/{competition}/odds` | `getCompetitionOdds` | `provider.priority`, `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/events/{event}/competitions/{competition}/officials` | `getOfficials` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/events/{event}/competitions/{competition}/plays/{play}/personnel` | `getPersonnel` | `page`, `limit` |

### News & Media

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/media` | `getMedia` | `page`, `limit` |

### Rankings & Awards

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/rankings` | `getRankings` | `page`, `limit` |

### Venues

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/venues` | `getVenues` | `page`, `limit` |

### Other

| Endpoint | Method ID | Query Params |
| --- | --- | --- |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/casinos` | `getCasinos` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/circuits` | `getCircuits` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/countries` | `getCountries` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/franchises` | `getFranchises` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/positions` | `getPositions` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/providers` | `getProviders` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/recruiting` | `getRecruitingSeasons` | `page`, `limit`, `sort`, `position`, `status` |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/season` | `getCurrentSeason` | `page`, `limit` |
| `https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/{league}/tournaments` | `getTournaments` | `majorsOnly`, `page`, `limit` |

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
GET https://site.api.espn.com/apis/site/v2/sports/lacrosse/{league}/{resource}
```

| Resource | Description |
|----------|-------------|
| `scoreboard` | Live scores & schedules |
| `teams` | All teams |
| `standings` | League standings |
| `news` | Latest news |

---

## Example API Calls

```bash
# PLL scoreboard
curl "https://site.api.espn.com/apis/site/v2/sports/lacrosse/pll/scoreboard"

# NLL scoreboard
curl "https://site.api.espn.com/apis/site/v2/sports/lacrosse/nll/scoreboard"

# Get all lacrosse leagues (core API)
curl "https://sports.core.api.espn.com/v2/sports/lacrosse/leagues"

# PLL teams (core API)
curl "https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/pll/teams"

# PLL events (core API)
curl "https://sports.core.api.espn.com/v2/sports/lacrosse/leagues/pll/events"
```
