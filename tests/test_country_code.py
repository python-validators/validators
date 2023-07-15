# external
import pytest

# local
from validators import country_code, ValidationFailure


@pytest.mark.parametrize(
    ("value", "code", "expected_result"),
    [
        ("US", "alpha2", True),
        ("us", "alpha2", True),
        ("usa", "alpha2", False),
        ("CA", "alpha2", True),
        ("840", "numeric", True),
        ("123", "numeric", False),
        ("USA", "alpha3", True),
        ("fre", "alpha3", False),
        ("ABCD", "auto", False),
        ("123456", "auto", False),
        ("XX", "auto", False),
        ("USA", "auto", True),
        ("840", "auto", True),
    ],
)
def test_country_code_validation(value: str, code: str, expected_result: bool):
    """Test country_code function for various country codes."""
    result = country_code(value, code=code)
    if expected_result:
        assert result is True
    else:
        assert isinstance(result, ValidationFailure)


@pytest.mark.parametrize(
    ("value", "code"),
    [
        ("USA", "alpha2"),
        ("us", "alpha3"),
        ("840", "alpha2"),
        ("124", "alpha3"),
        ("USA", "numeric"),
        ("fra", "numeric"),
    ],
)
def test_country_code_invalid_type(value: str, code: str):
    """Test country_code function for invalid code types."""
    assert isinstance(country_code(value, code=code), ValidationFailure)


@pytest.mark.parametrize(
    ("value", "code"),
    [
        ("123456", "auto"),
        ("XX", "auto"),
        ("1nd", "auto"),
        ("4", "auto"),
        ("CaLi", "auto"),
    ],
)
def test_country_code_auto_invalid(value: str, code: str):
    """Test country_code function for invalid auto identification."""
    assert isinstance(country_code(value, code=code), ValidationFailure)
