"""Test IBAN."""

# external
import pytest

# local
from validators import ValidationError, iban


@pytest.mark.parametrize("value", ["GB82WEST12345698765432", "NO9386011117947"])
def test_returns_true_on_valid_iban(value: str):
    """Test returns true on valid iban."""
    assert iban(value)


@pytest.mark.parametrize("value", ["GB81WEST12345698765432", "NO9186011117947"])
def test_returns_failed_validation_on_invalid_iban(value: str):
    """Test returns failed validation on invalid iban."""
    assert isinstance(iban(value), ValidationError)


@pytest.mark.parametrize("value", ["   ", "\t", "\n"])
def test_returns_failed_validation_on_whitespace_only_iban(value: str):
    """Test returns failed validation on whitespace-only iban."""
    assert isinstance(iban(value), ValidationError)


@pytest.mark.parametrize("value", ["gb82west12345698765432", "no9386011117947"])
def test_returns_failed_validation_on_lowercase_iban(value: str):
    """Test returns failed validation on lowercase iban (no normalization)."""
    assert isinstance(iban(value), ValidationError)


@pytest.mark.parametrize(
    "value",
    [
        "XX82WEST12345698765432",
        "ZZ9386011117947",
        "QQ12345678901234567890123",
    ],
)
def test_returns_failed_validation_on_invalid_country_code(value: str):
    """Test returns failed validation on invalid country code prefix."""
    assert isinstance(iban(value), ValidationError)
