from fastapi import APIRouter, UploadFile, Form, File
from typing import Optional
from app.langgraph.graph import build_graph
from app.langgraph.graph_state import GraphState
from app.utils.chat_history import chat_history
import base64

router = APIRouter()
graph = build_graph()

@router.post("/chat")
async def chat(
    message: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None),
    search_required: Optional[bool] = Form(False)  # 👈 NEW: receive from frontend
):
    messages = {"role": "user", "content": message if message else ""}
    
    if image:
        image_bytes = await image.read()
        encoded = base64.b64encode(image_bytes).decode("utf-8")
        messages["image"] = encoded

    print(f"Received message: {message}")
    print(f"Received image: {image is not None}")
    if image:
        print(f"Image size: {len(encoded)} bytes")
    
    chat_history.append(messages)
    
    state = GraphState(
        messages=list(chat_history),
        current_agent="agent2",
        search_required=search_required  # 👈 NEW
    )

    final_state = await graph.ainvoke(state)

    response_msg = next((m for m in reversed(final_state["messages"]) if m["role"] == "assistant"), None)

    if response_msg:
        chat_history.append(response_msg)

    return {
        "response": response_msg["content"] if response_msg else "No response"
    }
