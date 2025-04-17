# app/agents/agent2.py

from app.utils.groq_client_2 import call_groq
from app.utils.shared_memory import get_history, add_message

async def agent2_response(message: str):
    system_prompt = {
        "role": "system",
        "content": (
            "You are a legal assistant for tenants. Answer user questions related to tenancy laws, "
            "contracts, deposit disputes, eviction, and landlord responsibilities. If the user provides a city "
            "or country, respond with location-specific guidance. Otherwise, provide general advice. "  
            "he user may refer to previous property inspections conducted by another agent. Use the assistant's earlier responses for context. "
            "If the user asks something unrelated to property or tenancy, ask them to clarify politely."
            "Avoid giving legal guarantees; explain options clearly and be short and concise."
        )
    }

    # Log user message
    add_message("user", message)

    # Prepare message list with history
    messages = [system_prompt] + get_history()
    # print("Messages:", messages)

    # Get response from Groq
    response = await call_groq(messages)

    # Save assistant response
    add_message("assistant", response)

    return response
