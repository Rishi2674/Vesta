from app.agents.agent2 import agent2_response
from app.langgraph.graph_state import GraphState
from app.tools.web_summariser_tool import web_search_summarizer_tool

OUT_OF_DOMAIN_TRIGGERS = [
    "I don't have the capability to analyze images",
    "I'm not qualified to provide advice on selling",
    "I'm here to help with tenancy"
]

async def agent2_node(state: GraphState) -> GraphState:
    last_user_msg = next((msg["content"] for msg in reversed(state.messages) if msg["role"] == "user"), "")
    has_image = any(msg.get("image") for msg in reversed(state.messages) if msg["role"] == "user")

    # 🔁 Fallback to Agent 1 if there's an image
    if has_image:
        state.fallback = True
        return state

    # ⚡️Use web summariser tool if search_required is True
    if getattr(state, "search_required", False):
        print("[Agent2] Web summariser tool triggered.")
        assistant_reply = web_search_summarizer_tool(last_user_msg)
        state.messages.append({"role": "assistant", "content": assistant_reply})
        state.current_agent = "agent2"
        state.fallback = False
        state.search_required = False  # ✅ Reset after use
        return state

    # 🧠 Standard Agent 2 response
    print("Calling agent 2")
    assistant_reply = await agent2_response(state.messages)

    state.messages.append({"role": "assistant", "content": assistant_reply})
    state.current_agent = "agent2"

    # 🛑 Trigger fallback if out-of-domain response
    if any(trigger.lower() in assistant_reply.lower() for trigger in OUT_OF_DOMAIN_TRIGGERS):
        print("triggered fallback with statement")
        state.fallback = True
    else:
        state.fallback = False

    return state
