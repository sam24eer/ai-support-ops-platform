from fastapi import FastAPI
from app.api import tickets
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(title="AI Support Ops API")

app.include_router(tickets.router, prefix="/tickets")

@app.get("/health")
def health_check():
    return {"status": "ok"}
