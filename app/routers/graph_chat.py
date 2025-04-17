# app/routers/chatbot.py

from fastapi import APIRouter, UploadFile, Form, File
from app.langgraph.graph import build_graph
from app.langgraph.graph_state import GraphState
import base64
from typing import Optional
from app.utils.chat_history import chat_history  # import global memory


router = APIRouter()
graph = build_graph()

@router.post("/chat")
async def chat(
    message: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None)
):
    # Create initial message list
    messages = {"role": "user", "content": message if message else ""}
    print(messages)
    # If image is included, convert to base64 and attach
    if image:
        image_bytes = await image.read()
        encoded = base64.b64encode(image_bytes).decode("utf-8")
        messages["image"] = encoded

    # Create initial state
    print(f"Received message: {message}")
    print(f"Received image: {image is not None}")
    print(f"Image size: {len(encoded) if image else 'No image'} bytes")
    #print("Messages:", messages)
    
    chat_history.append(messages)
    
    state = GraphState(
        messages=list(chat_history),
        current_agent="agent2"
    )

    # Run the LangGraph
    final_state = await graph.ainvoke(state)

    # Get the last assistant message
    response_msg = next((m for m in reversed(final_state["messages"]) if m["role"] == "assistant"), None)
    
    if response_msg:
        chat_history.append(response_msg)
    return {
        "response": response_msg["content"] if response_msg else "No response"
    }
