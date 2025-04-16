# app/clients/groq_client.py

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY_AGENT_2")
# Load key and init client
client = Groq(api_key=GROQ_API_KEY)

async def call_groq(messages, model="llama3-70b-8192", temperature=0.7):

    prompt = f"You are a legal assistant for tenants. Answer user questions related to tenancy laws, contracts, deposit disputes, eviction, and landlord responsibilities.If the user provides a city or country, respond with location-specific guidance. Otherwise, provide general advice. Avoid giving legal guarantees; explain options clearly and be short and concise.User message: {messages}"

    chat_completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    return chat_completion.choices[0].message.content
