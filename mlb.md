---
layout: page
title: MLB Standings
permalink: /mlb-standings/
---

# MLB Standings

The standings below are automatically updated daily and show the latest records for each team.

{% assign standings = site.data.mlb_standings %}

## American League East
| Team               | Wins | Losses |
|--------------------|------|--------|
{% for team in standings.AL_East %}
| {{ team.team }}    | {{ team.wins }} | {{ team.losses }} |
{% endfor %}

## National League West
| Team               | Wins | Losses |
|--------------------|------|--------|
{% for team in standings.NL_West %}
| {{ team.team }}    | {{ team.wins }} | {{ team.losses }} |
{% endfor %}
