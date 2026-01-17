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
    vol = forecast.variance.iloc[-1].values[0] ** 0.5
    return vol
