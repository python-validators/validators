"""TRX Address."""
# -*- coding: utf-8 -*-

# standard
from _sha256 import sha256
import re

# external
import base58

# local
from validators.utils import validator


def _validate_trx_checksum_address(addr: str):
    """Validate TRX type checksum address."""
    if len(addr) != 34:
        return False

    address = base58.b58decode(addr)
    if len(address) != 25:
        return False

    if address[0] != 0x41:
        return False

    check_sum = sha256(sha256(address[:-4]).digest()).digest()[:4]
    return True if address[-4:] == check_sum else False


@validator
def trx_address(value: str, /):
    """Return whether or not given value is a valid tron (trx) address.

    Full validation is implemented for TRC20 tron addresses.

    Examples:
        >>> trx_address('TLjfbTbpZYDQ4EoA4N5CLNgGjfbF8ZWz38')
        # Output: True
        >>> trx_address('TR2G7Rm4vFqF8EpY4U5xdLdQ7XgJ2U8Vd')
        # Output: ValidationFailure(func=trx_address, args=...)

    Args:
        value:
            Tron address string to validate.

    Returns:
        (Literal[True]):
            If `value` is a valid tron address.
        (ValidationFailure):
            If `value` is an invalid tron address.

    """
    if not value:
        return False

    return re.compile(r"^(T|41)[a-zA-Z0-9]{33}$").match(value) and _validate_trx_checksum_address(
        value
    )
