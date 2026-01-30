## Backend - local dev

# create venv
python -m venv .venv
source .venv/bin/activate

# install dev deps
pip install -r requirements-dev.txt

--------------------------------------------------------------

# VulnIntel AI — Foundations

## Quick start (local)

# 1. create venv
python -m venv .venv
source .venv/bin/activate

# 2. install dev deps
pip install -r backend/requirements-dev.txt

# 3. run health server
python backend/app/health.py
# or
docker compose up --build
# check http://localhost:8000/health
