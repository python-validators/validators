# [Syntactiq Automated Test Suite] - Target: src/validators/crypto_addresses/bsc_address.py
# Framework: pytest
import pytest
import inspect

# Dynamic import fallback ensuring tests execute both in-repo and inside sandbox runners
try:
    import src.validators.crypto_addresses.bsc_address as target_module
except ImportError:
    import bsc_address as target_module

def test_bsc_address_exists_and_callable():
    """Verifies that bsc_address is exported and callable."""
    assert hasattr(target_module, 'bsc_address')
    func = getattr(target_module, 'bsc_address')
    assert callable(func)
    sig = inspect.signature(func)
    assert sig is not None
