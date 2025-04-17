# app/utils/memory.py
from collections import deque

# Memory for single-user chat
chat_history = deque(maxlen=6)  # holds last 6 messages (user + assistant)
