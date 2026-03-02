# Backend (FastAPI) scaffold

Quick start (development):

1. Create a virtualenv and install dependencies:

```markdown
# Backend (FastAPI) scaffold

Quick start (development):

1. Create a virtualenv and install dependencies (optional if using Docker):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and adjust values if needed.

3. Run locally (venv):

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

4. Run the full stack with Docker Compose (recommended):

```bash
# build and start services (Postgres + backend)
sudo docker compose up --build -d

# check running services
sudo docker compose ps

# verify backend health
curl http://127.0.0.1:8000/health
```

Notes
- The container entrypoint waits for Postgres, runs `init_db()` (creates tables via SQLModel),
  then starts Uvicorn. If you need migration history, add Alembic and replace the `init_db()`
  initialisation with migration commands.

- Provide `ALLOWED_ORIGINS` and other secrets via `.env` or your environment. See `./.env.example`.

Endpoints
- `/health` — health check
- `/auth/register` — register user
- `/auth/login` — obtain JWT

```
