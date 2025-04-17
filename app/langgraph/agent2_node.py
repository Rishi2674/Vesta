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
    has_image = any(msg.get("image") for msg in reversed(state.messages) if msg["role"] == "user")

    # 🔁 NEW: if user message has an image, immediately fallback to Agent 1
    if has_image:
        state.fallback = True
        return state

    # Otherwise, continue with Agent 2 as usual
    # print("state messages:", state.messages)
    print("Calling agent 2")
    assistant_reply = await agent2_response(state.messages)

    state.messages.append({"role": "assistant", "content": assistant_reply})
    state.current_agent = "agent2"

    # Trigger fallback if agent2 can't answer the question
    if any(trigger.lower() in assistant_reply.lower() for trigger in OUT_OF_DOMAIN_TRIGGERS):
        print("triggered fallback with statement")
        state.fallback = True
    else:
        state.fallback = False

    return state
