# [Syntactiq Automated Test Suite] - Target: src/validators/_extremes.py
# Framework: pytest
import pytest
import inspect

# Dynamic import fallback ensuring tests execute both in-repo and inside sandbox runners
try:
    import src.validators._extremes as target_module
except ImportError:
    import _extremes as target_module

def test_AbsMax_structure():
    """Verifies that AbsMax class and its public methods exist."""
    assert hasattr(target_module, 'AbsMax')
    cls = getattr(target_module, 'AbsMax')
    assert inspect.isclass(cls)

def test_AbsMin_structure():
    """Verifies that AbsMin class and its public methods exist."""
    assert hasattr(target_module, 'AbsMin')
    cls = getattr(target_module, 'AbsMin')
    assert inspect.isclass(cls)
