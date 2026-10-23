"""Test Country."""

# external
import pytest

# local
from validators import ValidationError, calling_code, country_code, currency


@pytest.mark.parametrize(("value"), ["+1", "+371"])
def test_returns_true_on_valid_calling_code(value: str):
    """Test returns true on valid calling code."""
    assert calling_code(value)


@pytest.mark.parametrize(("value"), ["+19", "+37", "-9"])
def test_returns_failed_validation_invalid_calling_code(value: str):
    """Test returns failed validation invalid calling code."""
    assert isinstance(calling_code(value), ValidationError)


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
    assert isinstance(country_code(value, iso_format=iso_format), ValidationError)


@pytest.mark.parametrize(
    ("value", "skip_symbols", "ignore_case"),
    [("$", False, False), ("⃀", False, False), ("৳", False, False), ("uSd", True, True)],
)
def test_returns_true_on_valid_currency(value: str, skip_symbols: bool, ignore_case: bool):
    """Test returns true on valid currency."""
    assert currency(value, skip_symbols=skip_symbols, ignore_case=ignore_case)


@pytest.mark.parametrize(
    ("value", "skip_symbols", "ignore_case"),
    [
        ("$", True, False),
        ("⃀", True, False),
        ("৳", True, False),
        ("⃀৳", False, False),
        ("uSd", True, False),
        ("Bucks", True, True),
    ],
)
def test_returns_failed_validation_invalid_currency(
    value: str, skip_symbols: bool, ignore_case: bool
):
    """Test returns failed validation invalid currency."""
    assert isinstance(
        currency(value, skip_symbols=skip_symbols, ignore_case=ignore_case), ValidationError
    )


@pytest.mark.parametrize("value", ["SLE", "XCG", "ZWG"])
@pytest.mark.parametrize("skip_symbols", [True, False])
def test_accepts_current_currency_codes(value: str, skip_symbols: bool):
    """Accept the current Leone, Caribbean guilder and Zimbabwe Gold codes."""
    assert currency(value, skip_symbols=skip_symbols) is True


@pytest.mark.parametrize("value", ["sle", "xcg", "zwg"])
def test_current_currency_codes_respect_ignore_case(value: str):
    """Only accept lowercase currency codes when case-insensitive matching is enabled."""
    assert isinstance(currency(value), ValidationError)
    assert currency(value, ignore_case=True) is True


@pytest.mark.parametrize("value", ["SLL", "ANG", "ZWL"])
def test_preserves_legacy_currency_codes(value: str):
    """Keep previously accepted codes when adding their current replacements."""
    assert currency(value) is True
