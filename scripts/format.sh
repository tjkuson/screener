#!/usr/bin/env sh

echo "Formatting with autofix ruff violation checks..."
ruff check --quiet --fix .

echo "Formatting with black..."
black --quiet .