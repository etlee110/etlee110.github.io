---
layout: page
title: Stocks
permalink: /stocks/
---

# Stock Prices

The table below is automatically updated with the latest stock prices for some oniasdf

<style>
  table.stock-table {
      border-collapse: collapse;
      width: 100%;
      font-size: 1.2em;
  }
  table.stock-table th, table.stock-table td {
      border: 1px solid #ddd;
      padding: 8px;
      text-align: center;
  }
  table.stock-table th {
      background-color: #f4f4f4;
      font-weight: bold;
  }
  table.stock-table tr:nth-child(even) {
      background-color: #f9f9f9;
  }
</style>

## Current Stock Prices

<table class="stock-table">
  <thead>
    <tr>
      <th>Stock Ticker</th>
      <th>Price (USD)</th>
    </tr>
  </thead>
  <tbody>
    {% assign stock_prices = site.data.stock_prices %}
    {% for ticker in stock_prices %}
    <tr>
      <td>{{ stock_prices[ticker].name }}</td>
      <td>${{ stock_prices[ticker].price }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
