# app/routes/chat.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.agent2 import agent2_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
async def chat_endpoint(payload: ChatRequest):
    message = payload.message
    response = await agent2_response(message)
    return {"response": response}
