# [Syntactiq Automated Test Suite] - Target: src/validators/email.py
# Framework: pytest
import pytest
import inspect

# Dynamic import fallback ensuring tests execute both in-repo and inside sandbox runners
try:
    import src.validators.email as target_module
except ImportError:
    import email as target_module

def test_email_exists_and_callable():
    """Verifies that email is exported and callable."""
    assert hasattr(target_module, 'email')
    func = getattr(target_module, 'email')
    assert callable(func)
    sig = inspect.signature(func)
    assert sig is not None
