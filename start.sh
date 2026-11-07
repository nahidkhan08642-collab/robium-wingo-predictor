#!/usr/bin/env bash
# ==========================================
# Robiul Predictor App - Automated Start Script
# ==========================================
echo "Starting Robiul Predictor & Hacker Tool..."
cd "$(dirname "$0")"

# Check python dependencies
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt --quiet
fi

# Run Flask application
python3 app.py
