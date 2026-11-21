"""BTC Address."""

# standard
from hashlib import sha256
import re

# local
from validators.utils import validator


def _decode_base58(addr: str):
    """Decode base58."""
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    return sum((58**enm) * alphabet.index(idx) for enm, idx in enumerate(addr[::-1]))


def _validate_old_btc_address(addr: str):
    """Validate P2PKH and P2SH type address."""
    if not re.fullmatch(
        r"1[1-9A-HJ-NP-Za-km-z]{24,33}"
        r"|[3mn][1-9A-HJ-NP-Za-km-z]{33}"
        r"|2[1-9A-HJ-NP-Za-km-z]{34}",
        addr,
    ):
        return False
    try:
        decoded_bytes = _decode_base58(addr).to_bytes(25, "big")
    except OverflowError:
        return False
    header, checksum = decoded_bytes[:-4], decoded_bytes[-4:]
    if header[0] not in {0x00, 0x05, 0x6F, 0xC4}:
        return False
    return checksum == sha256(sha256(header).digest()).digest()[:4]


@validator
def btc_address(value: str, /):
    """Return whether or not given value is a valid bitcoin address.

    Full validation is implemented for P2PKH and P2SH addresses.
    For segwit addresses a regexp is used to provide a reasonable
    estimate on whether the address is valid.

    Examples:
        >>> btc_address('3Cwgr2g7vsi1bXDUkpEnVoRLA9w4FZfC69')
        True
        >>> btc_address('1BvBMsEYstWetqTFn5Au4m4GFg7xJaNVN2')
        ValidationError(func=btc_address, args={'value': '1BvBMsEYstWetqTFn5Au4m4GFg7xJaNVN2'})

    Args:
        value:
            Bitcoin address string to validate.

    Returns:
        (Literal[True]): If `value` is a valid bitcoin address.
        (ValidationError): If `value` is an invalid bitcoin address.
    """
    if not value:
        return False

    return (
        # segwit pattern (BIP-173 / BIP-350)
        re.fullmatch(
            r"(bc|tb)1(?:q(?:[02-9ac-hj-np-z]{38}|[02-9ac-hj-np-z]{58})"
            r"|[pzry9x8gf2tvdw0s][02-9ac-hj-np-z]{10,70})",
            value,
        )
        if value[:2] in ("bc", "tb")
        else _validate_old_btc_address(value)
    )
