---
layout: page
title: Stocks
permalink: /stocks/
---

# Stock Prices

The table below is automatically updated with the latest stock prices.

<style>
  table.stock-table {
      border-collapse: collapse;
      width: 100%;
      font-size: 1.1em;
  }
  table.stock-table th, table.stock-table td {
      border: 1px solid #ddd;
      padding: 10px;
      text-align: center;
  }
  table.stock-table th {
      background-color: #f4f4f4;
      font-weight: 700;
  }
  table.stock-table tr:nth-child(even) {
      background-color: #fafafa;
  }
</style>

## Current Stock Prices

{% assign sp = site.data.stock_prices %}
<p><em>Last fetched {{ sp.fetched_at_et }}</em></p>

<table class="stock-table">
  <thead>
    <tr>
      <th>Stock Ticker</th>
      <th>Price (USD)</th>
    </tr>
  </thead>
  <tbody>
    {% for item in sp.stocks %}
      {% assign ticker = item[0] %}
      {% assign data = item[1] %}
      <tr>
        <td>{{ data.name | default: ticker }}</td>
        <td>${{ data.price }}</td>
      </tr>
    {% endfor %}
  </tbody>
</table>
