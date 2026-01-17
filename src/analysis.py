import quantstats as qs

def performance_report(returns):
    qs.extend_pandas()
    returns = returns / 100
    sharpe = qs.stats.sharpe(returns)
    max_dd = qs.stats.max_drawdown(returns)
    ann_return = qs.stats.cagr(returns)

    return {
        "Annualized Return": ann_return,
        "Sharpe Ratio": sharpe,
        "Max Drawdown": max_dd
    }
