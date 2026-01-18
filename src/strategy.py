import numpy as np

def position_size(
    target_vol,
    forecast_vol,
    price,
    trend_ma
):
    """
    Unlevered GARCH volatility targeting with trend filter

    Returns position size in [0, 1]
    """

    # Trend filter: no exposure in downtrend
    if price <= trend_ma or np.isnan(trend_ma):
        return 0.0

    # Unlevered volatility targeting
    size = target_vol / forecast_vol

    # Cap at 1.0 (NO leverage)
    return np.clip(size, 0.0, 1.0)
