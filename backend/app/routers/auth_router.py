from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import select
from typing import Optional

from app.db import get_session
from app.models import User
from app.auth import get_password_hash, verify_password, create_access_token, authenticate_user, get_current_user
from app.schemas import RegisterRequest, TokenResponse, UserRead

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post('/register', response_model=UserRead)
def register(payload: RegisterRequest, session=Depends(get_session)):
    existing = session.exec(select(User).where(User.email == payload.email)).first()
    if existing:
        raise HTTPException(status_code=400, detail='Email already registered')
    user = User(email=payload.email, password_hash=get_password_hash(payload.password), role='cleaner' if payload.is_cleaner else 'customer')
    session.add(user)
    session.commit()
    session.refresh(user)
    return UserRead(id=user.id, email=user.email, role=user.role)


@router.post('/login', response_model=TokenResponse)
def login(form_data: OAuth2PasswordRequestForm = Depends(), session=Depends(get_session)):
    user = authenticate_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail='Invalid credentials')
    token = create_access_token(sub=user.email)
    return TokenResponse(access_token=token)


@router.get('/me', response_model=UserRead)
def me(current_user: User = Depends(get_current_user)):
    return UserRead(id=current_user.id, email=current_user.email, role=current_user.role)
