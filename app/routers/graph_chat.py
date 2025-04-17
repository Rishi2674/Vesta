# app/routers/graph_chat.py - Add more debugging
from fastapi import APIRouter, UploadFile, Form, File, Request
from typing import Optional
from app.langgraph.graph import build_graph
from app.langgraph.graph_state import GraphState
from app.utils.chat_history import chat_history
import base64

router = APIRouter()
graph = build_graph()

@router.post("/chat")
async def chat(
    request: Request,
    message: Optional[str] = Form(None),
    image: Optional[UploadFile] = File(None),
    search_required: Optional[str] = Form(None)  # Changed to string
):
    # Debug incoming request
    print(f"DEBUG - Endpoint hit: /chat")
    print(f"DEBUG - Message: {message}")
    print(f"DEBUG - Image: {image is not None}")
    print(f"DEBUG - Search Required (raw): {search_required}")
    
    # Convert search_required string to boolean
    search_required_bool = False
    if search_required is not None:
        if search_required.lower() == "true":
            search_required_bool = True
            print("DEBUG - Search is enabled")
    
    messages = {"role": "user", "content": message if message else ""}
    
    if image:
        image_bytes = await image.read()
        encoded = base64.b64encode(image_bytes).decode("utf-8")
        messages["image"] = encoded
        print(f"DEBUG - Image encoded, size: {len(encoded)} bytes")
    
    print(f"DEBUG - Adding message to chat history")
    chat_history.append(messages)
    
    print(f"DEBUG - Creating GraphState")
    state = GraphState(
        messages=list(chat_history),
        current_agent="agent2",
        search_required=search_required_bool  # Use the converted boolean
    )

    print(f"DEBUG - Invoking graph")
    try:
        final_state = await graph.ainvoke(state)
        print(f"DEBUG - Graph execution complete")
        
        response_msg = next((m for m in reversed(final_state["messages"]) if m["role"] == "assistant"), None)

        if response_msg:
            print(f"DEBUG - Response found, adding to chat history")
            chat_history.append(response_msg)
            return {
                "response": response_msg["content"] if response_msg else "No response"
            }
        else:
            print(f"DEBUG - No response message found")
            return {"response": "No response generated"}
            
    except Exception as e:
        print(f"ERROR - Graph execution failed: {str(e)}")
        return {"error": f"Processing error: {str(e)}"}