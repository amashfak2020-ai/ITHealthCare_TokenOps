def extract_required_evidence(clinical_summary, payer_rules):
    return {
        "summary_length": len(str(clinical_summary)),
        "rules_checked": len(payer_rules) if hasattr(payer_rules, '__len__') else 0
    }


def prior_auth_pipeline(request_type, clinical_summary, payer_rules):
    return {
        "request_type": request_type,
        "required_evidence": extract_required_evidence(clinical_summary, payer_rules),
        "decision_support": "approved_if_all_criteria_met",
        "manual_review": False
    }
