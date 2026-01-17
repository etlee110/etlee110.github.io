import yfinance as yf

# List of company stock ticker symbols
stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]  # Add your companies here

def fetch_stock_prices(ticker_list):
    """
    Fetch the current stock prices for a list of companies.
    """
    prices = {}
    for ticker in ticker_list:
        try:
            stock = yf.Ticker(ticker)
            price = stock.info["regularMarketPrice"]  # Get current stock price
            prices[ticker] = price
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
    return prices

if __name__ == "__main__":
    stock_prices = fetch_stock_prices(stocks)
    print("Current Stock Prices:")
    for ticker, price in stock_prices.items():
        print(f"{ticker}: ${price}")
