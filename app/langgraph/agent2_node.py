# app/langgraph/agent2_node.py

from app.agents.agent2 import agent2_response
from app.langgraph.graph_state import GraphState

OUT_OF_DOMAIN_TRIGGERS = [
    "I don't have the capability to analyze images",
    "I'm not qualified to provide advice on selling",
    "I'm here to help with tenancy"
]

async def agent2_node(state: GraphState) -> GraphState:
    last_user_msg = next((msg["content"] for msg in reversed(state.messages) if msg["role"] == "user"), "")

    response_obj = await agent2_response(last_user_msg)
    assistant_reply = response_obj["response"]

    state.messages.append({"role": "assistant", "content": assistant_reply})
    state.current_agent = "agent2"

    # Check if response should trigger fallback
    if any(trigger.lower() in assistant_reply.lower() for trigger in OUT_OF_DOMAIN_TRIGGERS):
        state.fallback = True
    else:
        state.fallback = False

    return state
