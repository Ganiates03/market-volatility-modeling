import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_equity_curves(strategy_returns, baseline_returns):
    strat_equity = (1 + strategy_returns / 100).cumprod()
    base_equity = (1 + baseline_returns / 100).cumprod()

    plt.figure(figsize=(12, 6))
    plt.plot(strat_equity, label="Unleveraged GARCH + Trend Filter")
    plt.plot(base_equity, label="Buy & Hold", linestyle="--")
    plt.title("Equity Curve Comparison")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_rolling_volatility(strategy_returns, baseline_returns, window=60):
    strat_vol = strategy_returns.rolling(window).std() * np.sqrt(252)
    base_vol = baseline_returns.rolling(window).std() * np.sqrt(252)

    plt.figure(figsize=(12, 6))
    plt.plot(strat_vol, label="Strategy Volatility")
    plt.plot(base_vol, label="Buy & Hold Volatility", linestyle="--")
    plt.title("Rolling Annualized Volatility")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_position_sizes(positions):
    plt.figure(figsize=(12, 4))
    plt.plot(positions, color="purple")
    plt.title("Dynamic Position Sizing (Unleveraged Volatility Targeting)")
    plt.ylabel("Exposure (0-1)")
    plt.grid(True)
    plt.show()
