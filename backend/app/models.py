from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    __table_args__ = {"extend_existing": True}
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, nullable=False)
    password_hash: str
    role: str = Field(default="customer")
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Profile(SQLModel, table=True):
    __table_args__ = {"extend_existing": True}
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    first_name: Optional[str]
    last_name: Optional[str]
    phone: Optional[str]
    address_line1: Optional[str]
    city: Optional[str]
    postcode: Optional[str]


class Area(SQLModel, table=True):
    __table_args__ = {"extend_existing": True}
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    is_active: bool = Field(default=True)


class Booking(SQLModel, table=True):
    __table_args__ = {"extend_existing": True}
    id: Optional[int] = Field(default=None, primary_key=True)
    customer_id: int = Field(foreign_key="user.id")
    area_id: Optional[int] = Field(default=None, foreign_key="area.id")
    status: str = Field(default="requested")
    requested_at: datetime = Field(default_factory=datetime.utcnow)


class Quote(SQLModel, table=True):
    __table_args__ = {"extend_existing": True}
    id: Optional[int] = Field(default=None, primary_key=True)
    booking_id: int = Field(foreign_key="booking.id")
    cleaner_id: int = Field(foreign_key="user.id")
    amount_cents: int
    currency: str = Field(default="GBP")
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Payment(SQLModel, table=True):
    __table_args__ = {"extend_existing": True}
    id: Optional[int] = Field(default=None, primary_key=True)
    booking_id: int = Field(foreign_key="booking.id")
    provider_payment_id: Optional[str]
    amount_cents: int
    currency: str = Field(default="GBP")
    status: str = Field(default="pending")


class Rating(SQLModel, table=True):
    __table_args__ = {"extend_existing": True}
    id: Optional[int] = Field(default=None, primary_key=True)
    booking_id: Optional[int] = None
    rater_id: int
    ratee_id: int
    score: int = Field(ge=1, le=5)
    comment: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Notification(SQLModel, table=True):
    __table_args__ = {"extend_existing": True}
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int
    message: str
    read: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
