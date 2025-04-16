# app/utils/shared_memory.py

# Global message store (FIFO)
conversation_history = []
MAX_HISTORY = 6

def add_message(role: str, content: str):
    global conversation_history
    conversation_history.append({"role": role, "content": content})
    if len(conversation_history) > MAX_HISTORY:
        conversation_history = conversation_history[-MAX_HISTORY:]

def get_history():
    return conversation_history

def clear_history():
    global conversation_history
    conversation_history = []
