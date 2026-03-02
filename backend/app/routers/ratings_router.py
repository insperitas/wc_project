from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.db import get_session
from app.models import Rating
from sqlmodel import select

router = APIRouter(prefix="/ratings", tags=["ratings"])


@router.post('/')
def create_rating(rater_id: int, ratee_id: int, score: int, comment: str | None = None, session=Depends(get_session)):
    if score < 1 or score > 5:
        raise HTTPException(status_code=400, detail='Score must be 1-5')
    r = Rating(rater_id=rater_id, ratee_id=ratee_id, score=score, comment=comment)
    session.add(r)
    session.commit()
    session.refresh(r)
    return r


@router.get('/by-user/{user_id}', response_model=List[Rating])
def ratings_for_user(user_id: int, session=Depends(get_session)):
    q = session.exec(select(Rating).where(Rating.ratee_id == user_id)).all()
    return q
