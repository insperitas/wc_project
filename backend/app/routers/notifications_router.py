from fastapi import APIRouter, Depends
from typing import List
from app.db import get_session
from app.models import Notification
from sqlmodel import select

router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.post('/')
def create_notification(user_id: int, message: str, session=Depends(get_session)):
    n = Notification(user_id=user_id, message=message)
    session.add(n)
    session.commit()
    session.refresh(n)
    return n


@router.get('/for-user/{user_id}', response_model=List[Notification])
def notifications_for_user(user_id: int, session=Depends(get_session)):
    q = session.exec(select(Notification).where(Notification.user_id == user_id)).all()
    return q
