## How to Run:
1. Get a free Tiingo API key
2. Set it as an environmental variable.
On Mac, type in Terminal 
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
volatility forecasts, such as GARCH(1,1), can be used to adjust risk exposure in a simple trading strategy.

The focus is on learning Exam SRM & PA content rather than maximizing returns. If one wants to predict the direction in which a stock is going, other strategies are recommended.

### Key Features
- GARCH volatility forecasting of the SPY using ARCH package
- Volatility-targeted position sizing w/ target of 15%
- ADF and Ljung-Box diagnostics
- Walk-forward backtesting
- Downtrend exposure filter
- Performance analytics with QuantStats

### Results for 2005-2023
- ~8% increase in CAGR
- Sharpe ratio ~1.0+
- ~47% max drawdown reduction
- Calmar ~1.5 increase
- ~50% (conditional) volatility reduction vs buy-and-hold
<img width="456" height="446" alt="image" src="https://github.com/user-attachments/assets/aea6960c-89aa-41f5-bc17-008135b1f40d" />
<img width="1640" height="570" alt="image" src="https://github.com/user-attachments/assets/542da5d6-7f4d-43d7-93c3-70c2582a14ac" />
<img width="1200" height="600" alt="image" src="https://github.com/user-attachments/assets/5d4c4814-c807-4b29-812b-c390ca261795" />
<img width="1200" height="600" alt="image" src="https://github.com/user-attachments/assets/8010f7e4-94aa-4432-a7b9-9b727012f2b5" />
<img width="1200" height="400" alt="image" src="https://github.com/user-attachments/assets/2ae8c3ec-ee98-4193-8c4c-879471039320" />



