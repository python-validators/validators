# [Syntactiq Automated Test Suite] - Target: src/validators/hostname.py
# Framework: pytest
import pytest
import inspect

# Dynamic import fallback ensuring tests execute both in-repo and inside sandbox runners
try:
    import src.validators.hostname as target_module
except ImportError:
    import hostname as target_module

def test_hostname_exists_and_callable():
    """Verifies that hostname is exported and callable."""
    assert hasattr(target_module, 'hostname')
    func = getattr(target_module, 'hostname')
    assert callable(func)
    sig = inspect.signature(func)
    assert sig is not None
