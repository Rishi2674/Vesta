from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from app.routers import graph_chat, chat

app = FastAPI(title="Vesta: Multi-Agent Real Estate Assistant")

# CORS: Include production domain if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", 
        "http://127.0.0.1:3000"
        # add "https://your-production-site.com" here when ready
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files from the React build
app.mount("/static", StaticFiles(directory="frontend/build/static"), name="static")

# Serve React index.html for the root
@app.get("/")
def serve_react_index():
    return FileResponse("frontend/build/index.html")

# Serve React index.html for all other frontend routes
@app.get("/{full_path:path}")
def serve_react_app(full_path: str):
    file_path = os.path.join("frontend", "build", full_path)
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    return FileResponse("frontend/build/index.html")

# Include API routers
app.include_router(graph_chat.router)
app.include_router(chat.router)
