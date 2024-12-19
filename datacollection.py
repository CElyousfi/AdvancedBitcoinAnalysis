import yfinance as yf
import os

def fetch_data(ticker, filename):
    os.makedirs("data/raw", exist_ok=True)
    df = yf.download(ticker, period="max", interval="1d")
    df.index.name = 'Date'
    df.to_csv(f"data/raw/{filename}")
    print(f"Data for {ticker} saved to data/raw/{filename}")

if __name__ == "__main__":
    # Bitcoin
    fetch_data("BTC-USD", "bitcoin_data.csv")
    # Dow Jones
    fetch_data("^DJI", "dow_data.csv")
    # Nasdaq Composite
    fetch_data("^IXIC", "nasdaq_data.csv")
    # S&P 500
    fetch_data("^GSPC", "sp500_data.csv")
