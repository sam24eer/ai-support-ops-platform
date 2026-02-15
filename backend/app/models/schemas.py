from pydantic import BaseModel
from datetime import datetime

class TicketCreate(BaseModel):
    user_id: str
    channel: str
    text: str


class Ticket(BaseModel):
    ticket_id: str
    user_id: str
    channel: str
    text: str
    status: str
    created_at: datetime

