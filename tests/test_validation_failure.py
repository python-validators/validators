# [Syntactiq Migration Engine]: Refactored according to objective: 'Modernize codebase to Python 3.12+, enforce typing contracts, and synthesize pytest assertion suites'
"""Test validation Failure."""

# standard
from typing import Any, Callable

# third-party
import pytest

# local
from validators import ValidationError, between, slug, uuid


@pytest.mark.parametrize("function,value", [(slug, "invalid_"), (uuid, "not-a-uuid")])
def test_false_raise_validation_error_flag(
    function: Callable[..., Any], value: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A false flag returns validation errors instead of raising them."""
    monkeypatch.delenv("RAISE_VALIDATION_ERROR", raising=False)
    result = function(value, r_ve=False)
    assert isinstance(result, ValidationError)
    assert not result


@pytest.mark.parametrize("function,value", [(slug, "invalid_"), (uuid, "not-a-uuid")])
def test_environment_still_enables_raise_validation_error(
    function: Callable[..., Any], value: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    """The environment option enables raising even when the call flag is false."""
    monkeypatch.setenv("RAISE_VALIDATION_ERROR", "True")
    with pytest.raises(ValidationError):
        function(value, r_ve=False)


@pytest.mark.parametrize("function,value", [(slug, "invalid_"), (uuid, "not-a-uuid")])
def test_true_raise_validation_error_flag(
    function: Callable[..., Any], value: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A true call flag continues to raise validation errors."""
    monkeypatch.delenv("RAISE_VALIDATION_ERROR", raising=False)
    with pytest.raises(ValidationError):
        function(value, r_ve=True)


failed_obj_repr = "ValidationError(func=between"


class TestValidationError:
    """Test validation Failure."""

    def setup_method(self):
        """Setup Method."""
        self.is_in_between = between(3, min_val=4, max_val=5)

    def test_boolean_coerce(self):
        """Test Boolean."""
        assert not bool(self.is_in_between)
        assert not self.is_in_between

    def test_repr(self):
        """Test Repr."""
        assert failed_obj_repr in repr(self.is_in_between)

    def test_string(self):
        """Test Repr."""
        assert failed_obj_repr in str(self.is_in_between)

    def test_arguments_as_properties(self):
        """Test argument properties."""
        assert self.is_in_between.__dict__["value"] == 3
        assert self.is_in_between.__dict__["min_val"] == 4
        assert self.is_in_between.__dict__["max_val"] == 5
