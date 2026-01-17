from statsmodels.tsa.stattools import adfuller
from statsmodels.stats.diagnostic import acorr_ljungbox

def adf_test(series):
    result = adfuller(series)
    return {
        "ADF Statistic": result[0],
        "p-value": result[1]
    }

def ljung_box_test(series, lags=10):
    return acorr_ljungbox(series, lags=lags, return_df=True)
