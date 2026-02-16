def make_decision(intent: str, confidence: float) -> str:
    """
    Returns decision action.
    """

    AUTO_RESOLVE_INTENTS = {"password_reset"}
    CONFIDENCE_THRESHOLD = 0.80

    if intent in AUTO_RESOLVE_INTENTS and confidence >= CONFIDENCE_THRESHOLD:
        return "auto_resolve"

    return "escalate"
