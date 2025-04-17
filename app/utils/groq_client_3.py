# app/utils/groq_client.py
# At the top of groq_client.py
from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY_AGENT_2")
client = Groq(api_key=GROQ_API_KEY)  # Ideally load from environment variable

def groq_chat(messages: str, model: str = "llama-3.1-8b-instant"):
    """
    Call Groq ChatCompletion with a default system prompt and message history.
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that returns concise, clear and relevant information."},
            {"role": "user", "content": messages}
        ],
        temperature=0.2
    )
    return response.choices[0].message.content.strip()
   
