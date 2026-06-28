from examples.token_cost_calculator import estimate_monthly_savings


def test_estimate_monthly_savings_returns_positive_savings():
    result = estimate_monthly_savings(1000, 4000, 2000, 0.01)
    assert result["monthly_savings"] > 0
