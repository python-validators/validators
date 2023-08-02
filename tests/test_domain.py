"""Test Domain."""

# external
import pytest

# local
from validators import ValidationError, domain


@pytest.mark.parametrize(
    ("value", "rfc_1034", "rfc_2782"),
    [
        ("example.com", False, False),
        ("xn----gtbspbbmkef.xn--p1ai", False, False),
        ("underscore_subdomain.example.com", False, False),
        ("something.versicherung", False, False),
        ("someThing.versicherung.", True, False),
        ("11.com", False, False),
        ("3.cn.", True, False),
        ("_example.com", False, True),
        ("a.cn", False, False),
        ("sub1.sub2.sample.co.uk", False, False),
        ("somerandomexample.xn--fiqs8s", False, False),
        ("kräuter.com.", True, False),
        ("über.com", False, False),
    ],
)
def test_returns_true_on_valid_domain(value: str, rfc_1034: bool, rfc_2782: bool):
    """Test returns true on valid domain."""
    assert domain(value, rfc_1034=rfc_1034, rfc_2782=rfc_2782)


@pytest.mark.parametrize(
    ("value", "rfc_1034", "rfc_2782"),
    [
        ("example.com/.", True, False),
        ("example.com:4444", False, False),
        ("example.-com", False, False),
        ("example.", False, False),
        ("-example.com", False, False),
        ("example-.com.", True, False),
        ("_example.com", False, False),
        ("_example._com", False, False),
        ("example_.com", False, False),
        ("example", False, False),
        ("a......b.com", False, False),
        ("a.123", False, False),
        ("123.123", False, False),
        ("123.123.123.", True, False),
        ("123.123.123.123", False, False),
    ],
)
def test_returns_failed_validation_on_invalid_domain(value: str, rfc_1034: bool, rfc_2782: bool):
    """Test returns failed validation on invalid domain."""
    assert isinstance(domain(value, rfc_1034=rfc_1034, rfc_2782=rfc_2782), ValidationError)
