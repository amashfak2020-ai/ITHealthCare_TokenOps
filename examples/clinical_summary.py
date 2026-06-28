from typing import Dict, List


def build_clinical_summary_prompt(patient_context: Dict, note_sections: List[str]) -> str:
    relevant_sections = [section.strip() for section in note_sections if section and len(section.strip()) > 30]
    compressed_context = "\n".join(relevant_sections[:5])

    prompt = f"""
You are a healthcare documentation assistant.
Summarize only clinically relevant updates.
Return output in JSON with keys: chief_complaint, assessment, plan, risks.

Patient Context:
{patient_context}

Relevant Notes:
{compressed_context}
""".strip()

    return prompt
