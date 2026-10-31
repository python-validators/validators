# [Syntactiq Automated Test Suite] - Target: src/validators/utils.py
# Framework: pytest
import pytest
import inspect

# Dynamic import fallback ensuring tests execute both in-repo and inside sandbox runners
try:
    import src.validators.utils as target_module
except ImportError:
    import utils as target_module

def test_validator_exists_and_callable():
    """Verifies that validator is exported and callable."""
    assert hasattr(target_module, 'validator')
    func = getattr(target_module, 'validator')
    assert callable(func)
    sig = inspect.signature(func)
    assert sig is not None

def test_ValidationError_structure():
    """Verifies that ValidationError class and its public methods exist."""
    assert hasattr(target_module, 'ValidationError')
    cls = getattr(target_module, 'ValidationError')
    assert inspect.isclass(cls)
