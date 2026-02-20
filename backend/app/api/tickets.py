from fastapi import APIRouter
from typing import List
from app.models.schemas import TicketCreate
from app.services.classifier import classify_intent
from app.services.decision_engine import make_decision
from app.services.metrics import record_event
import logging
import uuid
from datetime import datetime

router = APIRouter()

# In-memory ticket store (MVP)
TICKETS: List[dict] = []


@router.post("/")
def create_ticket(payload: TicketCreate):
    ticket_id = str(uuid.uuid4())

    intent, confidence = classify_intent(payload.text)
    decision = make_decision(intent, confidence)

    ticket_data = {
        "ticket_id": ticket_id,
        "user_id": payload.user_id,
        "channel": payload.channel,
        "text": payload.text,
        "status": "created",
        "intent": intent,
        "confidence": confidence,
        "decision": decision,
        "created_at": datetime.utcnow()
    }

    # Store ticket in memory
    TICKETS.append(ticket_data)

    # Metrics
    record_event(
        event_type="ticket_created",
        payload={
            "ticket_id": ticket_id,
            "intent": intent,
            "decision": decision
        }
    )

    if decision == "auto_resolve":
        record_event("ticket_auto_resolved", {"ticket_id": ticket_id})
    else:
        record_event("ticket_escalated", {"ticket_id": ticket_id})

    logging.info(
        f"ticket_created id={ticket_id} "
        f"intent={intent} confidence={confidence} decision={decision}"
    )

    return ticket_data


@router.get("/", summary="Get all tickets (in-memory)")
def get_all_tickets():
    return TICKETS