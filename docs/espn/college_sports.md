# 🎓 College Sports

> ESPN API coverage of US college sports including Football (NCAAF), Men's & Women's Basketball (NCAAM/NCAAW), and Baseball.

---

## Supported College Leagues

| Sport | League Name | Slug | Core API URL |
|-------|------------|------|-------------|
| Football | NCAA Football | `college-football` | `sports.core.api.espn.com/v2/sports/football/leagues/college-football` |
| Men's Basketball | NCAA Men's Basketball | `mens-college-basketball` | `sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball` |
| Women's Basketball | NCAA Women's Basketball | `womens-college-basketball` | `sports.core.api.espn.com/v2/sports/basketball/leagues/womens-college-basketball` |
| Baseball | NCAA Baseball | `college-baseball` | `sports.core.api.espn.com/v2/sports/baseball/leagues/college-baseball` |

---

## Site API Endpoints

```
GET https://site.api.espn.com/apis/site/v2/sports/{sport}/{league}/{resource}
```

| Resource | NCAAF | NCAAM | NCAAW | NCAAB |
|----------|-------|-------|-------|-------|
| `scoreboard` | ✅ | ✅ | ✅ | ✅ |
| `scoreboard?dates={YYYYMMDD}` | ✅ | ✅ | ✅ | ✅ |
| `teams` | ✅ | ✅ | ✅ | ✅ |
| `teams/{id}` | ✅ | ✅ | ✅ | ✅ |
| `teams/{id}/roster` | ✅ | ✅ | ✅ | ✅ |
| `teams/{id}/schedule` | ✅ | ✅ | ✅ | ✅ |
| `news` | ✅ | ✅ | ✅ | ✅ |
| `rankings` | ✅ | ✅ | — | — |
| `summary?event={id}` | ✅ | ✅ | ✅ | ✅ |
| `groups` | ✅ | ✅ | ✅ | ✅ |

---

## College Football Specifics

### Conference Filtering (groups)

```bash
# Filter scoreboard by conference group
curl "https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?groups=80&dates=20241010"

# Common group IDs:
#   80 = FBS (all major conferences)
#   4  = ACC
#   8  = Big 12
#   9  = Pac-12
#  12  = SEC
#  21  = Big Ten
```

### Week-based Scoreboard

```bash
# NCAAF — Week 1, Regular Season
curl "https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?week=1&seasontype=2"
```

### Rankings

```bash
# AP Top 25 + Coaches Poll
curl "https://site.api.espn.com/apis/site/v2/sports/football/college-football/rankings"
```

Response includes: `rankings[].name` (e.g. `"AP Top 25"`), `ranks[]` with team, current rank, previous rank, first place votes.

### Power Index (SP+)

```bash
curl "https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/2024/powerindex"
curl "https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/2024/powerindex/leaders"
```

### QBR

```bash
# College Football QBR (Group 80 = FBS)
curl "https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/2024/types/2/groups/80/qbr/0"
```

### Recruiting

```bash
curl "https://sports.core.api.espn.com/v2/sports/football/leagues/college-football/seasons/2024/recruits"
```

---

## College Basketball Specifics

### Rankings

```bash
# AP Poll + USA Today Poll
curl "https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/rankings"
```

### Power Index (BPI)

```bash
curl "https://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/seasons/2025/powerindex"
curl "https://sports.core.api.espn.com/v2/sports/basketball/leagues/mens-college-basketball/seasons/2025/powerindex/leaders"
```

### NCAA Tournament Bracket

```bash
# Live bracket projections (Bracketology)
curl "https://sports.core.api.espn.com/v2/tournament/22/seasons/2025/bracketology"

# 22 = NCAA Men's Tournament, 23 = NCAA Women's Tournament
```

---

## CDN Game Data

```bash
# College Football — full game package
curl "https://cdn.espn.com/core/college-football/game?xhr=1&gameId={EVENT_ID}"
curl "https://cdn.espn.com/core/college-football/scoreboard?xhr=1"
```

---

## Example API Calls

```bash
# NCAAF scoreboard (all FBS games, current week)
curl "https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?groups=80"

# NCAAF Week 1 scores
curl "https://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?week=1&seasontype=2&groups=80"

# Men's NCAAB scoreboard
curl "https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/scoreboard"

# Women's NCAAB scoreboard
curl "https://site.api.espn.com/apis/site/v2/sports/basketball/womens-college-basketball/scoreboard"

# College Baseball scoreboard
curl "https://site.api.espn.com/apis/site/v2/sports/baseball/college-baseball/scoreboard"

# AP Top 25 in College Football
curl "https://site.api.espn.com/apis/site/v2/sports/football/college-football/rankings"

# AP Top 25 in NCAAB
curl "https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/rankings"

# All NCAAF teams (use limit for pagination)
curl "https://site.api.espn.com/apis/site/v2/sports/football/college-football/teams?limit=500"

# All NCAAB teams
curl "https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/teams?limit=500"
```
