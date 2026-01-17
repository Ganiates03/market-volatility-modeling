from src.data_loader import load_price_data
from src.diagnostics import adf_test, ljung_box_test
from src.backtest import run_backtest
from src.utils import performance_report

def main():
    data = load_price_data()

    print("ADF Test:", adf_test(data['returns']))
    print("Ljung-Box Test:")
    print(ljung_box_test(data['returns']))

    results = run_backtest(data)
    stats = performance_report(results['strategy_returns'])

    print("\nPerformance Metrics")
    for k, v in stats.items():
        print(f"{k}: {v:.2%}")

if __name__ == "__main__":
    main()
