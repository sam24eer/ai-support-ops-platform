from fastapi import APIRouter
from app.models.schemas import TicketCreate
from app.services.classifier import classify_intent
from app.services.decision_engine import make_decision
import logging
import uuid
from datetime import datetime

router = APIRouter()

@router.post("/")
def create_ticket(payload: TicketCreate):
    ticket_id = str(uuid.uuid4())

    intent, confidence = classify_intent(payload.text)
    decision = make_decision(intent, confidence)

    logging.info(
        f"ticket_created id={ticket_id} "
        f"intent={intent} confidence={confidence} decision={decision}"
    )

    return {
        "ticket_id": ticket_id,
        "status": "created",
        "intent": intent,
        "confidence": confidence,
        "decision": decision,
        "created_at": datetime.utcnow()
    }
