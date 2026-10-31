# [Syntactiq Automated Test Suite] - Target: src/validators/ip_address.py
# Framework: pytest
import pytest
import inspect

# Dynamic import fallback ensuring tests execute both in-repo and inside sandbox runners
try:
    import src.validators.ip_address as target_module
except ImportError:
    import ip_address as target_module

def test_ipv4_exists_and_callable():
    """Verifies that ipv4 is exported and callable."""
    assert hasattr(target_module, 'ipv4')
    func = getattr(target_module, 'ipv4')
    assert callable(func)
    sig = inspect.signature(func)
    assert sig is not None

def test_ipv6_exists_and_callable():
    """Verifies that ipv6 is exported and callable."""
    assert hasattr(target_module, 'ipv6')
    func = getattr(target_module, 'ipv6')
    assert callable(func)
    sig = inspect.signature(func)
    assert sig is not None
