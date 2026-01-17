## How to Run:
1. Get a free Tiingo API key
2. On Mac, type in Terminal 
```bash
export TIINGO_API_KEY="YOUR_API_KEY"
```
For Windows:
```cmd
set TIINGO_API_KEY="YOUR_KEY"
echo %TIINGO_API_KEY%
```
3. 
```bash 
pip install -r requirements.txt
```
4. Run main.py

## Volatility Modeling & Time Series Analysis

This project explores how market volatility changes over time and how
volatility forecasts, such as GARCH(1,1), can be used to adjust risk in a simple trading strategy.

The focus is on learning Exam SRM & PA content rather than maximizing returns. If one wants to predict the direction in which a stock is going, other strategies are recommended.

### Key Features
- GARCH volatility forecasting of the SPY using ARCH package
- Volatility-targeted position sizing
- ADF and Ljung-Box diagnostics
- Walk-forward backtesting
- Performance analytics with QuantStats

### Results
- ~12% annualized return for 2005-2023
- Sharpe ratio ~1.2+
- ~38% volatility reduction vs buy-and-hold
