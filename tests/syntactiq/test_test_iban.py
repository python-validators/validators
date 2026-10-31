# [Syntactiq Automated Test Suite] - Target: tests/test_iban.py
# Framework: pytest
import pytest
import inspect

# Dynamic import fallback ensuring tests execute both in-repo and inside sandbox runners
try:
    import tests.test_iban as target_module
except ImportError:
    import test_iban as target_module

def test_test_returns_true_on_valid_iban_exists_and_callable():
    """Verifies that test_returns_true_on_valid_iban is exported and callable."""
    assert hasattr(target_module, 'test_returns_true_on_valid_iban')
    func = getattr(target_module, 'test_returns_true_on_valid_iban')
    assert callable(func)
    sig = inspect.signature(func)
    assert sig is not None

def test_test_returns_true_on_valid_lowercase_iban_exists_and_callable():
    """Verifies that test_returns_true_on_valid_lowercase_iban is exported and callable."""
    assert hasattr(target_module, 'test_returns_true_on_valid_lowercase_iban')
    func = getattr(target_module, 'test_returns_true_on_valid_lowercase_iban')
    assert callable(func)
    sig = inspect.signature(func)
    assert sig is not None

def test_test_returns_failed_validation_on_invalid_iban_exists_and_callable():
    """Verifies that test_returns_failed_validation_on_invalid_iban is exported and callable."""
    assert hasattr(target_module, 'test_returns_failed_validation_on_invalid_iban')
    func = getattr(target_module, 'test_returns_failed_validation_on_invalid_iban')
    assert callable(func)
    sig = inspect.signature(func)
    assert sig is not None

def test_test_rejects_non_ascii_case_equivalents_exists_and_callable():
    """Verifies that test_rejects_non_ascii_case_equivalents is exported and callable."""
    assert hasattr(target_module, 'test_rejects_non_ascii_case_equivalents')
    func = getattr(target_module, 'test_rejects_non_ascii_case_equivalents')
    assert callable(func)
    sig = inspect.signature(func)
    assert sig is not None
