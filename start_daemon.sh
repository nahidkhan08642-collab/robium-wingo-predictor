#!/usr/bin/env bash
# ==========================================
# Robiul Predictor - Termux Permanent Daemon Service Setup (Step 21)
# ==========================================

echo "Initializing Robiul Predictor Background Daemon Service..."
cd "$(dirname "$0")"

# Kill any existing instance running on port 5000
PID=$(lsof -t -i:5000)
if [ ! -z "$PID" ]; then
    echo "Stopping existing instance on PID $PID..."
    kill -9 $PID
fi

# Start Flask app in background using nohup with log output
nohup python3 app.py > app_daemon.log 2>&1 &

NEW_PID=$!
echo "Robiul Predictor App is now running permanently in background as Daemon!"
echo "PID: $NEW_PID"
echo "Logs are being saved to: $(pwd)/app_daemon.log"
echo "Access local server at: http://127.0.0.1:5000"
