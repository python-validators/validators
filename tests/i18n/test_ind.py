"""Test Indian validators."""

# external
import pytest

# local
from validators import ValidationError
from validators.i18n import ind_aadhar, ind_pan


@pytest.mark.parametrize("value", ["3675 9834 6012", "5046 3182 4299"])
def test_returns_true_on_valid_ind_aadhar(value: str):
    """Test returns true on valid ind aadhar."""
    assert ind_aadhar(value)


@pytest.mark.parametrize("value", ["3675 9834 6012 8", "417598346012", "3675 98AF 60#2"])
def test_returns_failed_validation_on_invalid_ind_aadhar(value: str):
    """Test returns failed validation on invalid ind aadhar."""
    assert isinstance(ind_aadhar(value), ValidationError)


@pytest.mark.parametrize("value", ["ABCDE9999K", "AAAPL1234C"])
def test_returns_true_on_valid_ind_pan(value: str):
    """Test returns true on valid ind pan."""
    assert ind_pan(value)


@pytest.mark.parametrize(
    "value", ["ABC5d7896B", "417598346012", "AaaPL1234C", "ABCDE9999Kextra", "ABCDE9999K "]
)
def test_returns_failed_validation_on_invalid_ind_pan(value: str):
    """Test returns failed validation on invalid ind pan."""
    assert isinstance(ind_pan(value), ValidationError)


@pytest.mark.parametrize(
    "value", ["3\u066675 9834 6012", "3675 9834 601\uff12", "3675\u00a09834 6012"]
)
def test_returns_failed_validation_on_non_ascii_digits_or_spaces_in_ind_aadhar(value: str):
    """Test returns failed validation on digits or spaces outside ASCII."""
    assert isinstance(ind_aadhar(value), ValidationError)


@pytest.mark.parametrize("value", ["ABCDE\u0669999K", "ABCDE999\uff19K"])
def test_returns_failed_validation_on_non_ascii_digits_in_ind_pan(value: str):
    """Test returns failed validation when a script other than ASCII supplies the digits."""
    assert isinstance(ind_pan(value), ValidationError)
