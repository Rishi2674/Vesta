from app.utils.groq_client_1 import call_groq_vision_model

def agent1_response(user_text: str = "", base64_image: str = None) -> str:
    # Check if the base64 image is valid
    if not base64_image:
        return "Failed to receive valid image data."
    
    # If no user text is provided, set a default prompt
    if not user_text:
        user_text = "Please analyze the image for any visible issues."
    
    # Call the Groq Vision model with the base64 image and user text
    agent_response = call_groq_vision_model(base64_image, user_text)
    
    # Check if the response was successful
    if not agent_response:
        return "Failed to get response from Groq model."
    
    return agent_response
