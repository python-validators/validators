"""Test i18n/inn."""

# external
import pytest

# local
from validators import ValidationError
from validators.i18n.ru import ru_inn


@pytest.mark.parametrize(
    ("value",),
    [
        ("2222058686",),
        ("7709439560",),
        ("5003052454",),
        ("7730257499",),
        ("3664016814",),
        ("026504247480",),
        ("780103209220",),
        ("7707012148",),
        ("140700989885",),
        ("774334078053",),
    ],
)
def test_returns_true_on_valid_ru_inn(value: str):
    """Test returns true on valid russian individual tax number."""
    assert ru_inn(value)


@pytest.mark.parametrize(
    ("value",),
    [
        ("2222058687",),
        ("7709439561",),
        ("5003052453",),
        ("7730257490",),
        ("3664016815",),
        ("026504247481",),
        ("780103209222",),
        ("7707012149",),
        ("140700989886",),
        ("774334078054",),
    ],
)
def test_returns_false_on_valid_ru_inn(value: str):
    """Test returns true on valid russian individual tax number."""
    assert isinstance(ru_inn(value), ValidationError)


@pytest.mark.parametrize(
    "value",
    [
        "500100732266",  # First check digit is wrong; the second matches.
        "100000001103",  # First remainder is 10; the second check digit is wrong.
        "100000000781",  # Second remainder is 10; its check digit must be zero.
    ],
)
def test_individual_inn_requires_both_check_digits(value: str):
    """Reject an individual INN when either check digit is wrong."""
    assert isinstance(ru_inn(value), ValidationError)


@pytest.mark.parametrize("value", ["500100732259", "100000001102", "100000000780"])
def test_individual_inn_check_digit_remainders(value: str):
    """Accept both ordinary remainders and remainder 10 mapped to zero."""
    assert ru_inn(value) is True


@pytest.mark.parametrize("value", ["7830002293", "500100732259"])
@pytest.mark.parametrize("zero", ["\u0660", "\uff10", "\u0966"])
def test_rejects_non_ascii_inn_digits(value: str, zero: str):
    """Reject digit lookalikes in company and individual INNs."""
    translated = value.translate(
        str.maketrans("0123456789", "".join(chr(ord(zero) + n) for n in range(10)))
    )
    assert isinstance(ru_inn(translated), ValidationError)
    assert ru_inn(value) is True


@pytest.mark.parametrize("value", ["7830002293", "500100732259"])
@pytest.mark.parametrize("position", [0, -1])
def test_rejects_mixed_ascii_and_non_ascii_inn_digits(value: str, position: int):
    """A single non-ASCII digit must not be normalized by int()."""
    digits = list(value)
    digits[position] = chr(ord("\u0660") + int(digits[position]))
    assert isinstance(ru_inn("".join(digits)), ValidationError)
