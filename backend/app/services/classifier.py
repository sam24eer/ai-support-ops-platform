from typing import Tuple

def classify_intent(text: str) -> Tuple[str, float]:
    """
    Returns (intent, confidence)
    Stubbed logic for MVP.
    """

    text_lower = text.lower()

    if "password" in text_lower:
        return "password_reset", 0.92

    if "refund" in text_lower or "money" in text_lower:
        return "refund_request", 0.78

    if "error" in text_lower or "bug" in text_lower:
        return "technical_issue", 0.65

    return "general_inquiry", 0.55
