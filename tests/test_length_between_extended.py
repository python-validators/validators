"""Extended coverage for length, between and the AbsMin/AbsMax extremes.

The existing tests for these modules are short (length: 25 lines,
between: 40 lines); this file pins the boundary behaviour the existing
suite does not cover. Every assertion below was verified against the
cloned source with a probe script before being written here.

Note on failure reporting: the ``@validator`` decorator converts
``ValueError``/``TypeError`` raised inside a validator into a returned
``ValidationError`` object (unless ``r_ve=True``), so the tests below
assert ``ValidationError`` instances, not raised exceptions.
"""

from datetime import datetime

import pytest

from validators import ValidationError, between, length
from validators._extremes import AbsMax, AbsMin


# ---------------------------------------------------------------- length


@pytest.mark.parametrize(
    ("value", "min_val", "max_val"),
    [
        ("", 0, 0),  # empty string is a valid zero-length value
        ("abc", None, None),  # no bounds at all
        ("abc", 3, 3),  # exact length
        ("abc", 0, 10),
        ("abc", 3, None),
        ("abc", None, 3),
        ("12345", 5, None),
        ("héllo", 5, 5),  # len() counts code points, not bytes
        ("a b", 3, 3),  # spaces count towards the length
    ],
)
def test_length_returns_true_on_valid_lengths(value, min_val, max_val):
    assert length(value, min_val=min_val, max_val=max_val) is True


@pytest.mark.parametrize(
    ("value", "min_val", "max_val"),
    [
        ("abc", 4, None),
        ("abc", None, 2),
        ("abc", 5, 2),  # min > max can never match
        ("", 1, None),
    ],
)
def test_length_returns_failed_validation_on_invalid_lengths(value, min_val, max_val):
    assert isinstance(
        length(value, min_val=min_val, max_val=max_val), ValidationError
    )


@pytest.mark.parametrize("kwargs", [{"min_val": -1}, {"max_val": -1}])
def test_length_negative_bound_is_a_failed_validation_not_a_raise(kwargs):
    # The ValueError raised inside length() is swallowed by @validator.
    result = length("abc", **kwargs)
    assert isinstance(result, ValidationError)
    assert "negative" in result.reason


def test_length_r_ve_raises_validation_error():
    with pytest.raises(ValidationError):
        length("x", min_val=5, r_ve=True)


def test_length_r_ve_true_returns_true_on_valid():
    assert length("abc", min_val=2, r_ve=True) is True


# ---------------------------------------------------------------- between


@pytest.mark.parametrize(
    ("value", "min_val", "max_val"),
    [
        (5, None, None),  # no bounds: always True (except None value)
        (5, 5, 5),  # inclusive bounds
        (0, -1, 0),
        (-5, -10, -1),
        (1.5, 1, 2),  # floats mix with ints
        (13.2, 13, 14),
        ("b", "a", "c"),  # strings compare lexicographically
        ("a", "a", "c"),  # lower bound is inclusive
        (datetime(2020, 1, 1), datetime(2019, 1, 1), datetime(2021, 1, 1)),
        (datetime(2020, 1, 1), None, datetime(2021, 1, 1)),
        (True, 0, 1),  # bool is an int subclass
    ],
)
def test_between_returns_true_on_valid_ranges(value, min_val, max_val):
    assert between(value, min_val=min_val, max_val=max_val) is True


@pytest.mark.parametrize(
    ("value", "min_val", "max_val"),
    [
        (None, 1, 2),  # None is never "between" anything
        (None, None, None),
        (4, 5, 10),
        (11, 5, 10),
        (5, 10, 2),  # min > max
        ("d", "a", "c"),
        (datetime(2022, 1, 1), datetime(2019, 1, 1), datetime(2021, 1, 1)),
    ],
)
def test_between_returns_failed_validation_on_invalid_ranges(value, min_val, max_val):
    assert isinstance(
        between(value, min_val=min_val, max_val=max_val), ValidationError
    )


def test_between_min_greater_than_max_carries_the_reason():
    result = between(5, min_val=10, max_val=2)
    assert isinstance(result, ValidationError)
    assert result.reason == "`min_val` cannot be greater than `max_val`"


def test_between_type_mismatch_min_vs_value_carries_the_reason():
    # "a" <= 5 raises TypeError inside between(); @validator converts it.
    result = between(5, min_val="a", max_val="z")
    assert isinstance(result, ValidationError)
    assert "<=" in result.reason


def test_between_type_mismatch_min_vs_max_carries_the_reason():
    # 1 > "z" raises TypeError while checking min <= max.
    result = between(5, min_val=1, max_val="z")
    assert isinstance(result, ValidationError)
    assert result.reason == "Comparison type mismatch"


def test_between_accepts_explicit_extremes():
    assert between(5, min_val=AbsMin(), max_val=AbsMax()) is True
    assert between("anything", min_val=AbsMin(), max_val=AbsMax()) is True


# ---------------------------------------------------------------- extremes


def test_absmax_is_greater_than_everything():
    assert AbsMax() > AbsMin()
    assert AbsMax() > 99999999999999999
    assert AbsMax() > float("inf")


def test_absmin_is_smaller_than_everything():
    assert AbsMin() < -99999999999999999
    assert AbsMin() < ""
    assert AbsMin() < None


def test_extremes_compare_against_their_own_class_not_instance():
    # Quirk pinned as-is: __ge__/__le__ compare `other` against the *class*,
    # so an extreme compares True against another instance of itself...
    assert AbsMax() >= AbsMax()
    assert AbsMin() <= AbsMin()
    # ...while equality is still plain identity (total_ordering adds no __eq__).
    assert AbsMax() != AbsMax()
    assert (AbsMax() == AbsMax()) is False


def test_extremes_bracket_any_value():
    assert AbsMin() < 0 < AbsMax()
    assert AbsMin() < AbsMax()
    assert not (AbsMax() < AbsMin())
