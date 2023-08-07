#!/bin/bash

# tooling
pdm export --group tooling,tooling-extras -f requirements -o python/requirements.tooling.txt
# mkdocs
pdm export --group docs-online -f requirements -o python/requirements.mkdocs.txt
# sphinx
pdm export --group docs-offline -f requirements -o python/requirements.sphinx.txt
