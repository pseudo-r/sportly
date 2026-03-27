"""sportly CLI entry point.

Installed as the ``sportly`` command via ``[project.scripts]`` in pyproject.toml.

Usage::

    sportly info

    # ESPN
    sportly espn basketball teams --league nba
    sportly espn football scoreboard --league nfl
    sportly espn soccer standings --league eng.1

    # Native APIs
    sportly nhl teams
    sportly nhl schedule --date 2024-04-15

    sportly mlb schedule
    sportly mlb schedule --date 2025-04-01
    sportly mlb teams
    sportly mlb player 660271
    sportly mlb leaders homeRuns --season 2025

    sportly nba scoreboard 2025-03-26
    sportly nba leaders PTS --season 2024-25
    sportly nba player 2544

    sportly nfl scoreboard --week 1 --season 2024
    sportly nfl teams
    sportly nfl injuries

    sportly fotmob matches 20260326
    sportly fotmob league 47
    sportly fotmob team 8456
    sportly fotmob search "erling haaland"
"""

from __future__ import annotations

import argparse
import json
import sys


def _dump(obj: object) -> None:
    """Print a result as pretty JSON."""
    if hasattr(obj, "model_dump"):
        print(json.dumps(obj.model_dump(mode="json"), indent=2, default=str))
    elif isinstance(obj, list):
        if obj and hasattr(obj[0], "model_dump"):
            print(json.dumps([o.model_dump(mode="json") for o in obj], indent=2, default=str))
        else:
            print(json.dumps(obj, indent=2, default=str))
    else:
        print(json.dumps(obj, indent=2, default=str))


# ── info ──────────────────────────────────────────────────────────────────────

def _cmd_info(args: argparse.Namespace) -> None:  # noqa: ARG001
    from sportly import __author__, __email__, __version__
    print(f"sportly {__version__}")
    print(f"Author : {__author__} <{__email__}>")
    print("Repo   : https://github.com/pseudo-r/sportly")
    print()
    print("Available namespaces:")
    namespaces = [
        ("sportly.espn", "17 sports, 139+ leagues"),
        ("sportly.nhl",  "NHL Web API + Stats REST"),
        ("sportly.mlb",  "MLB Stats API"),
        ("sportly.nba",  "NBA Stats API (WAF headers auto-injected)"),
        ("sportly.nfl",  "NFL via ESPN public infrastructure"),
        ("sportly.fantasy", "ESPN Fantasy v3 (ffl/fba/flb/fhl)"),
        ("sportly.fotmob",  "FotMob web API (xG, ratings, shot maps)"),
        ("sportly.sofascore", "Sofascore API — requires pip install sportly[sofascore]"),
    ]
    for ns, desc in namespaces:
        print(f"  {ns:<28} {desc}")


# ── ESPN ──────────────────────────────────────────────────────────────────────

_ESPN_SPORTS = {
    "basketball", "football", "soccer", "hockey", "baseball", "cricket",
    "tennis", "golf", "mma", "racing", "lacrosse", "volleyball",
    "water_polo", "field_hockey", "rugby", "rugby_league", "australian_football",
}

_ESPN_METHODS = {
    "teams", "team", "roster", "scoreboard", "game",
    "news", "standings", "rankings", "athlete", "injuries",
    "transactions", "leaders", "play_by_play", "odds",
}


def _cmd_espn(args: argparse.Namespace) -> None:
    sport  = args.sport
    method = args.method

    if sport not in _ESPN_SPORTS:
        print(f"Unknown sport '{sport}'. Choose from: {', '.join(sorted(_ESPN_SPORTS))}")
        sys.exit(1)

    if method not in _ESPN_METHODS:
        print(f"Unknown method '{method}'. Choose from: {', '.join(sorted(_ESPN_METHODS))}")
        sys.exit(1)

    import importlib
    mod = importlib.import_module(f"sportly.espn.{sport}")
    fn = getattr(mod, method, None)
    if fn is None:
        print(f"Method '{method}' not available for '{sport}'.")
        sys.exit(1)

    kwargs: dict[str, object] = {}
    if hasattr(args, "league") and args.league:
        kwargs["league"] = args.league
    if hasattr(args, "date") and args.date:
        kwargs["date"] = args.date

    result = fn(args.id, **kwargs) if hasattr(args, "id") and args.id else fn(**kwargs)
    _dump(result)


