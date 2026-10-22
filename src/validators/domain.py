"""Domain."""

# standard
from os import environ
from pathlib import Path
import re
from stringprep import in_table_b1
from typing import Optional, Set
from unicodedata import normalize

# local
from .utils import validator


class _IanaTLD:
    """Read IANA TLDs, and optionally cache them."""

    _full_cache: Optional[Set[str]] = None
    # source: https://www.statista.com/statistics/265677
    _popular_cache = {"COM", "ORG", "RU", "DE", "NET", "BR", "UK", "JP", "FR", "IT"}
    _popular_cache.add("ONION")

    @classmethod
    def _retrieve(cls):
        with Path(__file__).parent.joinpath("_tld.txt").open() as tld_f:
            _ = next(tld_f)  # ignore the first line
            for line in tld_f:
                yield line.strip()

    @classmethod
    def check(cls, tld: str):
        if tld in cls._popular_cache:
            return True
        if cls._full_cache is None:
            if environ.get("PYVLD_CACHE_TLD") == "True":
                cls._full_cache = set(cls._retrieve())
            else:
                return tld in cls._retrieve()
        return tld in cls._full_cache


def _relies_on_idna_mapping(value: str):
    """Return whether `value` only becomes a valid name through IDNA 2003 mapping.

    Python's `idna` codec implements IDNA 2003 (RFC 3490), whose nameprep step
    (RFC 3491) drops invisible characters (RFC 3454, table B.1), folds
    compatibility characters such as fullwidth letters to ASCII, and treats
    U+3002 and similar dots as label separators. A value that needs any of
    these only looks like the name it encodes to, e.g. "example.com" written
    with fullwidth letters.
    """
    return not value.isascii() and (
        normalize("NFKC", value) != value
        or any(in_table_b1(char) or char in "\u3002\uff0e\uff61" for char in value)
    )


@validator
def domain(
    value: str, /, *, consider_tld: bool = False, rfc_1034: bool = False, rfc_2782: bool = False
):
    """Return whether or not given value is a valid domain.

    Examples:
        >>> domain('example.com')
        True
        >>> domain('example.com/')
        ValidationError(func=domain, args={'value': 'example.com/'})
        >>> # Supports IDN domains as well::
        >>> domain('xn----gtbspbbmkef.xn--p1ai')
        True

    Args:
        value:
            Domain string to validate.
        consider_tld:
            Restrict domain to TLDs allowed by IANA.
        rfc_1034:
            Allows optional trailing dot in the domain name.
            Ref: [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034).
        rfc_2782:
            Domain name is of type service record.
            Allows optional underscores in the domain name.
            Ref: [RFC 2782](https://www.rfc-editor.org/rfc/rfc2782).


    Returns:
        (Literal[True]): If `value` is a valid domain name.
        (ValidationError): If `value` is an invalid domain name.

    Raises:
        (UnicodeError): If `value` cannot be encoded into `idna` or decoded into `utf-8`.
    """
    if not value:
        return False

    try:
        if _relies_on_idna_mapping(value):
            return False

        if value.rstrip(".").rsplit(".", 1)[-1].isdecimal():
            # ref: RFC 1123 (2.1) and RFC 3696 (2), a TLD is not all-numeric. An
            # all-digit IDN label like "\u0661" is, but encodes to a letter-final A-label.
            return False

        service_record = r"_" if rfc_2782 else ""
        trailing_dot = r"\.?$" if rfc_1034 else r"$"

        encoded = value.encode("idna").decode("utf-8")
        if len(encoded.rstrip(".")) > 253:
            # ref: RFC 1035, presentation form is limited to 253 characters
            return False

        # IANA lists IDN TLDs in their ASCII (punycode) form,
        # so look up the encoded TLD, not the raw one.
        if consider_tld and not _IanaTLD.check(encoded.rstrip(".").rsplit(".", 1)[-1].upper()):
            return False

        return not re.search(r"\s|__+", value) and re.match(
            # First character of the domain
            rf"^(?:[a-z0-9{service_record}]"
            # Sub-domain
            + rf"(?:[a-z0-9-{service_record}]{{0,61}}"
            # Hostname
            + rf"[a-z0-9{service_record}])?\.)"
            # First 61 characters of the gTLD. An underscore belongs
            # in a service label, not here.
            + r"+[a-z0-9][a-z0-9-]{0,61}"
            # Last character of the gTLD
            + rf"[a-z]{trailing_dot}",
            encoded,
            re.IGNORECASE,
        )
    except UnicodeError as err:
        raise UnicodeError(f"Unable to encode/decode {value}") from err
