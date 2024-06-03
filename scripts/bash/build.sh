#!/bin/bash

set -e

# Run tests
poetry run pytest -v -s

# Run linters
#poetry run black *NAMED_SUBMODULE_HERE* -l 79
#poetry run flake8 *NAMED_SUBMODULE_HERE* --ignore=E203,W503,W504

# Update the version in pyproject.toml based on CHANGELOG.md
python scripts/py/update_version.py

# Build the project
poetry build
