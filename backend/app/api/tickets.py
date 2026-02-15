from fastapi import APIRouter
from app.models.schemas import TicketCreate
import logging
import uuid
from datetime import datetime

router = APIRouter()

@router.post("/")
def create_ticket(payload: TicketCreate):
    ticket_id = str(uuid.uuid4())

    logging.info(f"ticket_created id={ticket_id}")

    return {
        "ticket_id": ticket_id,
        "status": "created",
        "created_at": datetime.utcnow()
    }
