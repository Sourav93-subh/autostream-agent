import json

def load_knowledge():
    with open("knowledge.json") as f:
        return json.load(f)

def retrieve_answer(query):
    data = load_knowledge()
    query = query.lower()

    # Pricing / Plans
    if any(word in query for word in ["price", "pricing", "plan", "cost"]):
        basic = data["pricing"]["basic"]
        pro = data["pricing"]["pro"]

        return f"""
Basic Plan: {basic['price']} ({", ".join(basic['features'])})
Pro Plan: {pro['price']} ({", ".join(pro['features'])})
"""

    # Refund policy
    elif "refund" in query:
        return data["policies"]["refund"]

    # Support policy
    elif "support" in query:
        return data["policies"]["support"]

    return "Sorry, I couldn't find that information."