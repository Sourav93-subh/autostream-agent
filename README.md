# 🚀 AutoStream Conversational AI Agent

An intelligent conversational AI agent built for **AutoStream**, a SaaS platform offering automated video editing tools for content creators.

This project simulates a real-world **Social-to-Lead Agentic Workflow**, capable of understanding user intent, answering product queries using a knowledge base (RAG), and capturing high-intent leads through structured conversation.

---

## 🧠 Features

* ✅ Intent Detection (Greeting, Pricing, High-Intent)
* 📚 RAG-based Knowledge Retrieval (JSON-based)
* 🔁 Stateful Multi-turn Conversation
* 🛠️ Lead Capture Tool Execution
* 💬 Interactive CLI Chat Interface

---

## 🏗️ Architecture Overview

The system follows a modular agent-based architecture:

1. **User Input**
2. **Intent Detection**
3. **Knowledge Retrieval (RAG)**
4. **State Management (Conversation Memory)**
5. **Lead Qualification Flow**
6. **Tool Execution (Lead Capture)**

The agent maintains context across multiple conversation turns using a custom state object, ensuring smooth transitions between queries and lead collection.

---

## ⚙️ Tech Stack

* Python 3.9+
* LangChain / LangGraph (conceptual alignment)
* JSON (Knowledge Base)
* CLI Interface

---

## 📂 Project Structure

```
autostream-agent/
│── main.py          # CLI interface
│── agent.py         # Core agent logic
│── intent.py        # Intent classification
│── rag.py           # Knowledge retrieval
│── tools.py         # Lead capture function
│── state.py         # Conversation memory
│── knowledge.json   # Knowledge base
│── requirements.txt
```

---

## ▶️ How to Run Locally

### 1. Clone the repository

git clone https://github.com/Sourav93-subh/autostream-agent
cd autostream-agent

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run the agent

python main.py

---

## 💬 Example Conversation

You: Hi
Bot: Hello! How can I help you today?

You: Tell me pricing
Bot: Basic Plan: $29/month...
Pro Plan: $79/month...

You: I want to try Pro plan
Bot: Great! What's your name?

You: Sourav
Bot: Please provide your email.

You: [test@gmail.com](mailto:test@gmail.com)
Bot: Which platform do you create content on?

You: YouTube
Bot: Lead captured successfully...

---

## 🛠️ Lead Capture Tool

```python
def mock_lead_capture(name, email, platform):
    print(f"Lead captured successfully: {name}, {email}, {platform}")
```

---

## 📱 WhatsApp Integration (Using Webhooks)

To integrate this agent with WhatsApp, we can use the WhatsApp Cloud API provided by Meta.

### 🔹 Integration Flow

1. User sends a message on WhatsApp
2. WhatsApp forwards the message to a backend server via **Webhook (HTTP POST)**
3. The backend extracts the message and passes it to the agent (`chat()` function)
4. The agent processes the request:

   * Detects intent
   * Retrieves knowledge (RAG)
   * Maintains conversation state
   * Collects lead information
5. The response is sent back to the user via WhatsApp API

### 🔹 Flow Diagram

User → WhatsApp → Webhook → Backend → Agent → Response → WhatsApp

### 🔹 Backend Implementation (Concept)

A backend server (Flask/FastAPI) would:

* Receive webhook requests
* Call the agent logic
* Send responses using WhatsApp API

### 🔹 Benefits

* Real-time interaction with users
* Automated lead generation
* Easily scalable for production systems

---

## 🎥 Demo

Watch the demo here:  
👉 https://www.loom.com/share/5c04020f098c41538ec639967beb5629

The demo video demonstrates:

* Pricing query handling
* Intent detection
* Lead capture flow
* Tool execution

---

## 📊 Evaluation Highlights

* ✔ Accurate intent classification
* ✔ Effective RAG implementation
* ✔ Clean state management
* ✔ Proper tool execution logic
* ✔ Real-world architecture

---

## 🚀 Future Improvements

* LLM-based intent detection
* Vector database for advanced RAG
* Web UI or WhatsApp deployment
* CRM integration

---

## 👨‍💻 Author

Sourav Subham
B.Tech CSE, VIT Bhopal
GitHub: https://github.com/Sourav93-subh
