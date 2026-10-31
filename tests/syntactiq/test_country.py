# [Syntactiq Automated Test Suite] - Target: src/validators/country.py
# Framework: pytest
import pytest
import inspect

# Dynamic import fallback ensuring tests execute both in-repo and inside sandbox runners
try:
    import src.validators.country as target_module
except ImportError:
    import country as target_module

def test_calling_code_exists_and_callable():
    """Verifies that calling_code is exported and callable."""
    assert hasattr(target_module, 'calling_code')
    func = getattr(target_module, 'calling_code')
    assert callable(func)
    sig = inspect.signature(func)
    assert sig is not None

def test_country_code_exists_and_callable():
    """Verifies that country_code is exported and callable."""
    assert hasattr(target_module, 'country_code')
    func = getattr(target_module, 'country_code')
    assert callable(func)
    sig = inspect.signature(func)
    assert sig is not None

def test_currency_exists_and_callable():
    """Verifies that currency is exported and callable."""
    assert hasattr(target_module, 'currency')
    func = getattr(target_module, 'currency')
    assert callable(func)
    sig = inspect.signature(func)
    assert sig is not None
