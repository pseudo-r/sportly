"""sportly CLI entry point.

Installed as the ``sportly`` command via ``[project.scripts]`` in pyproject.toml.

Usage::

    sportly info
    sportly espn basketball teams --league nba
    sportly espn football scoreboard --league nfl
    sportly espn soccer standings --league eng.1
    sportly nhl teams
    sportly nhl schedule
    sportly nhl schedule --date 2024-04-15
"""

from __future__ import annotations

import argparse
import json
import sys


def _cmd_info(args: argparse.Namespace) -> None:  # noqa: ARG001
    from sportly import __version__, __author__, __email__
    print(f"sportly {__version__}")
    print(f"Author : {__author__} <{__email__}>")
    print(f"Repo   : https://github.com/pseudo-r/sportly")
    print()
    print("Available namespaces:")
    print("  sportly.espn.basketball   NBA, WNBA, NCAA …")
    print("  sportly.espn.football     NFL, NCAAF, CFL …")
    print("  sportly.espn.soccer       EPL, La Liga, UCL …")
    print("  sportly.espn.hockey       NHL …")
    print("  sportly.espn.baseball     MLB …")
    print("  sportly.espn.cricket")
    print("  sportly.espn.tennis       ATP, WTA")
    print("  sportly.espn.golf         PGA, LPGA …")
    print("  sportly.espn.mma")
    print("  sportly.espn.racing       F1, NASCAR …")
    print("  sportly.nhl               Native NHL Web API")


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


# ── ESPN dispatch ─────────────────────────────────────────────────────────────

_ESPN_SPORTS = {
    "basketball", "football", "soccer", "hockey",
    "baseball", "cricket", "tennis", "golf", "mma", "racing",
}

_ESPN_METHODS = {
    "teams", "team", "roster", "scoreboard", "game",
    "news", "standings", "rankings", "athlete",
}


def _cmd_espn(args: argparse.Namespace) -> None:
    sport = args.sport
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
    if hasattr(args, "id") and args.id:
        # team / game / athlete positional
        result = fn(args.id, **kwargs)
    else:
        result = fn(**kwargs)

    _dump(result)


def _cmd_nhl(args: argparse.Namespace) -> None:
    from sportly.nhl import _inst as nhl

    if args.nhl_cmd == "teams":
        _dump(nhl.teams())
    elif args.nhl_cmd == "schedule":
        date = getattr(args, "date", None)
        _dump(nhl.schedule(date))
    elif args.nhl_cmd == "game":
        _dump(nhl.game(args.id))
    elif args.nhl_cmd == "play-by-play":
        _dump(nhl.play_by_play(args.id))
    else:
        print(f"Unknown NHL command '{args.nhl_cmd}'.")
        sys.exit(1)


# ── Argument parser ───────────────────────────────────────────────────────────

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="sportly",
        description="Python SDK CLI for ESPN and NHL sports data",
    )
    sub = parser.add_subparsers(dest="command")

    # info
    sub.add_parser("info", help="Show version and available namespaces")

    # espn <sport> <method>
    espn_p = sub.add_parser("espn", help="ESPN data")
    espn_p.add_argument("sport", choices=sorted(_ESPN_SPORTS), help="Sport slug")
    espn_p.add_argument("method", choices=sorted(_ESPN_METHODS), help="Method to call")
    espn_p.add_argument("--league", "-l", default=None, help="League slug, e.g. nba")
    espn_p.add_argument("--date",   "-d", default=None, help="Date YYYYMMDD")
    espn_p.add_argument("--id",           default=None, help="Team / game / athlete ID")

    # nhl
    nhl_p = sub.add_parser("nhl", help="Native NHL API")
    nhl_sub = nhl_p.add_subparsers(dest="nhl_cmd")
    nhl_sub.add_parser("teams", help="All NHL franchises")
    sched_p = nhl_sub.add_parser("schedule", help="Schedule for a date")
    sched_p.add_argument("--date", "-d", default=None, help="Date YYYY-MM-DD")
    game_p = nhl_sub.add_parser("game", help="Game boxscore")
    game_p.add_argument("id", help="NHL game ID")
    pbp_p = nhl_sub.add_parser("play-by-play", help="Play-by-play")
    pbp_p.add_argument("id", help="NHL game ID")

    return parser


def main() -> None:
    """Entry point for the ``sportly`` CLI command."""
    parser = _build_parser()
    args = parser.parse_args()

    if args.command == "info":
        _cmd_info(args)
    elif args.command == "espn":
        _cmd_espn(args)
    elif args.command == "nhl":
        _cmd_nhl(args)
    else:
        parser.print_help()
        sys.exit(0)


if __name__ == "__main__":
    main()
