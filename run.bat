@echo off
title LAICIs - Autonomous Forensic Agent (Track 2)
echo ==============================================================================
echo  LAICIs: Local AI Checker Integration System
echo  DORMATHON 2026 - Track 2 (Tencent WorkBuddy Agentic Solutions)
echo ==============================================================================
echo.

:: Check for .env file
if not exist "backend\.env" (
    echo [INFO] backend\.env not found. Creating from .env.example...
    copy .env.example backend\.env
)

:: Install / Verify Requirements
echo [INFO] Verifying Python dependencies...
python -m pip install -r requirements.txt --quiet

:: Start LAICIs Server
echo [INFO] Starting LAICIs WorkBuddy Backend on http://localhost:5000 ...
echo [INFO] Opening browser in 3 seconds...
start "" "http://localhost:5000"

python backend\server.py
pause