# ── NHL ───────────────────────────────────────────────────────────────────────

def _cmd_nhl(args: argparse.Namespace) -> None:
    from sportly.nhl import _inst as nhl
    if args.nhl_cmd == "teams":
        _dump(nhl.teams())
    elif args.nhl_cmd == "schedule":
        _dump(nhl.schedule(getattr(args, "date", None)))
    elif args.nhl_cmd == "game":
        _dump(nhl.game(args.id))
    elif args.nhl_cmd == "play-by-play":
        _dump(nhl.play_by_play(args.id))
    else:
        print(f"Unknown NHL command '{args.nhl_cmd}'.")
        sys.exit(1)


# ── MLB ───────────────────────────────────────────────────────────────────────

def _cmd_mlb(args: argparse.Namespace) -> None:
    import sportly.mlb as mlb
    cmd = args.mlb_cmd

    if cmd == "schedule":
        _dump(mlb.schedule(date=getattr(args, "date", None)))
    elif cmd == "teams":
        _dump(mlb.teams())
    elif cmd == "team":
        _dump(mlb.team(args.id))
    elif cmd == "roster":
        _dump(mlb.roster(args.id))
    elif cmd == "player":
        _dump(mlb.player(args.id))
    elif cmd == "boxscore":
        _dump(mlb.boxscore(args.id))
    elif cmd == "linescore":
        _dump(mlb.linescore(args.id))
    elif cmd == "play-by-play":
        _dump(mlb.play_by_play(args.id))
    elif cmd == "standings":
        _dump(mlb.standings(season=getattr(args, "season", None)))
    elif cmd == "leaders":
        _dump(mlb.leaders(args.category, season=getattr(args, "season", None)))
    elif cmd == "transactions":
        _dump(mlb.transactions(start_date=args.start_date, end_date=args.end_date))
    else:
        print(f"Unknown MLB command '{cmd}'.")
        sys.exit(1)


# ── NBA ───────────────────────────────────────────────────────────────────────

def _cmd_nba(args: argparse.Namespace) -> None:
    import sportly.nba as nba
    cmd = args.nba_cmd

    if cmd == "scoreboard":
        _dump(nba.scoreboard(args.date))
    elif cmd == "teams":
        _dump(nba.teams())
    elif cmd == "player":
        _dump(nba.player(args.id))
    elif cmd == "career":
        _dump(nba.career_stats(args.id))
    elif cmd == "leaders":
        season = getattr(args, "season", "2024-25") or "2024-25"
        _dump(nba.leaders(args.stat, season=season))
    elif cmd == "standings":
        season = getattr(args, "season", "2024-25") or "2024-25"
        _dump(nba.standings(season))
    elif cmd == "shot-chart":
        season = getattr(args, "season", "2024-25") or "2024-25"
        _dump(nba.shot_chart(args.id, season))
    else:
        print(f"Unknown NBA command '{cmd}'.")
        sys.exit(1)


# ── NFL ───────────────────────────────────────────────────────────────────────

def _cmd_nfl(args: argparse.Namespace) -> None:
    import sportly.nfl as nfl
    cmd = args.nfl_cmd

    if cmd == "scoreboard":
        week   = getattr(args, "week", None)
        season = getattr(args, "season", None)
        _dump(nfl.scoreboard(week=week, season=season))
    elif cmd == "teams":
        _dump(nfl.teams())
    elif cmd == "team":
        _dump(nfl.team(args.id))
    elif cmd == "injuries":
        _dump(nfl.injuries())
    elif cmd == "news":
        _dump(nfl.news())
    elif cmd == "standings":
        _dump(nfl.standings())
    elif cmd == "play-by-play":
        _dump(nfl.play_by_play(args.id))
    elif cmd == "depth-chart":
        _dump(nfl.depth_chart(args.id))
    elif cmd == "qbr":
        season = getattr(args, "season", None)
        _dump(nfl.qbr(season=season))
    else:
        print(f"Unknown NFL command '{cmd}'.")
        sys.exit(1)


