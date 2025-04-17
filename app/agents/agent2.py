# app/agents/agent2.py

from app.utils.groq_client_2 import call_groq
from app.utils.shared_memory import get_history, add_message

async def agent2_response(message: list[dict]):
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

    cleaned_messages = []
    # print("Calling agent 2")
    # print(message)
    for msg in message:
        if "image" in msg:
            msg = msg.copy()
            msg.pop("image")  # remove invalid image field

        if isinstance(msg.get("content"), str):
            cleaned_messages.append(msg)
        else:
            # Skip or convert badly formed ones
            continue

    full_messages = [system_prompt] + cleaned_messages

    response = await call_groq(full_messages)
    return response
  
