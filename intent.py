def detect_intent(user_input):
    text = user_input.lower()

    # Greeting
    if any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    # Pricing / product queries
    elif any(word in text for word in ["price", "pricing", "plan", "cost"]):
        return "pricing"

    # High intent (lead)
    elif any(word in text for word in ["buy", "subscribe", "try", "sign up", "start"]):
        return "high_intent"

    return "other"