# ── FotMob ────────────────────────────────────────────────────────────────────

def _cmd_fotmob(args: argparse.Namespace) -> None:
    import sportly.fotmob as fotmob
    cmd = args.fm_cmd

    if cmd == "matches":
        _dump(fotmob.matches(args.date))
    elif cmd == "match":
        _dump(fotmob.match(args.id))
    elif cmd == "league":
        _dump(fotmob.league(args.id))
    elif cmd == "team":
        _dump(fotmob.team(args.id))
    elif cmd == "player":
        _dump(fotmob.player(args.id))
    elif cmd == "search":
        _dump(fotmob.search(args.term))
    elif cmd == "leagues":
        _dump(fotmob.LEAGUES)
    else:
        print(f"Unknown FotMob command '{cmd}'.")
        sys.exit(1)


# ── Fantasy ───────────────────────────────────────────────────────────────────

def _cmd_fantasy(args: argparse.Namespace) -> None:
    import sportly.fantasy as fantasy
    cmd     = args.fs_cmd
    game    = args.game
    lid     = getattr(args, "league_id", None)
    season  = getattr(args, "season", None)
    cookies = None
    if getattr(args, "espn_s2", None) and getattr(args, "swid", None):
        cookies = {"espn_s2": args.espn_s2, "SWID": args.swid}

    if cmd == "league":
        views = args.views.split(",") if getattr(args, "views", None) else None
        _dump(fantasy.league(game, league_id=lid, season=season, views=views, cookies=cookies))
    elif cmd == "teams":
        _dump(fantasy.teams(game, league_id=lid, season=season, cookies=cookies))
    elif cmd == "roster":
        _dump(fantasy.roster(game, league_id=lid, season=season, cookies=cookies))
    elif cmd == "standings":
        _dump(fantasy.standings(game, league_id=lid, season=season, cookies=cookies))
    elif cmd == "draft":
        _dump(fantasy.draft(game, league_id=lid, season=season, cookies=cookies))
    elif cmd == "meta":
        _dump(fantasy.game_meta(game, cookies=cookies))
    else:
        print(f"Unknown Fantasy command '{cmd}'.")
        sys.exit(1)


# ── Sofascore ─────────────────────────────────────────────────────────────────

def _cmd_sofascore(args: argparse.Namespace) -> None:
    try:
        import sportly.sofascore as sofascore
    except ImportError:
        print("sportly.sofascore requires curl_cffi. Install with: pip install sportly[sofascore]")
        sys.exit(1)
    cmd = args.ss_cmd

    if cmd == "matches":
        _dump(sofascore.matches(args.sport, args.date))
    elif cmd == "match":
        _dump(sofascore.match(args.id))
    elif cmd == "stats":
        _dump(sofascore.match_stats(args.id))
    elif cmd == "lineups":
        _dump(sofascore.lineups(args.id))
    elif cmd == "player":
        _dump(sofascore.player(args.id))
    elif cmd == "team":
        _dump(sofascore.team(args.id))
    elif cmd == "squad":
        _dump(sofascore.squad(args.id))
    else:
        print(f"Unknown Sofascore command '{cmd}'.")
        sys.exit(1)


