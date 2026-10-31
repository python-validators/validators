# [Syntactiq Automated Test Suite] - Target: src/validators/iban.py
# Framework: pytest
import pytest
import inspect

# Dynamic import fallback ensuring tests execute both in-repo and inside sandbox runners
try:
    import src.validators.iban as target_module
except ImportError:
    import iban as target_module

def test_iban_exists_and_callable():
    """Verifies that iban is exported and callable."""
    assert hasattr(target_module, 'iban')
    func = getattr(target_module, 'iban')
    assert callable(func)
    sig = inspect.signature(func)
    assert sig is not None
