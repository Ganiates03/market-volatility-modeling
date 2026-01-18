import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_equity_curves(strategy_returns, baseline_returns):
    strat_equity = (1 + strategy_returns / 100).cumprod()
    base_equity = (1 + baseline_returns / 100).cumprod()


    plt.figure(figsize=(12, 6))
    plt.plot(strat_equity, label="GARCH + Trend Filter")
    plt.plot(base_equity, label="Buy & Hold", linestyle="--")
    plt.title("Wealth Accumulation Chart")
    plt.ylabel("$ (millions)")

    def label_endpoint(series, dy=0.0):
        x = series.index[-1]
        y = series.iloc[-1]
        plt.scatter([x], [y], s=25)
        plt.annotate(
            f"${y:.2f} million",
            xy=(x, y),
            xytext=(8, dy),
            textcoords="offset points",
            va="center",
            ha="left",
            fontsize=10
        )
    label_endpoint(strat_equity,dy=10)
    label_endpoint(base_equity, dy=-10)
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_rolling_volatility(strategy_returns, baseline_returns, window=60):
    strat_vol = strategy_returns.rolling(window).std() * np.sqrt(252)
    base_vol = baseline_returns.rolling(window).std() * np.sqrt(252)

    plt.figure(figsize=(12, 6))
    plt.plot(strat_vol, label="Strategy Volatility")
    plt.plot(base_vol, label="Buy & Hold Volatility", linestyle="--")
    plt.ylabel("% std.dev")
    plt.title("Rolling Annualized Volatility")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_position_sizes(positions, start="2005-01-01", end="2023-12-31"):
    if not isinstance(positions.index, pd.DatetimeIndex):
        raise ValueError("positions must have a DatetimeIndex")

    filtered = positions.loc[start:end]

    plt.figure(figsize=(12, 4))
    plt.plot(filtered, color="purple")
    plt.title(f"Dynamic Position Sizing ({start} to {end})")
    plt.ylabel("Exposure (0–1)")
    plt.grid(True)
    plt.show()
