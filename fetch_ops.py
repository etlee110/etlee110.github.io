#!/usr/bin/env python3
import json
import requests
from datetime import date

BASE_URL = "https://statsapi.mlb.com"
MIN_PA = 50
LIMIT = 60


def fetch_ops_leaders():
    url = (
        f"{BASE_URL}/api/v1/stats"
        f"?stats=season&group=hitting&gameType=R&season={date.today().year}"
        f"&sportId=1&limit={LIMIT}&sortStat=onBasePlusSlugging&playerPool=qualified"
    )
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()

    leaders = []
    for split in resp.json().get("stats", [{}])[0].get("splits", []):
        stat = split.get("stat", {})
        pa = stat.get("plateAppearances", 0)
        if pa < MIN_PA:
            continue

        player = split.get("player", {})
        player_id = player.get("id")

        leaders.append({
            "name": player.get("fullName", "Unknown"),
            "team": split.get("team", {}).get("name", ""),
            "pa": pa,
            "ops": stat.get("ops"),
            "avg": stat.get("avg"),
            "obp": stat.get("obp"),
            "slg": stat.get("slg"),
            "url": f"https://www.mlb.com/player/{player_id}" if player_id else None,
        })

    return leaders


def main():
    leaders = fetch_ops_leaders()
    output = {
        "fetched": str(date.today()),
        "min_pa": MIN_PA,
        "leaders": leaders,
    }
    with open("_data/ops_leaders.json", "w") as f:
        json.dump(output, f, indent=2)
    print(f"Wrote {len(leaders)} OPS leaders to _data/ops_leaders.json")


if __name__ == "__main__":
    main()
