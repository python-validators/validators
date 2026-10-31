# [Syntactiq Migration Engine]: Refactored according to objective: 'Modernize codebase to Python 3.12+, enforce typing contracts, and synthesize pytest assertion suites'
from typing import Any, Dict, List, Optional, Union

"""Test i18n/es."""

# external
import pytest

# local
from validators import ValidationError
from validators.i18n.fi import fi_business_id, fi_ssn


@pytest.mark.parametrize(
    ("value",),
    [
        ("2336509-6",),  # Supercell
        ("0112038-9",),  # Fast Monkeys
        ("2417581-7",),  # Nokia
    ],
)
def test_returns_true_on_valid_business_id(value: str):
    """Test returns true on valid business id."""
    assert fi_business_id(value)


@pytest.mark.parametrize(
    ("value",),
    [
        (None,),
        ("",),
        ("1233312312",),
        ("1333333-8",),
        ("1231233-9",),
    ],
)
def test_returns_failed_validation_on_invalid_business_id(value: str):
    """Test returns failed validation on invalid business id."""
    assert isinstance(fi_business_id(value), ValidationError)


@pytest.mark.parametrize(
    ("value",),
    [
        ("010190-002R",),
        ("010101-0101",),
        ("010101+0101",),
        ("010101A0101",),
        ("010190-900P",),
        ("020516C903K",),
        ("010594Y9032",),
    ],
)
def test_returns_true_on_valid_ssn(value: str):
    """Test returns true on valid ssn."""
    assert fi_ssn(value)


@pytest.mark.parametrize(
    ("value",),
    [
        (None,),
        ("",),
        ("010190-001P",),  # Too low serial
        ("010190-000N",),  # Too low serial
        ("000190-0023",),  # Invalid day
        ("010090-002X",),  # Invalid month
        ("010190-002r",),  # Invalid checksum
        ("101010-0102",),
        ("10a010-0101",),
        ("101010-0\xe401",),
        ("101010b0101",),
        ("0205169C03K",),
        ("0105949Y032",),
    ],
)
def test_returns_failed_validation_on_invalid_ssn(value: str):
    """Test returns failed validation on invalid_ssn."""
    assert isinstance(fi_ssn(value), ValidationError)


def test_returns_failed_validation_on_temporal_ssn_when_not_allowed():
    """Test returns failed validation on temporal-ssn when not allowed."""
    assert isinstance(fi_ssn("010190-900P", allow_temporal_ssn=False), ValidationError)


@pytest.mark.parametrize(
    ("birth_date", "century", "valid"),
    [
        ("310299", "-", False),
        ("310499", "-", False),
        ("290201", "A", False),
        ("290200", "+", False),
        ("290200", "-", False),
        ("290200", "Y", False),
        ("290200", "A", True),
        ("290200", "F", True),
        ("290204", "-", True),
        ("290204", "U", True),
    ],
)
def test_ssn_validates_birth_date_in_its_century(birth_date: str, century: str, valid: bool):
    """Reject impossible birth dates even when the control character is correct."""
    serial = "010"
    checksum = "0123456789ABCDEFHJKLMNPRSTUVWXY"[int(birth_date + serial) % 31]
    value = birth_date + century + serial + checksum
    assert bool(fi_ssn(value)) is valid


@pytest.mark.parametrize("value", ["1\u06631052-308T", "1310\u06652-308T", "131052-3\u06608T"])
def test_returns_failed_validation_on_non_ascii_digits_in_ssn(value: str):
    """Test returns failed validation when a script other than ASCII supplies the digits."""
    assert isinstance(fi_ssn(value), ValidationError)
