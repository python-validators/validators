# [Syntactiq Automated Test Suite] - Target: src/validators/crypto_addresses/eth_address.py
# Framework: pytest
import pytest
import inspect

# Dynamic import fallback ensuring tests execute both in-repo and inside sandbox runners
try:
    import src.validators.crypto_addresses.eth_address as target_module
except ImportError:
    import eth_address as target_module

def test_eth_address_exists_and_callable():
    """Verifies that eth_address is exported and callable."""
    assert hasattr(target_module, 'eth_address')
    func = getattr(target_module, 'eth_address')
    assert callable(func)
    sig = inspect.signature(func)
    assert sig is not None
