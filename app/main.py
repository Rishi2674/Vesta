# app/main.py
from fastapi import FastAPI
from app.routers import chat

app = FastAPI(title="Vesta: Multi-Agent Real Estate Assistant")

app.include_router(chat.router)
