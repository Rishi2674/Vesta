# app/agents/agent2.py

from app.utils.groq_client_2 import call_groq

# Global memory for single user
conversation_history = []
MAX_HISTORY = 6

async def agent2_response(message: str):
    system_prompt = {
        "role": "system",
        "content": (
            "You are a legal assistant for tenants. Answer user questions related to tenancy laws, "
            "contracts, deposit disputes, eviction, and landlord responsibilities. If the user provides a city "
            "or country, respond with location-specific guidance. Otherwise, provide general advice. "  
            "If the user asks something unrelated to property or tenancy, ask them to clarify politely."
            "Avoid giving legal guarantees; explain options clearly and be short and concise."
        )
    }

    # Append current user message
    conversation_history.append({"role": "user", "content": message})

    # Trim to last MAX_HISTORY messages if needed
    if len(conversation_history) > MAX_HISTORY:
        del conversation_history[0:len(conversation_history) - MAX_HISTORY]

    # Full message payload for LLM
    messages = [system_prompt] + conversation_history

    # Get LLM response
    reply = await call_groq(messages)

    # Append assistant response to memory
    conversation_history.append({"role": "assistant", "content": reply})

    # Again trim if necessary
    if len(conversation_history) > MAX_HISTORY:
        del conversation_history[0:len(conversation_history) - MAX_HISTORY]

    return reply
