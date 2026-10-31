# [Syntactiq Automated Test Suite] - Target: src/validators/between.py
# Framework: pytest
import pytest
import inspect

# Dynamic import fallback ensuring tests execute both in-repo and inside sandbox runners
try:
    import src.validators.between as target_module
except ImportError:
    import between as target_module

def test_between_exists_and_callable():
    """Verifies that between is exported and callable."""
    assert hasattr(target_module, 'between')
    func = getattr(target_module, 'between')
    assert callable(func)
    sig = inspect.signature(func)
    assert sig is not None
