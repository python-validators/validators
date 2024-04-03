"""Test Encodings."""

# external
import pytest

# local
from validators import ValidationError, base58, base64

# ==> base58 <== #


@pytest.mark.parametrize(
    "value",
    [
        "cUSECaVvAiV3srWbFRvVPzm5YzcXJwPSwZfE7veYPHoXmR9h6YMQ",
        "18KToMF5ckjXBYt2HAj77qsG3GPeej3PZn",
        "n4FFXRNNEW1aA2WPscSuzHTCjzjs4TVE2Z",
        "38XzQ9dPGb1uqbZsjPtUajp7omy8aefjqj",
    ],
)
def test_returns_true_on_valid_base58(value: str):
    """Test returns true on valid base58."""
    assert base58(value)


@pytest.mark.parametrize(
    "value",
    ["ThisIsAReallyLongStringThatIsDefinitelyNotBase58Encoded", "abcABC!@#", "InvalidBase58!"],
)
def test_returns_failed_validation_on_invalid_base58(value: str):
    """Test returns failed validation on invalid base58."""
    assert isinstance(base58(value), ValidationError)


# ==> base64 <== #


@pytest.mark.parametrize(
    "value",
    ["SGVsbG8gV29ybGQ=", "U29tZSBkYXRhIHN0cmluZw==", "YW55IGNhcm5hbCBwbGVhcw=="],
)
def test_returns_true_on_valid_base64(value: str):
    """Test returns true on valid base64."""
    assert base64(value)


@pytest.mark.parametrize(
    "value",
    ["SGVsbG8gV29ybGQ", "U29tZSBkYXRhIHN0cmluZw", "YW55IGNhcm5hbCBwbGVhc"],
)
def test_returns_failed_validation_on_invalid_base64(value: str):
    """Test returns failed validation on invalid base64."""
    assert isinstance(base64(value), ValidationError)
