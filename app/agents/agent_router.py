# app/agents/agent_router.py
from app.agents.agent1 import agent1_response
from app.agents.agent2 import agent2_response
from app.utils.helpers import is_tenancy_question

async def route_message(message: str = None, image: str = None):
    if image:
        return agent1_response(message, image)
    
    if message:
        return  await agent2_response(message)
    
    return "Can you please clarify if you're asking about a rental issue or showing a property problem?"
