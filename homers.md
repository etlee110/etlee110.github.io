---
layout: page
title: MLB Stats
permalink: /homers/
---

# Last Night's Home Runs

{% assign data = site.data.home_runs %}

Updated daily at 12 PM ET &nbsp;·&nbsp; **{{ data.date }}** &nbsp;·&nbsp; {{ data.total }} home runs &nbsp;·&nbsp; *Statcast data via MLB Stats API*

<style>
  table.hr-table, table.ops-table {
    border-collapse: collapse;
    width: 100%;
    font-size: 1.05em;
    margin-bottom: 2em;
  }
  table.hr-table th, table.hr-table td,
  table.ops-table th, table.ops-table td {
    border: 1px solid #ddd;
    padding: 9px 12px;
    text-align: center;
  }
  table.hr-table th, table.ops-table th {
    background-color: #f4f4f4;
    font-weight: 700;
  }
  table.hr-table tr:nth-child(even),
  table.ops-table tr:nth-child(even) {
    background-color: #fafafa;
  }
  table.hr-table tr.big-fly td {
    background-color: #fff3cd;
    font-weight: 700;
  }
  table.hr-table tr.big-fly td:nth-child(3) {
    color: #b85c00;
    font-size: 1.1em;
  }
  table.hr-table td:nth-child(2) a,
  table.ops-table td:nth-child(2) a {
    color: inherit;
    text-decoration: none;
    border-bottom: 1px dashed #888;
  }
  table.hr-table td:nth-child(2) a:hover,
  table.ops-table td:nth-child(2) a:hover {
    border-bottom-color: #333;
  }
</style>

{% if data.no_games %}
<p><em>No games on {{ data.date }}.</em></p>
{% elsif data.total == 0 %}
<p><em>No home runs on {{ data.date }}.</em></p>
{% else %}
<table class="hr-table">
  <thead>
    <tr>
      <th>#</th>
      <th>Batter</th>
      <th>Distance (ft)</th>
      <th>Exit Velo (mph)</th>
      <th>Launch Angle (°)</th>
      <th>Inning</th>
      <th>Game</th>
    </tr>
  </thead>
  <tbody>
    {% for hr in data.home_runs %}
    <tr{% if hr.big_fly %} class="big-fly"{% endif %}>
      <td>{{ forloop.index }}</td>
      <td>
        {% if hr.savant_url %}
          <a href="{{ hr.savant_url }}" target="_blank" rel="noopener">{{ hr.batter }}</a>
        {% else %}
          {{ hr.batter }}
        {% endif %}
      </td>
      <td>{% if hr.distance_ft %}{{ hr.distance_ft }}{% else %}—{% endif %}</td>
      <td>{% if hr.launch_speed %}{{ hr.launch_speed }}{% else %}—{% endif %}</td>
      <td>{% if hr.launch_angle %}{{ hr.launch_angle }}{% else %}—{% endif %}</td>
      <td>{% if hr.half_inning == "top" %}Top{% else %}Bot{% endif %} {{ hr.inning }}</td>
      <td>{{ hr.game }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
{% endif %}

---

# OPS Leaders

{% assign ops = site.data.ops_leaders %}

*{{ ops.fetched }} &nbsp;·&nbsp; Min. {{ ops.min_pa }} PA &nbsp;·&nbsp; Data via Baseball Reference*

<table class="ops-table">
  <thead>
    <tr>
      <th>#</th>
      <th>Player</th>
      <th>Team</th>
      <th>OPS</th>
      <th>OPS+</th>
      <th>AVG</th>
      <th>OBP</th>
      <th>SLG</th>
      <th>PA</th>
    </tr>
  </thead>
  <tbody>
    {% for p in ops.leaders %}
    <tr>
      <td>{{ forloop.index }}</td>
      <td>
        {% if p.url %}
          <a href="{{ p.url }}" target="_blank" rel="noopener">{{ p.name }}</a>
        {% else %}
          {{ p.name }}
        {% endif %}
      </td>
      <td>{{ p.team }}</td>
      <td><strong>{{ p.ops }}</strong></td>
      <td>{{ p.ops_plus }}</td>
      <td>{{ p.avg }}</td>
      <td>{{ p.obp }}</td>
      <td>{{ p.slg }}</td>
      <td>{{ p.pa }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
