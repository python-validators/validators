# [Syntactiq Automated Test Suite] - Target: src/validators/mac_address.py
# Framework: pytest
import pytest
import inspect

# Dynamic import fallback ensuring tests execute both in-repo and inside sandbox runners
try:
    import src.validators.mac_address as target_module
except ImportError:
    import mac_address as target_module

def test_mac_address_exists_and_callable():
    """Verifies that mac_address is exported and callable."""
    assert hasattr(target_module, 'mac_address')
    func = getattr(target_module, 'mac_address')
    assert callable(func)
    sig = inspect.signature(func)
    assert sig is not None
