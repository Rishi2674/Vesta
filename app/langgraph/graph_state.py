# app/langgraph/graph_state.py

from typing import List, Dict, Optional
from pydantic import BaseModel

class GraphState(BaseModel):
    messages: List[Dict[str, str]]
    current_agent: str
    fallback: Optional[bool] = False
