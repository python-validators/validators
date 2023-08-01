"""Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# standard
from datetime import datetime
from importlib.metadata import metadata

# -- Project information ----------------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
_metadata = metadata("validators")

project: str = _metadata["name"]
author: str = _metadata["author"]
project_copyright = f"2013 - {datetime.now().year}, {_metadata['author']}"
version: str = _metadata["version"]
release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "myst_parser",
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "*.md"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "alabaster"

# -- Options for manpage generation -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-man_pages
man_pages = [("index", project, _metadata["summary"], [author], 1)]

# -- Options for docstring parsing -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
napoleon_numpy_docstring = False
