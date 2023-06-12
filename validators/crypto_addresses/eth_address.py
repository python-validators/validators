"""ETH Address."""
# -*- coding: utf-8 -*-

# standard
import re

from sha3 import keccak_256

# local
from validators.utils import validator


def _validate_eth_checksum_address(addr: str):
    """Validate ETH type checksum address."""
    addr = addr.replace("0x", "")
    addr_hash = keccak_256(addr.lower().encode("ascii")).hexdigest()

    for i in range(0, 40):
        if ((int(addr_hash[i], 16) > 7 and addr[i].upper() != addr[i]) or
                (int(addr_hash[i], 16) <= 7 and addr[i].lower() != addr[i])):
            return False
    return True


@validator
def eth_address(value: str, /):
    """Return whether or not given value is a valid ethereum address.

    Full validation is implemented for ERC20 addresses.

    Examples:
        >>> eth_address('0x9cc14ba4f9f68ca159ea4ebf2c292a808aaeb598')
        # Output: True
        >>> eth_address('0x8Ba1f109551bD432803012645Ac136ddd64DBa72')
        # Output: ValidationFailure(func=eth_address, args=...)

    Args:
        value:
            Ethereum address string to validate.

    Returns:
        (Literal[True]):
            If `value` is a valid ethereum address.
        (ValidationFailure):
            If `value` is an invalid ethereum address.

    """
    if not value:
        return False

    return (
        re.compile(r"^0x[0-9a-f]{40}$").match(value) or
        re.compile(r"^0x[0-9A-F]{40}$").match(value) or
        _validate_eth_checksum_address(value)
    )
