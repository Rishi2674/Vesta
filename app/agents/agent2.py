# app/agents/agent2.py
from app.utils.groq_client import call_groq

async def agent2_response(message : str):
    # Placeholder response
    system_prompt = "You are a helpful real estate assistant who answers tenancy law and rental questions clearly and accurately. If location is provided, tailor your response accordingly."

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": message}
    ]
    agent_response = call_groq(messages)
    return await agent_response
