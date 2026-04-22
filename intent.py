def detect_intent(user_input):
    text = user_input.lower()

    if any(word in text for word in ["hi", "hello"]):
        return "greeting"

    elif any(word in text for word in ["price", "plan", "cost"]):
        return "pricing"

    elif any(word in text for word in ["buy", "subscribe", "try", "sign up"]):
        return "high_intent"

    return "other"