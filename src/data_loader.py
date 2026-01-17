import yfinance as yf
import pandas as pd

def load_price_data(ticker="SPY", start="2005-01-01", end="2023-12-31"):
    data = yf.download(ticker, start=start, end=end)
    data = data[['Adj Close']]
    data.rename(columns={'Adj Close': 'price'}, inplace=True)
    data['returns'] = 100 * data['price'].pct_change().dropna()
    return data.dropna()
