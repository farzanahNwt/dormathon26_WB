#!/usr/bin/env bash
# ==============================================================================
# LAICIs - 1-Click Tencent Cloud Lighthouse / CVM Deployment Script
# DORMATHON 2026 · Track 2 (Tencent WorkBuddy Agentic Solutions)
# ==============================================================================

set -e

echo "=============================================================================="
echo " 🛡️ Deploying LAICIs to Tencent Cloud (WorkBuddy Agent Core)"
echo "=============================================================================="

# 1. Update system
echo "[1/5] Updating system packages..."
sudo apt-get update -y && sudo apt-get upgrade -y

# 2. Install Docker & Docker Compose if not present
echo "[2/5] Checking Docker installation..."
if ! command -v docker &> /dev/null; then
    echo "Installing Docker..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker $USER
    rm get-docker.sh
fi

if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
    echo "Installing Docker Compose plugin..."
    sudo apt-get install -y docker-compose-plugin
fi

# 3. Configure Firewall
echo "[3/5] Configuring firewall ports (80 & 5000)..."
if command -v ufw &> /dev/null; then
    sudo ufw allow 80/tcp || true
    sudo ufw allow 5000/tcp || true
fi

# 4. Verify Environment Variables
echo "[4/5] Verifying backend/.env credentials..."
if [ ! -f "backend/.env" ]; then
    echo "Creating backend/.env from .env.example..."
    cp .env.example backend/.env
    echo "⚠️ Please edit backend/.env to provide your actual Tencent Cloud and Gemini API keys!"
fi

# 5. Build and Launch Container
echo "[5/5] Building and launching LAICIs Docker container..."
docker compose down || true
docker compose up -d --build

SERVER_IP=$(curl -s ifconfig.me || echo "YOUR-SERVER-IP")

echo ""
echo "=============================================================================="
echo " 🎉 LAICIs successfully deployed on Tencent Cloud!"
echo " Direct Web URL:  http://${SERVER_IP}/"
echo " Alternate Port:  http://${SERVER_IP}:5000/"
echo " Dashboard:       http://${SERVER_IP}/results.html"
echo " Pitch Deck:      http://${SERVER_IP}/slides.html"
echo " MCP Server:      http://${SERVER_IP}/api/workbuddy/mcp"
echo "=============================================================================="
