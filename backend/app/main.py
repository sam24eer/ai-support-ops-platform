from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path

from app.api import tickets
from app.services.metrics import get_metrics
from app.core.logging import setup_logging

# --------------------------------------------------
# App setup
# --------------------------------------------------

setup_logging()

app = FastAPI(
    title="AI Support Operations Platform",
    version="1.0.0"
)

# --------------------------------------------------
# CORS (for browser UI)
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# API Routers
# --------------------------------------------------

app.include_router(tickets.router, prefix="/tickets", tags=["Tickets"])

# --------------------------------------------------
# Health & Metrics
# --------------------------------------------------

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return get_metrics()

# --------------------------------------------------
# Frontend UI Serving
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

@app.get("/ui")
def serve_ui():
    return FileResponse(FRONTEND_DIR / "index.html")

@app.get("/ops")
def serve_ops():
    return FileResponse(FRONTEND_DIR / "history.html")