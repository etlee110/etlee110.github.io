import os
import json
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import yfinance as yf

# List of stock tickers
stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "COF", "CRSP", "DAL", "SE", "UBER", "DIDIY", "EDIT", "JPM", "QXO"]

def fetch_stock_prices(ticker_list):
    """
    Fetch the current stock prices for a list of companies.
    """
    prices = {}
    for ticker in ticker_list:
        try:
            stock = yf.Ticker(ticker)
            price = stock.info["regularMarketPrice"]  # Get current stock price
            prices[ticker] = {"name": ticker, "price": price}
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
    return prices

if __name__ == "__main__":
    stock_prices = fetch_stock_prices(stocks)

    # Print the stock prices for debugging
    print("Current Stock Prices:")
    for ticker, data in stock_prices.items():
        print(f"{ticker}: ${data['price']}")

    # Ensure the `_data` directory exists
    os.makedirs("_data", exist_ok=True)

    now_utc = datetime.now(timezone.utc)
    now_et = now_utc.astimezone(ZoneInfo("America/New_York"))

    # Wrap with fetched_at + stocks
    payload = {
        "fetched_at_utc": now_utc.isoformat(),
        "fetched_at_et": now_et.strftime("%B %-d, %Y at %-I:%M %p %Z"),
        "stocks": stock_prices
    }

    # Save to `_data/stock_prices.json`
    with open("_data/stock_prices.json", "w") as json_file:
        json.dump(payload, json_file, indent=4)

    print("Stock prices saved to _data/stock_prices.json")
