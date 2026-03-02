# Development setup (quick reference)

This file documents quick commands to get the local dev environment running.

Start the full stack (Postgres + backend) with Docker Compose:

```bash
sudo docker compose up --build -d
sudo docker compose ps
curl http://127.0.0.1:8000/health
```

Start frontend apps (requires Node 18+). We recommend using `nvm`:

```bash
# install nvm (if needed)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
export NVM_DIR="$HOME/.nvm" && . "$NVM_DIR/nvm.sh"
nvm install 20
nvm use 20

# customer frontend
cd frontend/customer
npm install
npm run dev

# cleaner frontend
cd ../cleaner
npm install
npm run dev -- --port 5174
```

Environment variables
- See `backend/.env.example` for backend envs. Copy it to `backend/.env` and edit values.
- Frontends have `frontend/*/.env` setting `VITE_API_BASE`.

Notes
- The backend entrypoint will wait for Postgres and run `init_db()` to create tables.
- If you need migration history, add Alembic and a migration process.
