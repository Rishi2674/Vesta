# app/langgraph/graph.py

from langgraph.graph import StateGraph, END
from app.langgraph.graph_state import GraphState
from app.langgraph.agent1_node import agent1_node
from app.langgraph.agent2_node import agent2_node

def build_graph():
    # Initialize graph with our shared state class
    builder = StateGraph(GraphState)

    # Add both agents as nodes
    builder.add_node("agent1", agent1_node)
    builder.add_node("agent2", agent2_node)

    # Set agent2 as the entry point
    builder.set_entry_point("agent2")

    # Define transitions
    # If agent2 sets fallback = True → go to agent1
    builder.add_conditional_edges(
        "agent2",
        lambda state: "agent1" if state.fallback else END
    )

    # Agent1 always ends (for now)
    builder.add_edge("agent1", END)

    # Compile the graph
    return builder.compile()
