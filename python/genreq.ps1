#!/bin/pwsh

# tooling
pdm export -dG tooling,pycqa -f requirements -o python/requirements.tooling.txt
# mkdocs
pdm export -dG docs-online -f requirements -o python/requirements.mkdocs.txt
# sphinx
pdm export -dG docs-offline -f requirements -o python/requirements.sphinx.txt
