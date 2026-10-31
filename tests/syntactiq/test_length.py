# [Syntactiq Automated Test Suite] - Target: src/validators/length.py
# Framework: pytest
import pytest
import inspect

# Dynamic import fallback ensuring tests execute both in-repo and inside sandbox runners
try:
    import src.validators.length as target_module
except ImportError:
    import length as target_module

def test_length_exists_and_callable():
    """Verifies that length is exported and callable."""
    assert hasattr(target_module, 'length')
    func = getattr(target_module, 'length')
    assert callable(func)
    sig = inspect.signature(func)
    assert sig is not None
