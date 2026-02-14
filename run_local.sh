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
if [ -z "$OPENAI_API_KEY" ] && [ -z "$GITHUB_TOKEN" ]; then
    echo "ERROR: At least one of OPENAI_API_KEY or GITHUB_TOKEN must be set"
    echo
    echo "You can set them by:"
    echo "1. Creating a .env file with:"
    echo "   OPENAI_API_KEY=your_key_here"
    echo "   GITHUB_TOKEN=your_token_here"
    echo
    echo "2. Or export them in your shell:"
    echo "   export OPENAI_API_KEY=your_key_here"
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
