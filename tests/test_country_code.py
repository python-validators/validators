# external
import pytest

# local
from validators import country_code, ValidationFailure


@pytest.mark.parametrize(
    ("value", "iso_format"),
    [
        ("ISR", "auto"),
        ("US", "alpha2"),
        ("USA", "alpha3"),
        ("840", "numeric"),
    ],
)
def test_returns_true_on_valid_country_code(value: str, iso_format: str):
    """Test returns true on valid country code."""
    assert country_code(value, iso_format=iso_format)


@pytest.mark.parametrize(
    ("value", "iso_format"),
    [
        (None, "auto"),
        ("", "auto"),
        ("123456", "auto"),
        ("XY", "alpha2"),
        ("PPP", "alpha3"),
        ("123", "numeric"),
        ("us", "auto"),
        ("uSa", "auto"),
        ("US ", "auto"),
        ("U.S", "auto"),
        ("1ND", "unknown"),
        ("ISR", None),
    ],
)
def test_returns_failed_validation_on_invalid_country_code(value: str, iso_format: str):
    """Test returns failed validation on invalid country code."""
    assert isinstance(country_code(value, iso_format=iso_format), ValidationFailure)
