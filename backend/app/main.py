from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import tickets
from app.services.metrics import get_metrics, get_events
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(title="AI Support Ops API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tickets.router, prefix="/tickets")

@app.get("/health")
def health_check():
    return {"status": "ok"}
@app.get("/metrics")
def metrics():
    return {
        "counters": get_metrics(),
        "recent_events": get_events()
    }
