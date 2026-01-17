import os
import json
import yfinance as yf

# List of stock tickers
stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]

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
    
    # Save stock prices to `_data/stock_prices.json`
    with open("_data/stock_prices.json", "w") as json_file:
        json.dump(stock_prices, json_file, indent=4)
    print("Stock prices saved to _data/stock_prices.json")
