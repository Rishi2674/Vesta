from fastapi import APIRouter, UploadFile, File, Form
from typing import Optional
from app.agents.agent_router import route_message
# hypothetical
import base64

router = APIRouter()

@router.post("/chat")
async def chat_endpoint(
    message: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None)
):
    # If image is uploaded, use Agent 1
    base64_image = None
    
    if image is not None:
        image_bytes = await image.read()
        base64_image = base64.b64encode(image_bytes).decode('utf-8')

    print(f"Received message: {message}")
    print(f"Received image: {base64_image is not None}")
    print(f"Image size: {len(base64_image) if base64_image else 'No image'} bytes")
    route_message_response = await route_message(message, base64_image)
    if route_message_response:
        return {"response": route_message_response}

    return {"error": "No input provided"}
