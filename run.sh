#!/usr/bin/env bash
echo "=============================================================================="
echo " LAICIs: Local AI Checker Integration System"
echo " DORMATHON 2026 - Track 2 (Tencent WorkBuddy Agentic Solutions)"
echo "=============================================================================="
echo ""

# Copy .env if missing
if [ ! -f "backend/.env" ]; then
    echo "[INFO] backend/.env not found. Creating from .env.example..."
    cp .env.example backend/.env
fi

# Install dependencies
echo "[INFO] Verifying Python dependencies..."
python3 -m pip install -r requirements.txt --quiet

# Launch
echo "[INFO] Starting LAICIs WorkBuddy Backend on http://localhost:5000 ..."
python3 backend/server.py
