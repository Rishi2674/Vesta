from fastapi import APIRouter, UploadFile, File, Form
from typing import Optional
from app.agents.agent1 import agent1_response
from app.agents.agent2 import agent2_response  # hypothetical
import base64

router = APIRouter()

@router.post("/chat")
async def chat_endpoint(
    message: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None)
):
    # If image is uploaded, use Agent 1
    if image is not None:
        image_bytes = await image.read()
        base64_image = base64.b64encode(image_bytes).decode('utf-8')
        return {
            "agent": "Agent 1 - Property Inspector",
            "response": agent1_response(base64_image, user_text=message or "")
        }

    # Fallback to Agent 2
    if message:
        response = await agent2_response(message)
        return {
            "agent": "Agent 2 - Tenancy FAQ Bot",
            "response": response
        }

    return {"error": "No input provided"}
