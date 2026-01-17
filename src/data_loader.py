import os
import pandas as pd
import requests
from dotenv import load_doatenv

load_dotenv()

def load_price_data(ticker="SPY", start="2005-01-01", end="2023-12-31"):
    api_key = os.getenv("TIINGO_API_KEY")
    if not api_key:
        raise ValueError("TIINGO_API_KEY not found. Set it as an environment variable.")

    url = (
        f"https://api.tiingo.com/tiingo/daily/{ticker}/prices"
        f"?startDate={start}&endDate={end}&resampleFreq=d&token={api_key}"
    )

    response = requests.get(url)
    if response.status_code != 200:
        raise ConnectionError(f"Tiingo request failed: {response.status_code} - {response.text}")

    data = pd.DataFrame(response.json())

    if data.empty:
        raise ValueError("No data returned from Tiingo. Check your ticker or date range.")

    data["date"] = pd.to_datetime(data["date"])
    data.set_index("date", inplace=True)

    data = data[["close"]]
    data.rename(columns={"close": "price"}, inplace=True)
    data["returns"] = 100 * data["price"].pct_change()

    return data.dropna()