# ── Argument parser ───────────────────────────────────────────────────────────

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="sportly",
        description="Python SDK CLI for multi-source sports data",
    )
    sub = parser.add_subparsers(dest="command")

    # ── info ──────────────────────────────────────────────────────────────────
    sub.add_parser("info", help="Show version and available namespaces")

    # ── espn ──────────────────────────────────────────────────────────────────
    espn_p = sub.add_parser("espn", help="ESPN data (17 sports)")
    espn_p.add_argument("sport",  choices=sorted(_ESPN_SPORTS), help="Sport slug")
    espn_p.add_argument("method", choices=sorted(_ESPN_METHODS), help="Method to call")
    espn_p.add_argument("--league", "-l", default=None, help="League slug, e.g. nba")
    espn_p.add_argument("--date",   "-d", default=None, help="Date YYYYMMDD")
    espn_p.add_argument("--id",           default=None, help="Team / game / athlete ID")

    # ── nhl ───────────────────────────────────────────────────────────────────
    nhl_p   = sub.add_parser("nhl", help="Native NHL API")
    nhl_sub = nhl_p.add_subparsers(dest="nhl_cmd")
    nhl_sub.add_parser("teams", help="All NHL franchises")
    sp = nhl_sub.add_parser("schedule", help="Schedule for a date")
    sp.add_argument("--date", "-d", default=None, help="Date YYYY-MM-DD")
    gp = nhl_sub.add_parser("game", help="Game boxscore")
    gp.add_argument("id", help="NHL game ID")
    pp = nhl_sub.add_parser("play-by-play", help="Play-by-play")
    pp.add_argument("id", help="NHL game ID")

    # ── mlb ───────────────────────────────────────────────────────────────────
    mlb_p   = sub.add_parser("mlb", help="MLB Stats API")
    mlb_sub = mlb_p.add_subparsers(dest="mlb_cmd")
    mlb_sub.add_parser("teams", help="All MLB teams")
    sched = mlb_sub.add_parser("schedule", help="Games for a date")
    sched.add_argument("--date", "-d", default=None, help="Date YYYY-MM-DD")
    for cmd in ("team", "roster", "player", "boxscore", "linescore", "play-by-play"):
        p2 = mlb_sub.add_parser(cmd, help=f"MLB {cmd}")
        p2.add_argument("id", help="Team / game / player ID")
    st = mlb_sub.add_parser("standings", help="Division standings")
    st.add_argument("--season", default=None, type=int, help="Season year")
    ld = mlb_sub.add_parser("leaders", help="Statistical leaders")
    ld.add_argument("category", help="E.g. homeRuns, era, battingAverage")
    ld.add_argument("--season", default=None, type=int, help="Season year")
    tx = mlb_sub.add_parser("transactions", help="IL moves, trades")
    tx.add_argument("--start-date", required=True, dest="start_date", help="YYYY-MM-DD")
    tx.add_argument("--end-date",   required=True, dest="end_date",   help="YYYY-MM-DD")

    # ── nba ───────────────────────────────────────────────────────────────────
    nba_p   = sub.add_parser("nba", help="NBA Stats API")
    nba_sub = nba_p.add_subparsers(dest="nba_cmd")
    nba_sub.add_parser("teams", help="All NBA teams")
    sc = nba_sub.add_parser("scoreboard", help="Scoreboard for a date")
    sc.add_argument("date", help="Date YYYY-MM-DD")
    for cmd in ("player", "career", "shot-chart"):
        p2 = nba_sub.add_parser(cmd, help=f"NBA {cmd}")
        p2.add_argument("id", help="NBA player ID")
        if cmd in ("career", "shot-chart"):
            p2.add_argument("--season", default="2024-25", help="Season e.g. 2024-25")
    ld2 = nba_sub.add_parser("leaders", help="League leaders")
    ld2.add_argument("stat", help="E.g. PTS, REB, AST")
    ld2.add_argument("--season", default="2024-25", help="Season e.g. 2024-25")
    st2 = nba_sub.add_parser("standings", help="League standings")
    st2.add_argument("--season", default="2024-25", help="Season e.g. 2024-25")

    # ── nfl ───────────────────────────────────────────────────────────────────
    nfl_p   = sub.add_parser("nfl", help="NFL via ESPN")
    nfl_sub = nfl_p.add_subparsers(dest="nfl_cmd")
    for cmd in ("teams", "injuries", "news", "standings", "qbr"):
        nfl_sub.add_parser(cmd, help=f"NFL {cmd}")
    sb_nfl = nfl_sub.add_parser("scoreboard", help="NFL scoreboard")
    sb_nfl.add_argument("--week",   type=int, default=None, help="NFL week number")
    sb_nfl.add_argument("--season", type=int, default=None, help="Season year")
    for cmd in ("team", "depth-chart", "play-by-play"):
        p2 = nfl_sub.add_parser(cmd, help=f"NFL {cmd}")
        p2.add_argument("id", help="Team / game ID")

    # ── fotmob ────────────────────────────────────────────────────────────────
    fm_p   = sub.add_parser("fotmob", help="FotMob football data")
    fm_sub = fm_p.add_subparsers(dest="fm_cmd")
    fm_sub.add_parser("leagues", help="Show all popular league IDs")
    mt = fm_sub.add_parser("matches", help="All matches for a date")
    mt.add_argument("date", help="Date YYYYMMDD e.g. 20260326")
    sr = fm_sub.add_parser("search", help="Search players/teams/tournaments")
    sr.add_argument("term", help="Search term")
    for cmd in ("match", "league", "team", "player"):
        p2 = fm_sub.add_parser(cmd, help=f"FotMob {cmd} by ID")
        p2.add_argument("id", type=int, help="Numeric FotMob ID")

    # ── fantasy ───────────────────────────────────────────────────────────────
    def _add_fantasy_common(p: argparse.ArgumentParser) -> None:
        p.add_argument("game", choices=["ffl", "fba", "flb", "fhl"], help="Game code")
        p.add_argument("--league-id", required=True, type=int, dest="league_id", help="League ID")
        p.add_argument("--season",    required=True, type=int, help="Season year")
        p.add_argument("--espn-s2",   dest="espn_s2", default=None, help="espn_s2 cookie (private leagues)")
        p.add_argument("--swid",      dest="swid",    default=None, help="SWID cookie (private leagues)")

    fs_p   = sub.add_parser("fantasy", help="ESPN Fantasy (ffl/fba/flb/fhl)")
    fs_sub = fs_p.add_subparsers(dest="fs_cmd")
    for cmd in ("teams", "roster", "standings", "draft"):
        p2 = fs_sub.add_parser(cmd, help=f"Fantasy {cmd}")
        _add_fantasy_common(p2)
    lg_p = fs_sub.add_parser("league", help="Raw league data by view")
    _add_fantasy_common(lg_p)
    lg_p.add_argument("--views", default=None, help="Comma-separated views e.g. mTeam,mRoster")
    mt_p = fs_sub.add_parser("meta", help="Game metadata")
    mt_p.add_argument("game", choices=["ffl", "fba", "flb", "fhl"], help="Game code")
    mt_p.add_argument("--espn-s2", dest="espn_s2", default=None)
    mt_p.add_argument("--swid",    dest="swid",    default=None)

    # ── sofascore ─────────────────────────────────────────────────────────────
    ss_p   = sub.add_parser("sofascore", help="Sofascore (requires pip install sportly[sofascore])")
    ss_sub = ss_p.add_subparsers(dest="ss_cmd")
    ss_mt = ss_sub.add_parser("matches", help="Events for sport/date")
    ss_mt.add_argument("sport", help="Sport slug e.g. football, basketball, tennis")
    ss_mt.add_argument("date",  help="Date YYYY-MM-DD")
    for cmd in ("match", "stats", "lineups"):
        p2 = ss_sub.add_parser(cmd, help=f"Sofascore {cmd} by event ID")
        p2.add_argument("id", type=int, help="Event / match ID")
    for cmd in ("player", "team", "squad"):
        p2 = ss_sub.add_parser(cmd, help=f"Sofascore {cmd} by ID")
        p2.add_argument("id", type=int, help="Player / team ID")

    return parser


def main() -> None:
    """Entry point for the ``sportly`` CLI command."""
    parser = _build_parser()
    args = parser.parse_args()

    dispatch = {
        "info":       _cmd_info,
        "espn":       _cmd_espn,
        "nhl":        _cmd_nhl,
        "mlb":        _cmd_mlb,
        "nba":        _cmd_nba,
        "nfl":        _cmd_nfl,
        "fotmob":     _cmd_fotmob,
        "fantasy":    _cmd_fantasy,
        "sofascore":  _cmd_sofascore,
    }

    handler = dispatch.get(args.command)
    if handler:
        handler(args)
    else:
        parser.print_help()
        sys.exit(0)


if __name__ == "__main__":
    main()
