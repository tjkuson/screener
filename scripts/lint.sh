#!/usr/bin/env sh

echo "Checking with ssort..."
python3 -m ssort --check .

echo "Running ruff violation checks..."
python3 -m ruff check --quiet .

echo "Checking with black..."
python3 -m black --check .

echo "Checking with mypy..."
python3 -m mypy --strict .