"""Pure-Python Keccak-256 implementation — no external dependencies.

Used as fallback when ``eth-hash`` is not installed.
Compatible with Ethereum's EIP-55 address checksum (RFC Keccak-256,
which differs from NIST SHA3-256 only in the padding byte).
"""

from __future__ import annotations

_KeccakF_RoundConstants = [
    0x0000000000000001, 0x0000000000008082, 0x800000000000808A, 0x8000000080008000,
    0x000000000000808B, 0x0000000080000001, 0x8000000080008081, 0x8000000000008009,
    0x000000000000008A, 0x0000000000000088, 0x0000000080008009, 0x000000008000000A,
    0x000000008000808B, 0x800000000000008B, 0x8000000000008089, 0x8000000000008003,
    0x8000000000008002, 0x8000000000000080, 0x000000000000800A, 0x800000008000000A,
    0x8000000080008081, 0x8000000000008080, 0x0000000080000001, 0x8000000080008008,
]

_KeccakF_RotationConstants = [
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 2, 14,
    27, 41, 56, 8, 25, 43, 62, 18, 39, 61, 20, 44,
]

_KeccakF_PiLane = [
    10, 7, 11, 17, 18, 3, 5, 16, 8, 21, 24, 4,
    15, 23, 19, 13, 12, 2, 20, 14, 22, 9, 6, 1,
]

_MOD64 = (1 << 64) - 1


def _keccak_f(state: list[int]) -> list[int]:
    for rc in _KeccakF_RoundConstants:
        c = [state[x] ^ state[x + 5] ^ state[x + 10] ^ state[x + 15] ^ state[x + 20]
             for x in range(5)]
        d = [c[(x + 4) % 5] ^ ((c[(x + 1) % 5] << 1 | c[(x + 1) % 5] >> 63) & _MOD64)
             for x in range(5)]
        state = [state[x] ^ d[x % 5] for x in range(25)]
        b = [0] * 25
        b[0] = state[0]
        for x, (y, r) in enumerate(zip(_KeccakF_PiLane, _KeccakF_RotationConstants), 1):
            b[y] = ((state[x] << r | state[x] >> (64 - r)) & _MOD64)
        state = [b[x] ^ ((~b[(x + 1) % 5 + (x // 5) * 5]) & b[(x + 2) % 5 + (x // 5) * 5])
                 for x in range(25)]
        state[0] ^= rc
    return state


def keccak256(data: bytes) -> bytes:
    """Compute Keccak-256 (Ethereum variant) of *data*.

    This is NOT the same as NIST SHA3-256; the padding byte differs (0x01 vs 0x06).

    Args:
        data: Raw bytes to hash.

    Returns:
        32-byte digest.
    """
    rate_bytes = 136  # Keccak-256: 1600 - 2*256 = 1088 bits = 136 bytes
    data = bytearray(data)

    # Padding: Keccak uses 0x01 ... 0x80 (not SHA3's 0x06)
    data += b"\x01"
    data += b"\x00" * (rate_bytes - len(data) % rate_bytes)
    data[-1] |= 0x80

    state: list[int] = [0] * 25
    for i in range(0, len(data), rate_bytes):
        block = data[i:i + rate_bytes]
        for j in range(rate_bytes // 8):
            state[j] ^= int.from_bytes(block[j * 8:(j + 1) * 8], "little")
        state = _keccak_f(state)

    digest = bytearray()
    for word in state[:4]:
        digest += word.to_bytes(8, "little")
    return bytes(digest)
