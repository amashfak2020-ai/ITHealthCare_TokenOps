from examples.prior_auth_pipeline import prior_auth_pipeline


def test_prior_auth_pipeline_returns_expected_keys():
    result = prior_auth_pipeline("imaging", "summary", ["rule1", "rule2"])
    assert "request_type" in result
    assert "required_evidence" in result
    assert "decision_support" in result
    assert "manual_review" in result
