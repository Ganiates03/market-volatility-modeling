from arch import arch_model

def fit_garch(returns):
    model = arch_model(
        returns,
        mean="Zero",
        vol="GARCH",
        p=1,
        q=1,
        dist="normal"
    )
    res = model.fit(disp="off")
    return res

def forecast_volatility(model_result, horizon=1):
    forecast = model_result.forecast(horizon=horizon)
    daily_var = forecast.variance.iloc[-1].values[0]
    daily_vol_pct = daily_var ** 0.5

    annual_vol_decimal = (daily_vol_pct / 100) * np.sqrt(252)
    return annual_vol_decimal
