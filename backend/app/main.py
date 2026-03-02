import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import init_db
from app.routers import auth_router, ratings_router, scheduling_router, notifications_router
from app.payments import router as payments_router

app = FastAPI(title='WindowClean API')

# Configure CORS: allow origins from env `ALLOWED_ORIGINS` (comma-separated)
_origins = os.getenv('ALLOWED_ORIGINS')
if _origins:
    allowed_origins = [o.strip() for o in _origins.split(',') if o.strip()]
else:
    allowed_origins = [
        'http://localhost:5173',
        'http://127.0.0.1:5173',
        'http://localhost:5174',
        'http://127.0.0.1:5174',
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.on_event('startup')
def on_startup():
    init_db()


@app.get('/health')
def health():
    return {'status': 'ok'}


# include routers
app.include_router(auth_router.router)
app.include_router(payments_router)
app.include_router(ratings_router.router)
app.include_router(scheduling_router.router)
app.include_router(notifications_router.router)
