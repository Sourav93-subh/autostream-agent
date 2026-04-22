import json

def load_knowledge():
    with open("knowledge.json") as f:
        return json.load(f)

def retrieve_answer(query):
    data = load_knowledge()

    if "price" in query.lower():
        return f"""
Basic Plan: $29/month (10 videos, 720p)
Pro Plan: $79/month (Unlimited videos, 4K, AI captions)
"""
    elif "refund" in query.lower():
        return data["policies"]["refund"]
    elif "support" in query.lower():
        return data["policies"]["support"]

    return "Sorry, I couldn't find that information."