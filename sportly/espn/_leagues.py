"""League and sport registry for the ESPN API.

All 17 ESPN sports and their known leagues, extracted from the ESPN WADL
(sports.core.api.espn.com/v2/application.wadl) and community documentation.

Usage
-----
::

    from sportly.espn._leagues import LEAGUES, SPORT_LEAGUES

    # All basketball leagues
    print(LEAGUES["basketball"])
    # {"nba": "National Basketball Association", ...}

    # Lookup a league name
    name = LEAGUES["soccer"].get("eng.1")
    # → "English Premier League"
"""

# ── Per-sport league registries ────────────────────────────────────────────────
# Format: {league_slug: "Display Name"}
# These are the canonical slugs to pass to all sportly.espn.* methods.

LEAGUES: dict[str, dict[str, str]] = {

    "australian-football": {
        "afl": "Australian Football League",
    },

    "baseball": {
        "mlb": "Major League Baseball",
        "college-baseball": "NCAA Baseball",
        "college-softball": "NCAA Softball",
        "world-baseball-classic": "World Baseball Classic",
        "dominican-winter-league": "Dominican Winter League",
        "mexican-winter-league": "Mexican Winter League",
        "puerto-rican-winter-league": "Puerto Rican Winter League",
        "venezuelan-winter-league": "Venezuelan Winter League",
        "caribbean-series": "Caribbean Series",
        "llb": "Little League Baseball",
        "lls": "Little League Softball",
        "olympics-baseball": "Olympics Men's Baseball",
    },

    "basketball": {
        "nba": "National Basketball Association",
        "wnba": "Women's National Basketball Association",
        "nba-development": "NBA G League",
        "nba-summer-las-vegas": "Las Vegas Summer League",
        "nba-summer-california": "NBA California Classic",
        "nba-summer-golden-state": "Golden State Summer League",
        "nba-summer-orlando": "Orlando Summer League",
        "nba-summer-sacramento": "Sacramento Summer League",
        "nba-summer-utah": "Salt Lake City Summer League",
        "mens-college-basketball": "NCAA Men's Basketball",
        "womens-college-basketball": "NCAA Women's Basketball",
        "mens-olympics-basketball": "Olympics Men's Basketball",
        "womens-olympics-basketball": "Olympics Women's Basketball",
        "nbl": "National Basketball League (Australia)",
        "fiba": "FIBA World Cup",
    },

    "cricket": {
        "icc-cricket": "ICC Cricket",
        "icc-men-t20-world-cup": "ICC Men's T20 World Cup",
        "icc-world-cup": "ICC Men's Cricket World Cup",
        "icc-champions-trophy": "ICC Champions Trophy",
    },

    "field-hockey": {
        "womens-college-field-hockey": "NCAA Women's Field Hockey",
        "fih-men": "FIH Men's Hockey",
        "fih-women": "FIH Women's Hockey",
    },

    "football": {
        "nfl": "National Football League",
        "college-football": "NCAA Football",
        "cfl": "Canadian Football League",
        "ufl": "United Football League",
        "xfl": "XFL",
    },

    "golf": {
        "pga": "PGA TOUR",
        "lpga": "LPGA TOUR",
        "eur": "DP World Tour",
        "liv": "LIV Golf",
        "champions-tour": "PGA TOUR Champions",
        "ntw": "Korn Ferry Tour",
        "tgl": "TGL",
        "mens-olympics-golf": "Olympic Golf – Men",
        "womens-olympics-golf": "Olympic Golf – Women",
    },

    "hockey": {
        "nhl": "National Hockey League",
        "mens-college-hockey": "NCAA Men's Ice Hockey",
        "womens-college-hockey": "NCAA Women's Hockey",
        "hockey-world-cup": "World Cup of Hockey",
        "olympics-mens-ice-hockey": "Men's Ice Hockey Olympics",
        "olympics-womens-ice-hockey": "Women's Ice Hockey Olympics",
    },

    "lacrosse": {
        "pll": "Premier Lacrosse League",
        "nll": "National Lacrosse League",
        "mens-college-lacrosse": "NCAA Men's Lacrosse",
        "womens-college-lacrosse": "NCAA Women's Lacrosse",
    },

    "mma": {
        "bellator": "Bellator MMA",
        "lfa": "Legacy Fighting Alliance",
        "cage-warriors": "Cage Warriors",
        "absolute": "Absolute Championship Berkut",
        "ksw": "KSW",
        "ifc": "Invicta FC",
        "fng": "Fight Nights Global",
        "k1": "K-1",
        "m1": "M-1 Global",
        "dream": "Dream",
        "ifl": "International Fight League",
        "lfc": "Legacy Fighting Championship",
    },

    "racing": {
        "f1": "Formula 1",
        "irl": "IndyCar Series",
        "nascar-premier": "NASCAR Cup Series",
        "nascar-secondary": "NASCAR Xfinity Series",
        "nascar-truck": "NASCAR Truck Series",
    },

    "rugby": {
        # Rugby union uses numeric league IDs
        "164205": "Rugby World Cup",
        "180659": "Six Nations",
        "244293": "The Rugby Championship",
        "271937": "European Rugby Champions Cup",
        "267979": "Gallagher Premiership",
        "270557": "United Rugby Championship",
        "270559": "French Top 14",
        "242041": "Super Rugby Pacific",
        "289262": "Major League Rugby",
        "289234": "International Test Match",
        "282": "Olympic Men's Rugby Sevens",
        "283": "Olympic Women's Rugby Sevens",
        "289237": "Women's Rugby World Cup",
        "268565": "British and Irish Lions Tour",
        "272073": "European Rugby Challenge Cup",
        "270555": "Currie Cup",
        "270563": "Mitre 10 Cup",
        "2009": "URBA Primera A",
    },

    "rugby-league": {
        "3": "Rugby League",
    },

    "soccer": {
        # International / FIFA
        "fifa.world": "FIFA World Cup",
        "fifa.wwc": "FIFA Women's World Cup",
        "fifa.world.u20": "FIFA Under-20 World Cup",
        "fifa.friendly": "International Friendly",
        "fifa.olympics": "Men's Olympic Soccer",
        "fifa.w.olympics": "Women's Olympic Soccer",
        "fifa.worldq": "World Cup Qualifying",
        "fifa.worldq.uefa": "WCQ – UEFA",
        "fifa.worldq.concacaf": "WCQ – CONCACAF",
        "fifa.worldq.conmebol": "WCQ – CONMEBOL",
        "fifa.worldq.caf": "WCQ – CAF",
        "fifa.worldq.afc": "WCQ – AFC",
        # UEFA
        "uefa.champions": "UEFA Champions League",
        "uefa.europa": "UEFA Europa League",
        "uefa.europa.conf": "UEFA Conference League",
        "uefa.super_cup": "UEFA Super Cup",
        "uefa.wchampions": "UEFA Women's Champions League",
        "uefa.euro": "UEFA European Championship",
        "uefa.euroq": "UEFA Euro Qualifying",
        "uefa.nations": "UEFA Nations League",
        # England
        "eng.1": "English Premier League",
        "eng.2": "English Championship",
        "eng.3": "English League One",
        "eng.4": "English League Two",
        "eng.fa": "English FA Cup",
        "eng.league_cup": "English Carabao Cup",
        "eng.w.1": "English Women's Super League",
        # Spain
        "esp.1": "Spanish LALIGA",
        "esp.2": "Spanish LALIGA 2",
        "esp.copa_del_rey": "Spanish Copa del Rey",
        "esp.super_cup": "Spanish Supercopa",
        "esp.w.1": "Spanish Liga F",
        # Germany
        "ger.1": "German Bundesliga",
        "ger.2": "German 2. Bundesliga",
        "ger.dfb_pokal": "German Cup",
        "ger.super_cup": "German Supercup",
        # Italy
        "ita.1": "Italian Serie A",
        "ita.2": "Italian Serie B",
        "ita.coppa_italia": "Coppa Italia",
        # France
        "fra.1": "French Ligue 1",
        "fra.2": "French Ligue 2",
        "fra.coupe_de_france": "Coupe de France",
        # Netherlands
        "ned.1": "Dutch Eredivisie",
        "ned.cup": "Dutch KNVB Beker",
        # Portugal / Belgium / Other Europe
        "por.1": "Portuguese Primeira Liga",
        "bel.1": "Belgian Pro League",
        "sco.1": "Scottish Premiership",
        "tur.1": "Turkish Super Lig",
        "rus.1": "Russian Premier League",
        "den.1": "Danish Superliga",
        "nor.1": "Norwegian Eliteserien",
        "swe.1": "Swedish Allsvenskan",
        # USA / CONCACAF
        "usa.1": "MLS",
        "usa.nwsl": "NWSL",
        "usa.open": "U.S. Open Cup",
        "usa.usl.1": "USL Championship",
        "usa.ncaa.m.1": "NCAA Men's Soccer",
        "usa.ncaa.w.1": "NCAA Women's Soccer",
        "concacaf.champions": "Concacaf Champions Cup",
        "concacaf.leagues.cup": "Leagues Cup",
        "concacaf.gold": "Concacaf Gold Cup",
        # Mexico
        "mex.1": "Mexican Liga BBVA MX",
        "mex.2": "Mexican Liga de Expansion MX",
        # South America
        "conmebol.libertadores": "CONMEBOL Libertadores",
        "conmebol.sudamericana": "CONMEBOL Sudamericana",
        "conmebol.america": "Copa America",
        "arg.1": "Argentine Liga Profesional",
        "bra.1": "Brazilian Serie A",
        "col.1": "Colombian Primera A",
        "chi.1": "Chilean Primera Division",
        "per.1": "Peruvian Liga 1",
        # Africa
        "caf.nations": "Africa Cup of Nations",
        "caf.champions": "CAF Champions League",
        "rsa.1": "South African Premiership",
        # Asia / Middle East
        "afc.champions": "AFC Champions League Elite",
        "afc.asian.cup": "AFC Asian Cup",
        "ksa.1": "Saudi Pro League",
        "jpn.1": "Japanese J.League",
        "chn.1": "Chinese Super League",
        # Oceania
        "aus.1": "Australian A-League Men",
        "aus.w.1": "Australian A-League Women",
        # Misc
        "club.friendly": "Club Friendly",
    },

    "tennis": {
        "atp": "ATP Tour",
        "wta": "WTA Tour",
    },

    "volleyball": {
        "womens-college-volleyball": "NCAA Women's Volleyball",
        "mens-college-volleyball": "NCAA Men's Volleyball",
    },

    "water-polo": {
        "mens-college-water-polo": "NCAA Men's Water Polo",
        "womens-college-water-polo": "NCAA Women's Water Polo",
    },
}


def league_name(sport: str, slug: str) -> str:
    """Return the display name for a league slug, or the slug itself if unknown."""
    return LEAGUES.get(sport, {}).get(slug, slug)


def sport_leagues(sport: str) -> dict[str, str]:
    """Return all known leagues for a sport slug."""
    return LEAGUES.get(sport, {})
