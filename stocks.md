---
layout: page
title: Stock Prices
permalink: /stocks
---

# Stock Prices

{% assign stock_prices = site.data.stock_prices %}

| Ticker | Price (USD) |
|--------|-------------|
{% for stock in stock_prices %}
| {{ stock.name }} | {{ stock.price }} |
{% endfor %}
