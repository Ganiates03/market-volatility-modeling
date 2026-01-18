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

### Results for 2005-2023
- ~8% increase in CAGR
- Sharpe ratio ~1.0+
- ~47% max drawdown reduction
- Calmar ~1.5 increase
- ~50% (conditional) volatility reduction vs buy-and-hold
<img width="1200" height="600" alt="image" src="https://github.com/user-attachments/assets/5d4c4814-c807-4b29-812b-c390ca261795" />
<img width="1200" height="600" alt="image" src="https://github.com/user-attachments/assets/8010f7e4-94aa-4432-a7b9-9b727012f2b5" />
<img width="1200" height="400" alt="image" src="https://github.com/user-attachments/assets/2ae8c3ec-ee98-4193-8c4c-879471039320" />



