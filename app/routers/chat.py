# app/routers/chat.py
from fastapi import APIRouter, UploadFile, File, Form
from typing import Optional
from app.agents.agent_router import route_message

router = APIRouter()

@router.post("/chat")
async def chat_endpoint(
    message: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None)
):
    response = await route_message(message=message, image=image)
    return {"response": response}
