# [Syntactiq Automated Test Suite] - Target: src/validators/slug.py
# Framework: pytest
import pytest
import inspect

# Dynamic import fallback ensuring tests execute both in-repo and inside sandbox runners
try:
    import src.validators.slug as target_module
except ImportError:
    import slug as target_module

def test_slug_exists_and_callable():
    """Verifies that slug is exported and callable."""
    assert hasattr(target_module, 'slug')
    func = getattr(target_module, 'slug')
    assert callable(func)
    sig = inspect.signature(func)
    assert sig is not None
