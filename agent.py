from intent import detect_intent
from rag import retrieve_answer
from tools import mock_lead_capture
from state import AgentState

# Initialize global state
state = AgentState()

def chat(user_input):
    global state

    # -------------------------------
    # STEP 1: Handle ongoing lead flow
    # -------------------------------
    if state.stage == "ask_name":
        state.name = user_input
        state.stage = "ask_email"
        return "Please provide your email."

    elif state.stage == "ask_email":
        state.email = user_input
        state.stage = "ask_platform"
        return "Which platform do you create content on? (YouTube, Instagram, etc.)"

    elif state.stage == "ask_platform":
        state.platform = user_input

        # ✅ Call tool ONLY after all data collected
        mock_lead_capture(state.name, state.email, state.platform)

        state.stage = "done"
        return "✅ You're all set! Our team will contact you soon."

    # -------------------------------
    # STEP 2: Detect intent
    # -------------------------------
    intent = detect_intent(user_input)
    state.intent = intent

    # -------------------------------
    # STEP 3: Respond based on intent
    # -------------------------------
    if intent == "greeting":
        return "Hello! 👋 How can I help you today?"

    elif intent == "pricing":
        return retrieve_answer(user_input)

    elif intent == "high_intent":
        state.stage = "ask_name"
        return "Great choice! 🚀 Let's get you started.\nWhat's your name?"

    # -------------------------------
    # DEFAULT RESPONSE
    # -------------------------------
    return "I'm not sure I understood that. Can you rephrase?"