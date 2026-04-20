#!/usr/bin/env python3
import json
import requests
from bs4 import BeautifulSoup
from datetime import date

BREF_BASE = "https://www.baseball-reference.com"
MIN_PA = 50


def fetch_ops_leaders():
    year = date.today().year
    url = f"{BREF_BASE}/leagues/majors/{year}-standard-batting.shtml"
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=15)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.content, "html.parser")
    table = soup.find("table", {"id": "players_standard_batting"})
    if not table:
        raise RuntimeError("Could not find batting table on Baseball Reference")

    players = []
    for row in table.find("tbody").find_all("tr"):
        classes = row.get("class", [])
        if "thead" in classes or "spacer" in classes:
            continue

        def cell(stat):
            td = row.find("td", {"data-stat": stat})
            return td.get_text(strip=True) if td else ""

        ops_str = cell("b_onbase_plus_slugging")
        pa_str = cell("b_pa")
        if not ops_str or not pa_str:
            continue

        try:
            ops = float(ops_str)
            pa = int(pa_str)
        except ValueError:
            continue

        if pa < MIN_PA:
            continue

        name_td = row.find("td", {"data-stat": "name_display"})
        if not name_td:
            continue
        name = name_td.get_text(strip=True).rstrip("*#")
        link = name_td.find("a")
        href = f"{BREF_BASE}{link['href']}" if link else None

        players.append({
            "name": name,
            "team": cell("team_name_abbr"),
            "pa": pa,
            "ops": ops,
            "avg": cell("b_batting_avg"),
            "obp": cell("b_onbase_perc"),
            "slg": cell("b_slugging_perc"),
            "ops_plus": cell("b_onbase_plus_slugging_plus"),
            "url": href,
        })

    players.sort(key=lambda x: x["ops"], reverse=True)
    return players[:20]


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
