import requests
import json
import os
from datetime import datetime

API_KEY = "e30ced038634957b94c47f2eb92faa70"
BASEBALL_URL = "https://api.api-baseball.io/v3/standings"
CACHE_FILE = "mlb_standings.json"

def fetch_and_cache_standings():
    if os.path.exists(CACHE_FILE):
        cache_time = datetime.fromtimestamp(os.path.getmtime(CACHE_FILE))
        time_diff = datetime.now() - cache_time
        # Only fetch data if it's older than 24 hours
        if time_diff.total_seconds() < 24 * 60 * 60:
            print("Using cached standings data.")
            with open(CACHE_FILE, "r") as file:
                return json.load(file)

    # Fetch new standings from API
    headers = {"x-rapidapi-key": API_KEY}
    response = requests.get(BASEBALL_URL, headers=headers)
    if response.status_code == 200:
        standings = response.json()
        print("Fetched new standings data.")
        # Save data to cache file
        with open(CACHE_FILE, "w") as file:
            json.dump(standings, file, indent=4)
        return standings
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

standings = fetch_and_cache_standings()
print(standings)
