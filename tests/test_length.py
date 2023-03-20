"""Test Length."""
# -*- coding: utf-8 -*-

# external
import pytest

# local
from validators import length, ValidationFailure


@pytest.mark.parametrize(
    ("value", "min_val", "max_val"),
    [("password", 2, 10), ("password", 0, 10), ("password", 8, 8)],
)
def test_returns_true_on_valid_length(value: str, min_val: int, max_val: int):
    """Test returns true on valid length."""
    assert length(value, min_val=min_val, max_val=max_val)


@pytest.mark.parametrize(
    ("value", "min_val", "max_val"),
    [("something", 14, 12), ("something", -10, -20), ("something", 0, -2)],
)
def test_raises_assertion_error_for_invalid_args(value: str, min_val: int, max_val: int):
    """Test raises assertion error for invalid args."""
    with pytest.raises(AssertionError):
        assert length(value, min_val=min_val, max_val=max_val)


@pytest.mark.parametrize(
    ("value", "min_val", "max_val"),
    [("something", 13, 14), ("something", 0, 6), ("something", 14, 20)],
)
def test_returns_failed_validation_on_invalid_range(value: str, min_val: int, max_val: int):
    """Test returns failed validation on invalid range."""
    assert isinstance(length(value, min_val=min_val, max_val=max_val), ValidationFailure)
