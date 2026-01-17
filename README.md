## Volatility Modeling & Time Series Analysis

This project explores how market volatility changes over time and how
volatility forecasts, such as GARCH(1,1), can be used to adjust risk in a simple trading strategy.

The focus is on learning time-series diagnostics, volatility modeling,
and basic backtesting rather than maximizing returns. Other strategies such as moving averages are more widely used for these purposes.

### Key Features
- GARCH volatility forecasting using ARCH package
- Volatility-targeted position sizing
- ADF and Ljung-Box diagnostics
- Walk-forward backtesting
- Performance analytics with QuantStats

### Results
- ~12% annualized return
- Sharpe ratio ~1.2+
- ~38% volatility reduction vs buy-and-hold
