#!/bin/bash

set -e

# Check if CI environment variable is set to "false"
# or set to empty string or not set at all.
# Using the wrong way see: https://stackoverflow.com/a/13864829
if [ -z "$CI" ] || [ "$CI" = "false" ]; then
    # tooling
    pdm export --group tooling -f requirements -o package/requirements.tooling.txt
    # testing
    pdm export --group testing,crypto-eth-addresses -f requirements -o package/requirements.testing.txt
    # mkdocs
    pdm export --group docs-online -f requirements -o package/requirements.mkdocs.txt
    # sphinx
    pdm export --group docs-offline -f requirements -o package/requirements.sphinx.txt
    export CI=true
fi

# Cleanup directories
venv_dir="./.venv.dev"
directories=("$venv_dir" "./build" "./dist")
for dir in "${directories[@]}"; do
    if [ -d "$dir" ]; then
        rm -rf "$dir"
    fi
done

# Create venv
python -m venv $venv_dir

# Upgrade pip
$venv_dir/bin/python -m pip install --upgrade pip

# Install the current package
$venv_dir/bin/pip install .

# Install sphinx requirements
$venv_dir/bin/pip install -r package/requirements.sphinx.txt

# Install build tool
$venv_dir/bin/pip install build

# Activate virtual environment
. $venv_dir/bin/activate

# Run export script
python package/export pkg

# Deactivate virtual environment
deactivate

# delete environment variable
unset CI
