from examples.clinical_summary import build_clinical_summary_prompt


def test_build_clinical_summary_prompt_contains_context():
    prompt = build_clinical_summary_prompt(
        {"patient_id": "demo"},
        ["This is a sufficiently long note section for testing prompt creation."]
    )
    assert "Patient Context" in prompt
    assert "Relevant Notes" in prompt
