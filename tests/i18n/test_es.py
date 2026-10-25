"""Test i18n/es."""

from typing import Callable

# external
import pytest

# local
from validators import ValidationError, es_cif, es_doi, es_nie, es_nif


@pytest.mark.parametrize(
    ("value",),
    [
        ("B25162520",),
        ("U4839822F",),
        ("B96817697",),
        ("P7067074J",),
        ("Q7899705C",),
        ("C75098681",),
        ("G76061860",),
        ("C71345375",),
        ("G20558169",),
        ("U5021960I",),
    ],
)
def test_returns_true_on_valid_cif(value: str):
    """Test returns true on valid cif."""
    assert es_cif(value)


@pytest.mark.parametrize(
    ("value",),
    [
        ("12345",),
        ("ABCDEFGHI",),
        ("Z5021960I",),
    ],
)
def test_returns_false_on_invalid_cif(value: str):
    """Test returns false on invalid cif."""
    result = es_cif(value)
    assert isinstance(result, ValidationError)


@pytest.mark.parametrize(
    ("value",),
    [
        ("X0095892M",),
        ("X8868108K",),
        ("X2911154K",),
        ("Y2584969J",),
        ("X7536157T",),
        ("Y5840388N",),
        ("Z2915723H",),
        ("Y4002236C",),
        ("X7750702R",),
        ("Y0408759V",),
    ],
)
def test_returns_true_on_valid_nie(value: str):
    """Test returns true on valid nie."""
    assert es_nie(value)


@pytest.mark.parametrize("validate", [es_nie, es_doi])
@pytest.mark.parametrize("value", ["X0095892M", "Y2584969J", "Z2915723H"])
def test_nie_accepts_lowercase_prefix(validate: Callable[[str], object], value: str):
    """Accept lowercase NIE prefixes consistently with NIF and CIF letters."""
    assert validate(value[0].lower() + value[1:]) is True
    assert validate(value.lower()) is True


@pytest.mark.parametrize("validate", [es_nie, es_doi])
@pytest.mark.parametrize("value", ["x0095892x", "y2584969x", "z2915723x"])
def test_lowercase_nie_still_checks_checksum(validate: Callable[[str], object], value: str):
    """Do not accept an invalid checksum after normalizing the prefix."""
    assert isinstance(validate(value), ValidationError)


@pytest.mark.parametrize(
    ("value",),
    [
        ("K0000023T",),
        ("L0000024R",),
        ("M0000025W",),
        ("00000026A",),
        ("00000027G",),
        ("00000028M",),
        ("00000029Y",),
        ("00000030F",),
        ("00000031P",),
        ("00000032D",),
        ("00000033X",),
        ("00000034B",),
        ("00000035N",),
        ("00000036J",),
        ("00000037Z",),
        ("00000038S",),
        ("00000039Q",),
        ("00000040V",),
        ("00000041H",),
        ("00000042L",),
        ("00000043C",),
        ("00000044K",),
        ("00000045E",),
    ],
)
def test_returns_true_on_valid_nif(value: str):
    """Test returns true on valid nif."""
    assert es_nif(value)


def test_returns_false_on_invalid_nif():
    """Test returns false on invalid nif."""
    result = es_nif("12345")
    assert isinstance(result, ValidationError)


@pytest.mark.parametrize(
    ("value",),
    [
        # CIFs
        ("B25162520",),
        ("U4839822F",),
        ("B96817697",),
        # NIEs
        ("X0000000T",),
        ("X0095892M",),
        ("X8868108K",),
        ("X2911154K",),
        # NIFs
        ("00000001R",),
        ("00000000T",),
        ("26643189N",),
        ("07060225F",),
        ("49166693F",),
    ],
)
def test_returns_true_on_valid_doi(value: str):
    """Test returns true on valid doi."""
    assert es_doi(value)


@pytest.mark.parametrize(
    "digits",
    [
        "\uff10\uff11\uff12\uff13\uff14\uff15\uff16\uff17\uff18\uff19",
        "\u0660\u0661\u0662\u0663\u0664\u0665\u0666\u0667\u0668\u0669",
        "\u0966\u0967\u0968\u0969\u096a\u096b\u096c\u096d\u096e\u096f",
    ],
)
@pytest.mark.parametrize(
    "validate,value",
    [
        (es_nif, "26643189N"),
        (es_nie, "X0095892M"),
        (es_cif, "B25162520"),
        (es_doi, "26643189N"),
        (es_doi, "X0095892M"),
        (es_doi, "B25162520"),
    ],
)
def test_spanish_identifiers_reject_non_ascii_digits(
    validate: Callable[[str], object], value: str, digits: str
):
    """Reject lookalike digit bodies even when their numeric checksums agree."""
    translated = value[:-1].translate(str.maketrans("0123456789", digits)) + value[-1]
    assert validate(value) is True
    assert isinstance(validate(translated), ValidationError)
