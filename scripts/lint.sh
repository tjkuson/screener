#!/usr/bin/env sh

echo "Checking with ssort..."
python3 -m ssort --check .

echo "Checking with Ruff..."
python3 -m ruff --quiet .

echo "Checking with black..."
python3 -m ruff format --check .

echo "Checking with mypy..."
python3 -m mypy --strict .
