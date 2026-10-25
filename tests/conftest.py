"""Make the ``validators`` package importable without an install.

Tries, in order: the src-layout of a checked-out repo (``../src``),
this workdir's ``../validators-src/src`` clone, and the repo root itself.
Only directories that actually contain the ``validators`` package are added.
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_CANDIDATES = (
    os.path.join(_HERE, "..", "src"),
    os.path.join(_HERE, "..", "validators-src", "src"),
    os.path.join(_HERE, ".."),
)
for _candidate in _CANDIDATES:
    if os.path.isdir(os.path.join(_candidate, "validators")):
        sys.path.insert(0, os.path.normpath(_candidate))
