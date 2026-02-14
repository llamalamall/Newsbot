#!/bin/bash
# Local helper script to run Newsbot

set -e

echo "============================================"
echo "Newsbot - Local Execution Helper"
echo "============================================"
echo

# Check if running in virtual environment
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
else
    echo "Using existing virtual environment: $VIRTUAL_ENV"
fi

# Install dependencies
echo "Installing dependencies..."
pip install -q -r requirements.txt

echo

# Check for .env file
if [ -f .env ]; then
    echo "Loading environment from .env file..."
    export $(cat .env | grep -v '^#' | xargs)
fi

# Check for required environment variables
if [ -z "$GITHUB_TOKEN" ]; then
    echo "ERROR: GITHUB_TOKEN must be set"
    echo
    echo "GITHUB_TOKEN is required for:"
    echo "  - GitHub repository searches"
    echo "  - LLM-powered searches via GitHub Models"
    echo
    echo "You can set it by:"
    echo "1. Creating a .env file with:"
    echo "   GITHUB_TOKEN=your_token_here"
    echo
    echo "2. Or export it in your shell:"
    echo "   export GITHUB_TOKEN=your_token_here"
    exit 1
fi

# Run the newsbot
echo "Running Newsbot..."
echo
python3 scripts/newsbot.py

echo
echo "============================================"
echo "Done! Check the outputs/ directory for results."
echo "============================================"
