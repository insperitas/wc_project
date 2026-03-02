import os
import stripe
from fastapi import APIRouter

router = APIRouter(prefix="/payments", tags=["payments"])

STRIPE_KEY = os.getenv('STRIPE_API_KEY')
if STRIPE_KEY:
    stripe.api_key = STRIPE_KEY


@router.post('/create-intent')
def create_intent(amount_cents: int = 1000, currency: str = 'usd'):
    """Create a Stripe payment intent; returns client_secret or a mock value if stripe not configured."""
    if not STRIPE_KEY:
        return {"client_secret": "test_client_secret_mock", "mode": "mock"}
    intent = stripe.PaymentIntent.create(amount=amount_cents, currency=currency)
    return {"client_secret": intent.client_secret}
