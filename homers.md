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
    cursor: pointer;
    user-select: none;
    white-space: nowrap;
  }
  table.hr-table th:hover, table.ops-table th:hover {
    background-color: #e8e8e8;
  }
  table.hr-table th[data-sort]::after, table.ops-table th[data-sort]::after {
    content: ' ' attr(data-sort);
    font-size: 0.75em;
    color: #666;
  }
  table.hr-table tr:nth-child(even),
  table.ops-table tr:nth-child(even) {
    background-color: #fafafa;
  }
  table.hr-table tr.big-fly td {
    background-color: #fff3cd;
    font-weight: 700;
  }
  table.hr-table tr.big-fly td:nth-child(4) {
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
      <th>HR #</th>
      <th>Distance (ft)</th>
      <th>Exit Velo (mph)</th>
      <th>Launch Angle (°)</th>
      <th>Pitcher</th>
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
      <td>{{ hr.hr_count }}</td>
      <td>{% if hr.distance_ft %}{{ hr.distance_ft }}{% else %}—{% endif %}</td>
      <td>{% if hr.launch_speed %}{{ hr.launch_speed }}{% else %}—{% endif %}</td>
      <td>{% if hr.launch_angle %}{{ hr.launch_angle }}{% else %}—{% endif %}</td>
      <td>{{ hr.pitcher }}</td>
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

*{{ ops.fetched }} &nbsp;·&nbsp; Min. {{ ops.min_pa }} PA &nbsp;·&nbsp; Data via MLB Stats API*

<table class="ops-table">
  <thead>
    <tr>
      <th>#</th>
      <th>Player</th>
      <th>Team</th>
      <th>OPS</th>
      <th>AVG</th>
      <th>OBP</th>
      <th>SLG</th>
      <th>HR</th>
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
      <td>{{ p.avg }}</td>
      <td>{{ p.obp }}</td>
      <td>{{ p.slg }}</td>
      <td>{{ p.hr }}</td>
      <td>{{ p.pa }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

<script>
document.querySelectorAll('table.hr-table, table.ops-table').forEach(function(table) {
  var sortCol = -1, sortAsc = true;

  table.querySelectorAll('thead th').forEach(function(th, col) {
    th.addEventListener('click', function() {
      if (sortCol === col) {
        sortAsc = !sortAsc;
      } else {
        sortCol = col;
        sortAsc = false;
      }
      table.querySelectorAll('thead th').forEach(function(h) { delete h.dataset.sort; });
      th.dataset.sort = sortAsc ? '▲' : '▼';

      var tbody = table.querySelector('tbody');
      var rows = Array.from(tbody.querySelectorAll('tr'));
      rows.sort(function(a, b) {
        var aText = a.cells[col].textContent.trim();
        var bText = b.cells[col].textContent.trim();
        var aNum = parseFloat(aText);
        var bNum = parseFloat(bText);
        var numeric = !isNaN(aNum) && !isNaN(bNum);
        if (aText === '—') return 1;
        if (bText === '—') return -1;
        if (numeric) return sortAsc ? aNum - bNum : bNum - aNum;
        return sortAsc ? aText.localeCompare(bText) : bText.localeCompare(aText);
      });
      rows.forEach(function(row) { tbody.appendChild(row); });
    });
  });
});
</script>
