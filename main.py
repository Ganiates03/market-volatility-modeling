from src.data_loader import load_price_data
from src.diagnostics import adf_test, ljung_box_test
from src.backtest import run_backtest
from src.baseline import buy_and_hold
from src.analysis import compare_performance
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

    strategy_results, start_idx = run_backtest(data)
    baseline_results = buy_and_hold(data, start_idx)

    comparison = compare_performance(
        strategy_results['strategy_returns'],
        baseline_results['strategy_returns']
    )

    print("\nPerformance Comparison")
    for k, v in comparison.items():
        print(f"{k}: {v:.2%}")

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
