#!/usr/bin/env python3
import json
import re
import requests
import sys
from datetime import date, timedelta

BASE_URL = "https://statsapi.mlb.com"


def get_games(game_date):
    url = f"{BASE_URL}/api/v1/schedule?sportId=1&date={game_date}"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    games = []
    for d in resp.json().get("dates", []):
        games.extend(d.get("games", []))
    return games


def get_home_runs(game_pk):
    url = f"{BASE_URL}/api/v1.1/game/{game_pk}/feed/live"
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()
    data = resp.json()

    teams = data.get("gameData", {}).get("teams", {})
    away = teams.get("away", {}).get("name", "Away")
    home = teams.get("home", {}).get("name", "Home")
    matchup = f"{away} @ {home}"

    home_runs = []
    all_plays = data.get("liveData", {}).get("plays", {}).get("allPlays", [])

    for play in all_plays:
        result = play.get("result", {})
        if result.get("eventType") != "home_run":
            continue

        batter = play.get("matchup", {}).get("batter", {}).get("fullName", "Unknown")

        # Statcast hit data lives on the last pitch event, not the play root
        hit_data = {}
        play_id = None
        for event in reversed(play.get("playEvents", [])):
            if event.get("hitData"):
                hit_data = event["hitData"]
                play_id = event.get("playId")
                break

        distance = hit_data.get("totalDistance")

        pitcher = play.get("matchup", {}).get("pitcher", {}).get("fullName", "Unknown")
        description = result.get("description", "")
        m = re.search(r"homers?\s*\((\d+)\)", description, re.IGNORECASE)
        season_hr = int(m.group(1)) if m else None

        home_runs.append({
            "batter": batter,
            "pitcher": pitcher,
            "hr_count": season_hr,
            "distance_ft": distance,
            "launch_speed": hit_data.get("launchSpeed"),
            "launch_angle": hit_data.get("launchAngle"),
            "inning": play.get("about", {}).get("inning"),
            "half_inning": play.get("about", {}).get("halfInning", ""),
            "game": matchup,
            "description": description,
            "savant_url": f"https://baseballsavant.mlb.com/sporty-videos?playId={play_id}" if play_id else None,
            "big_fly": distance is not None and distance > 420,
        })

    return home_runs


def main():
    target_date = sys.argv[1] if len(sys.argv) > 1 else str(date.today() - timedelta(days=1))

    games = get_games(target_date)
    all_home_runs = []

    for game in games:
        if game.get("status", {}).get("abstractGameState") not in ("Final", "Live"):
            continue
        try:
            all_home_runs.extend(get_home_runs(game["gamePk"]))
        except Exception as e:
            print(f"[warn] game {game['gamePk']}: {e}")

    all_home_runs.sort(key=lambda x: x["distance_ft"] or 0, reverse=True)

    output = {
        "date": target_date,
        "no_games": len(games) == 0,
        "total": len(all_home_runs),
        "home_runs": all_home_runs,
    }

    with open("_data/home_runs.json", "w") as f:
        json.dump(output, f, indent=2)

    print(f"Wrote {len(all_home_runs)} home runs for {target_date} to _data/home_runs.json")


if __name__ == "__main__":
    main()
