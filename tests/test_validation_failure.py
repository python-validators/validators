"""Test validation Failure."""

# external
import pytest

# local
from validators import between, cron, email, hostname, uuid
from validators.utils import ValidationError

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


@pytest.mark.parametrize("validator", [uuid, email, hostname, cron])
@pytest.mark.parametrize("value", [123, 1.5, True, ["x"], {"a": 1}])
def test_returns_validation_error_on_non_string_input(validator, value):
    """Wrong-typed input returns ValidationError, not a leaked exception.

    These validators reach for string methods (e.g. ``.replace``/``.count``/
    ``.strip``) on the value, which raises ``AttributeError`` for non-strings.
    The decorator must convert that into a ``ValidationError`` like every other
    invalid input, rather than letting it escape.
    """
    assert isinstance(validator(value), ValidationError)
