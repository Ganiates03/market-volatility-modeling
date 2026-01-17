import numpy as np

def position_size(target_vol, forecast_vol, max_leverage=2.0):
    """
    Volatility targeting position sizing
    """
    size = target_vol / forecast_vol
    return np.clip(size, 0, max_leverage)
