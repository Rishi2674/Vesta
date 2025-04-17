# app/langgraph/agent1_node.py

from app.agents.agent1 import agent1_response
from app.langgraph.graph_state import GraphState

def agent1_node(state: GraphState) -> GraphState:
    last_user_msg = next((msg["content"] for msg in reversed(state.messages) if msg["role"] == "user"), "")
    image_data = next((msg.get("image") for msg in reversed(state.messages) if msg.get("image")), None)

    response = agent1_response(user_text=state.messages, base64_image=image_data)
    
    state.messages.append({"role": "assistant", "content": response})
    state.current_agent = "agent1"
    return state
