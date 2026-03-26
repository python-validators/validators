"""ETH Address."""

# standard
import re

# local
from validators.utils import validator

# Try providers in order: eth-hash (fast, C ext) → pycryptodome → unavailable
_keccak_fn = None

try:
    from eth_hash.auto import keccak as _eth_keccak  # type: ignore

    def _keccak_fn(data: bytes) -> bytes:  # type: ignore[no-redef]
        return _eth_keccak.new(data).digest()

except ImportError:
    pass

if _keccak_fn is None:
    try:
        from Crypto.Hash import keccak as _pycrypto_keccak  # type: ignore

        def _keccak_fn(data: bytes) -> bytes:  # type: ignore[no-redef]
            k = _pycrypto_keccak.new(digest_bits=256)
            k.update(data)
            return k.digest()

    except ImportError:
        pass

_keccak_available = _keccak_fn is not None

_RE_ALL_LOWER = re.compile(r"^0x[0-9a-f]{40}$")
_RE_ALL_UPPER = re.compile(r"^0x[0-9A-F]{40}$")
_RE_ETH_ADDR  = re.compile(r"^0x[0-9a-fA-F]{40}$")


def _validate_eth_checksum_address(addr: str) -> bool:
    """Validate EIP-55 mixed-case checksum address."""
    addr_stripped = addr[2:]  # remove 0x
    addr_hash = _keccak_fn(addr_stripped.lower().encode("ascii")).hex()  # type: ignore[misc]
    return all(
        (int(addr_hash[i], 16) > 7 and addr_stripped[i].upper() == addr_stripped[i])
        or (int(addr_hash[i], 16) <= 7 and addr_stripped[i].lower() == addr_stripped[i])
        for i in range(40)
    )


@validator
def eth_address(value: str, /):
    """Return whether or not given value is a valid ethereum address.

    Validates ERC-20 / EIP-55 addresses. Three address forms are accepted:

    * **All-lowercase** ``0x`` + 40 hex chars — valid without checksum.
    * **All-uppercase** ``0X`` + 40 hex chars — valid without checksum.
    * **Mixed-case** (EIP-55 checksum) — requires ``eth-hash`` or
      ``pycryptodome`` to verify the Keccak-256 checksum.  If neither
      is available the address is rejected to avoid accepting corrupt
      checksums silently.

    Examples:
        >>> eth_address('0x9cc14ba4f9f68ca159ea4ebf2c292a808aaeb598')
        True
        >>> eth_address('0x8Ba1f109551bD432803012645Ac136ddd64DBa72')
        ValidationError(func=eth_address, args={'value': '0x8Ba1f109551bD432803012645Ac136ddd64DBa72'})

    Args:
        value:
            Ethereum address string to validate.

    Returns:
        (Literal[True]): If ``value`` is a valid ethereum address.
        (ValidationError): If ``value`` is an invalid ethereum address.

    Note:
        For full mixed-case checksum validation install either
        ``pip install validators[crypto-eth-addresses]``
        or ``pip install pycryptodome``.
    """
    if not value:
        return False

    if not _RE_ETH_ADDR.match(value):
        return False

    # Pure-lowercase or pure-uppercase: structurally valid, no checksum needed
    if _RE_ALL_LOWER.match(value) or _RE_ALL_UPPER.match(value):
        return True

    # Mixed-case requires EIP-55 checksum verification
    if not _keccak_available:
        # Cannot verify checksum — reject to avoid silently accepting bad checksums
        return False

    return _validate_eth_checksum_address(value)
