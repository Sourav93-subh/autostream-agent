def detect_intent(user_input):
    text = user_input.lower()

    # ✅ High intent FIRST (priority)
    if any(word in text for word in ["buy", "subscribe", "try", "sign up", "start", "want", "interested"]):
        return "high_intent"

    # Greeting
    elif any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    # Pricing / product queries
    elif any(word in text for word in ["price", "pricing", "plan", "cost"]):
        return "pricing"

    return "other"