"""Test validation Failure."""

# standard
from functools import partial

# external
import pytest

# local
from validators import ValidationError, between, validator

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


def test_partial_validation_error_representation():
    """Validation errors support partial callables without a name attribute."""

    def above(value: int, minimum: int) -> bool:
        return value > minimum

    check = validator(partial(above, minimum=3))
    error = check(1)
    assert isinstance(error, ValidationError)
    assert repr(error) == "ValidationError(func=partial, args={'value': 1})"
    assert str(error) == repr(error)
    assert check(4) is True


def test_callable_instance_validation_error_representation():
    """Callable instance errors use their type name."""

    class Positive:
        def __call__(self, *, value: int) -> bool:
            return value > 0

    error = validator(Positive())(value=-1)
    assert isinstance(error, ValidationError)
    assert repr(error) == "ValidationError(func=Positive, args={'value': -1})"


def test_builtin_validation_error_keeps_raw_arguments():
    """An unavailable builtin signature must not hide its validation error."""
    check = validator(int)
    error = check("invalid")
    assert isinstance(error, ValidationError)
    assert "func=int" in repr(error)
    assert error.__dict__["args"] == ("invalid",)
    assert error.__dict__["kwargs"] == {}
    assert "invalid literal" in error.reason
    assert check("42") is True

    with pytest.raises(ValidationError, match="func=int"):
        check("invalid", r_ve=True)
