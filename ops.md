---
layout: page
title: OPS Leaders
permalink: /ops/
---

# OPS Leaders

Ranking of MLB players by OPS (On-base Plus Slugging), updated regularly with the latest season statistics.

<style>
  table.ops-table {
    border-collapse: collapse;
    width: 100%;
    font-size: 1.05em;
    margin-bottom: 2em;
  }
  table.ops-table th, table.ops-table td {
    border: 1px solid #ddd;
    padding: 9px 12px;
    text-align: center;
  }
  table.ops-table th {
    background-color: #f4f4f4;
    font-weight: 700;
  }
  table.ops-table tr:nth-child(even) {
    background-color: #fafafa;
  }
  table.ops-table td:nth-child(2) a {
    color: inherit;
    text-decoration: none;
    border-bottom: 1px dashed #888;
  }
  table.ops-table td:nth-child(2) a:hover {
    border-bottom-color: #333;
  }
</style>

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
