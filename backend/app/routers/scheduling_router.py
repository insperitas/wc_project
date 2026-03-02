from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.db import get_session
from app.models import Booking
from sqlmodel import select

router = APIRouter(prefix="/scheduling", tags=["scheduling"])


@router.post('/book')
def create_booking(customer_id: int, scheduled_at: str, session=Depends(get_session)):
    # scheduled_at as ISO string for simplicity; in production parse/validate properly
    b = Booking(customer_id=customer_id, scheduled_at=scheduled_at)
    session.add(b)
    session.commit()
    session.refresh(b)
    return b


@router.get('/{booking_id}')
def get_booking(booking_id: int, session=Depends(get_session)):
    b = session.get(Booking, booking_id)
    if not b:
        raise HTTPException(status_code=404, detail='Booking not found')
    return b
