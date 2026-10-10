#!/bin/bash

set -e

# Cleanup directories
venv_dir="./.venv.dev"
directories=("$venv_dir" "./build" "./dist")
for dir in "${directories[@]}"; do
    if [ -d "$dir" ]; then
        rm -rf "$dir"
    fi
done

# Generate the man page, then build `sdist` and `bdist`.
# Runs in a throwaway environment containing the package (non-editable), its
# optional extras and the locked `docs-offline` dependencies. `uv build` is called
# by the export script.
UV_PROJECT_ENVIRONMENT="$venv_dir" uv run --locked --no-editable \
    --group docs-offline --extra crypto-eth-addresses \
    python package/export pkg
