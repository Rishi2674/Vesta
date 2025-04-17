# app/agents/agent1.py

from app.utils.groq_client_1 import call_groq_vision_model
from app.utils.shared_memory import add_message, get_history

def agent1_response(user_text: str = "", base64_image: str = None):
    
    if not base64_image:
        return {"agent": "Agent 1", "response": "Failed to receive valid image data."}

    if not user_text:
        user_text = "Please analyze the image for any visible issues."

    # Log user input to shared memory
    # add_message("user", user_text)

    # Call Groq Vision model
    print("calling agent 1")
    agent_response = call_groq_vision_model(base64_image, user_text)

    if not agent_response:
        return {"agent": "Agent 1", "response": "Failed to get response from Groq model."}

    # Log assistant response
    # add_message("assistant", f"Image analysis result: {agent_response}")


    return agent_response
