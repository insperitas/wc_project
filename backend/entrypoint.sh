#!/usr/bin/env bash
set -e

echo "Waiting for database..."
for i in {1..60}; do
  if python - <<'PY'
import os
import sys
from urllib.parse import urlparse
try:
    import psycopg2
except Exception:
    sys.exit(0)

url = os.getenv('DATABASE_URL')
if not url:
    sys.exit(0)
parsed = urlparse(url)
host = parsed.hostname or 'db'
port = parsed.port or 5432
user = parsed.username or 'postgres'
password = parsed.password or 'postgres'
dbname = parsed.path.lstrip('/') if parsed.path else 'wcdb'
try:
    conn = psycopg2.connect(host=host, port=port, user=user, password=password, dbname=dbname)
    conn.close()
    sys.exit(0)
except Exception:
    sys.exit(1)
PY
  then
    echo "database reachable"
    break
  else
    sleep 1
  fi
done

echo "Initializing DB (if needed)"
python -c "from app.db import init_db; init_db()"

echo "Starting server"
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
