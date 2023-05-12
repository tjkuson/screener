#!/usr/bin/env sh

echo "Checking with ssort..."
ssort --check .

echo "Running ruff violation checks..."
ruff check --quiet .

echo "Checking with black..."
black --check .

echo "Checking with mypy..."
mypy --strict .