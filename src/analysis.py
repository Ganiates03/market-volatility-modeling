import quantstats as qs

def compare_performance(strategy_returns, baseline_returns):
    qs.extend_pandas()

    strategy = strategy_returns / 100
    baseline = baseline_returns / 100

    comparison = {
        "Strategy CAGR": qs.stats.cagr(strategy),
        "Baseline CAGR": qs.stats.cagr(baseline),
        "Strategy Sharpe": qs.stats.sharpe(strategy),
        "Baseline Sharpe": qs.stats.sharpe(baseline),
        "Strategy Max DD": qs.stats.max_drawdown(strategy),
        "Baseline Max DD": qs.stats.max_drawdown(baseline),
        "Strategy Calmar": qs.stats.calmar(strategy),
        "Baseline Calmar": qs.stats.calmar(baseline),
        "Strategy Volatility": qs.stats.volatility(strategy),
        "Baseline Volatility": qs.stats.volatility(baseline),
    }

    return comparison
