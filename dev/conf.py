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

_author_name = _metadata["author-email"].split(" <")[0]
# _author_email = _metadata["author-email"].split(" <")[1].rstrip(">")

project: str = _metadata["name"]
author: str = _author_name
project_copyright = f"2013 - {datetime.now().year}, {_author_name}"
version: str = _metadata["version"]
release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "myst_parser",
]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**/*.md", "*.md"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "furo"
html_favicon = "./assets/icons/favicon.svg"

# -- Options for manpage generation -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-man_pages
man_pages = [("index", project, _metadata["summary"], [author], 1)]

# -- Options for docstring parsing -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
napoleon_numpy_docstring = False
