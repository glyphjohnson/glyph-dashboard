# Glyph Dashboard - Production Ready

## Features
- Live sub-agent monitoring (JSON data from OpenClaw sessions, cron-updated)
- Professional UI (Inter font, gradient, responsive table)
- API endpoints (/api/subs, /api/meta)
- Auto-refresh ready

## Local Run
```bash
pip3 install -r requirements.txt
python3 app.py
```
http://localhost:8080

## SSH Tunnel
ssh -L 8080:localhost:8080 root@[host IP]

## Live Data Update (Cron in OpenClaw)
- Every 5 min: sessions_list → subs.json/meta.json → git commit/push
- Edit cron in OpenClaw for production.

## Deploy (Production)
- VPS: gunicorn app:app -b 0.0.0.0:8080
- Docker: See Dockerfile (add if needed)

Repo auto-deploys on push.
