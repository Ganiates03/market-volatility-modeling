import pandas as pd
from src.garch_model import fit_garch, forecast_volatility
from src.strategy import position_size

def run_backtest(data, target_vol=10.0, lookback=500):
    returns = data['returns']
    positions = []
    realized_returns = []

    for t in range(lookback, len(returns)):
        train_returns = returns.iloc[t-lookback:t]
        garch = fit_garch(train_returns)
        vol_forecast = forecast_volatility(garch)

        pos = position_size(target_vol, vol_forecast)
        strat_ret = pos * returns.iloc[t]

        positions.append(pos)
        realized_returns.append(strat_ret)

    result = pd.DataFrame({
        "strategy_returns": realized_returns,
        "position": positions
    }, index=returns.index[lookback:])

    return result
