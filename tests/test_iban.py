"""Test IBAN."""

# external
import pytest

# local
from validators import ValidationError, iban


@pytest.mark.parametrize(
    "value",
    [
        "GB82WEST12345698765432",
        "NO9386011117947",
        "DE29100500001061045672",
        "LC55HEMM000100010012001200023015",
        "RU5600000000000000000000000000000",
    ],
)
def test_returns_true_on_valid_iban(value: str):
    """Test returns true on valid iban."""
    assert iban(value)


@pytest.mark.parametrize("value", ["gb82west12345698765432", "No9386011117947"])
def test_returns_true_on_valid_lowercase_iban(value: str):
    """Lowercase/mixed-case IBANs are accepted (the format regex is case-insensitive)."""
    assert iban(value)


@pytest.mark.parametrize(
    "value",
    [
        "GB81WEST12345698765432",
        "NO9186011117947",
        # These values have correct checksums but incorrect country lengths.
        "DE3110050000106104567",
        "DE631005000010610456720",
        "NO37860111179470",
        "LC67000000000000000000000000000",
        "RU56000000000000000000000000000000",
        # These prefixes have no registered IBAN format.
        "ZZ66000000000000000000",
        "US35000000000000000000",
    ],
)
def test_returns_failed_validation_on_invalid_iban(value: str):
    """Test returns failed validation on invalid iban."""
    assert isinstance(iban(value), ValidationError)


@pytest.mark.parametrize(
    "value", ["\u0131T60X0542811101000000123456", "GB82WE\u017fT12345698765432"]
)
def test_rejects_non_ascii_case_equivalents(value: str):
    """Unicode case equivalents must not pass the ASCII IBAN format check."""
    assert isinstance(iban(value), ValidationError)
