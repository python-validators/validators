"""Domain."""
# -*- coding: utf-8 -*-

# standard
import re
import requests

# local
from validators.utils import validator

# Function to download the TLD list and create a set of valid TLDs
def get_valid_tlds():
    response = requests.get("https://data.iana.org/TLD/tlds-alpha-by-domain.txt")
    tlds = response.text.strip().split("\n")[1:]
    return tlds

VALID_TLDS = get_valid_tlds()

@validator
def domain(value: str, /, *, rfc_1034: bool = False, rfc_2782: bool = False):
    """Return whether or not given value is a valid domain.

    Examples:
        >>> domain('example.com')
        # Output: True
        >>> domain('example.com/')
        # Output: ValidationFailure(func=domain, ...)
        >>> # Supports IDN domains as well::
        >>> domain('xn----gtbspbbmkef.xn--p1ai')
        # Output: True

    Args:
        value:
            Domain string to validate.
        rfc_1034:
            Allow trailing dot in domain name.
            Ref: [RFC 1034](https://www.rfc-editor.org/rfc/rfc1034).
        rfc_2782:
            Domain name is of type service record.
            Ref: [RFC 2782](https://www.rfc-editor.org/rfc/rfc2782).


    Returns:
        (Literal[True]):
            If `value` is a valid domain name.
        (ValidationFailure):
            If `value` is an invalid domain name.

    Note:
        - *In version 0.10.0*:
            - Added support for internationalized domain name (IDN) validation.

    > *New in version 0.9.0*.
    """
    if not value:
        return False
    try:
        if rfc_1034 and value.endswith("."):
            tld = value.rstrip(".")
        else:
            tld = value

        _ , tld = tld.rsplit(".", 1)
        if tld.upper() not in VALID_TLDS:
            return False
        
        return not re.search(r"\s", value) and re.match(
            # First character of the domain
            rf"^(?:[a-zA-Z0-9{'_'if rfc_2782 else ''}]"
            # Sub domain + hostname
            + r"(?:[a-zA-Z0-9-_]{0,61}[A-Za-z0-9])?\.)"
            # First 61 characters of the gTLD
            + r"+[A-Za-z0-9][A-Za-z0-9-_]{0,61}"
            # Last character of the gTLD
            + rf"[A-Za-z]{r'.$' if rfc_1034 else r'$'}",
            value.encode("idna").decode("utf-8"),
            re.IGNORECASE,
        )
    except UnicodeError:
        return False
