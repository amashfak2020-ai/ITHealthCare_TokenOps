def estimate_monthly_savings(requests_per_month, baseline_tokens, optimized_tokens, cost_per_1k_tokens):
    baseline_cost = (requests_per_month * baseline_tokens / 1000) * cost_per_1k_tokens
    optimized_cost = (requests_per_month * optimized_tokens / 1000) * cost_per_1k_tokens
    savings = baseline_cost - optimized_cost

    return {
        "baseline_cost": round(baseline_cost, 2),
        "optimized_cost": round(optimized_cost, 2),
        "monthly_savings": round(savings, 2)
    }
