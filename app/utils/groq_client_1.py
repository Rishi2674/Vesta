import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY_AGENT_1")

client = Groq(api_key=GROQ_API_KEY)

def call_groq_vision_model(base64_image: str, user_text: str = "") -> str:
    prompt = f"You are a property inspection assistant. {user_text} Describe any visible issues with the image and suggest potential fixes."

    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        },
                    },
                ],
            }
        ],
        temperature=0.8,
        max_completion_tokens=1024,
        stream=False,
    )

    return response.choices[0].message.content