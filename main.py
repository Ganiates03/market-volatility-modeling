from src.analysis import compare_performance
from src.data_loader import load_price_data
from src.diagnostics import adf_test, ljung_box_test
from src.backtest import run_backtest
from src.baseline import buy_and_hold
from src.plots import (
    plot_equity_curves,
    plot_rolling_volatility,
    plot_position_sizes
)

def main():
    data = load_price_data()

    print("ADF Test:", adf_test(data['returns']))
    print("Ljung-Box Test:")
    print(ljung_box_test(data['returns']))

    strategy_results, start_idx = run_backtest(data, target_vol=0.15, lookback=500, ma_window=200)
    baseline_results = buy_and_hold(data, start_idx)

    comparison = compare_performance(
        strategy_results['strategy_returns'],
        baseline_results['strategy_returns']
    )

    print("\nPerformance Comparison")
    for k, v in comparison.items():
        if "Max DD" in k:
            print(f"{k}: {v:.2%}")
        elif "CAGR" in k:
            print(f"{k}: {v:.2%}")
        elif "Volatility" in k:
            print(f"{k}: {v:.2%}")
        else:
            print(f"{k}: {v:.4f}")

    # Plots
    plot_equity_curves(
        strategy_results['strategy_returns'],
        baseline_results['strategy_returns']
    )

    plot_rolling_volatility(
        strategy_results['strategy_returns'],
        baseline_results['strategy_returns']
    )

    plot_position_sizes(strategy_results['position'])

if __name__ == "__main__":
    main()
