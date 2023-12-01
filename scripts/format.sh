#!/usr/bin/env sh

echo "Formatting with ssort..."
ssort .

echo "Apply Ruff lint autofixes..."
ruff --quiet --fix .

echo "Formatting with Ruff..."
ruff format .
