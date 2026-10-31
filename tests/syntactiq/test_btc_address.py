# [Syntactiq Automated Test Suite] - Target: src/validators/crypto_addresses/btc_address.py
# Framework: pytest
import pytest
import inspect

# Dynamic import fallback ensuring tests execute both in-repo and inside sandbox runners
try:
    import src.validators.crypto_addresses.btc_address as target_module
except ImportError:
    import btc_address as target_module

def test_btc_address_exists_and_callable():
    """Verifies that btc_address is exported and callable."""
    assert hasattr(target_module, 'btc_address')
    func = getattr(target_module, 'btc_address')
    assert callable(func)
    sig = inspect.signature(func)
    assert sig is not None
