import pandas as pd

def buy_and_hold(data, start_index):
    returns = data['returns'].iloc[start_index:]
    bh = pd.DataFrame(index=returns.index)
    bh['strategy_returns'] = returns
    bh['position'] = 1.0
    return bh
