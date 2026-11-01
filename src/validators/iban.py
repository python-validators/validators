"""IBAN."""

# standard
import re

# local
from .utils import validator

# Swift IBAN Registry, release 103 (September 2026).
# https://www.swift.com/resource/iban-registry-pdf
_COUNTRY_LENGTHS = {
    "AD": 24,
    "AE": 23,
    "AL": 28,
    "AT": 20,
    "AZ": 28,
    "BA": 20,
    "BE": 16,
    "BG": 22,
    "BH": 22,
    "BI": 27,
    "BR": 29,
    "BY": 28,
    "CH": 21,
    "CR": 22,
    "CY": 28,
    "CZ": 24,
    "DE": 22,
    "DJ": 27,
    "DK": 18,
    "DO": 28,
    "EE": 20,
    "EG": 29,
    "ES": 24,
    "FI": 18,
    "FK": 18,
    "FO": 18,
    "FR": 27,
    "GB": 22,
    "GE": 22,
    "GI": 23,
    "GL": 18,
    "GR": 27,
    "GT": 28,
    "HN": 28,
    "HR": 21,
    "HU": 28,
    "IE": 22,
    "IL": 23,
    "IQ": 23,
    "IS": 26,
    "IT": 27,
    "JO": 30,
    "KW": 30,
    "KZ": 20,
    "LB": 28,
    "LC": 32,
    "LI": 21,
    "LT": 20,
    "LU": 20,
    "LV": 21,
    "LY": 25,
    "MC": 27,
    "MD": 24,
    "ME": 22,
    "MK": 19,
    "MN": 20,
    "MR": 27,
    "MT": 31,
    "MU": 30,
    "NI": 28,
    "NL": 18,
    "NO": 15,
    "OM": 23,
    "PK": 24,
    "PL": 28,
    "PS": 29,
    "PT": 25,
    "QA": 29,
    "RO": 24,
    "RS": 22,
    "RU": 33,
    "SA": 24,
    "SC": 31,
    "SD": 18,
    "SE": 24,
    "SI": 19,
    "SK": 24,
    "SM": 27,
    "SO": 23,
    "ST": 25,
    "SV": 28,
    "TL": 23,
    "TN": 24,
    "TR": 26,
    "UA": 29,
    "VA": 22,
    "VG": 24,
    "XK": 20,
    "YE": 30,
}


def _char_value(char: str):
    """A=10, B=11, ..., Z=35 (case-insensitive)."""
    return char if char.isdigit() else str(10 + ord(char.upper()) - ord("A"))


def _mod_check(value: str):
    """Check if the value string passes the mod97-test."""
    # move country code and check numbers to end
    rearranged = value[4:] + value[:4]
    return int("".join(_char_value(char) for char in rearranged)) % 97 == 1


@validator
def iban(value: str, /):
    """Return whether or not given value is a valid IBAN code.

    Check the registered country code, national length, and checksum.
    This does not check all national account rules or whether the account exists.

    Examples:
        >>> iban('DE29100500001061045672')
        True
        >>> iban('123456')
        ValidationError(func=iban, args={'value': '123456'})

    Args:
        value:
            IBAN string to validate.

    Returns:
        (Literal[True]): If `value` is a valid IBAN code.
        (ValidationError): If `value` is an invalid IBAN code.
    """
    return (
        (
            re.match(r"^[a-z]{2}[0-9]{2}[a-z0-9]{11,30}$", value, re.IGNORECASE | re.ASCII)
            and len(value) == _COUNTRY_LENGTHS.get(value[:2].upper())
            and _mod_check(value)
        )
        if value
        else False
    )
