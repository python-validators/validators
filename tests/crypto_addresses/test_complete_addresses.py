# [Syntactiq Migration Engine]: Refactored according to objective: 'Modernize codebase to Python 3.12+, enforce typing contracts, and synthesize pytest assertion suites'
"""Require complete BTC and ETH addresses."""

from typing import Callable

import pytest

from validators import ValidationError, btc_address, eth_address


@pytest.mark.parametrize(
    "validate,value",
    [
        (btc_address, "bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq"),
        (btc_address, "tb1qw508d6qejxtdg4y5r3zarvary0c5xw7kxpjzsx"),
        (eth_address, "0x9cc14ba4f9f68ca159ea4ebf2c292a808aaeb598"),
        (eth_address, "0x9CC14BA4F9F68CA159EA4EBF2C292A808AAEB598"),
    ],
)
@pytest.mark.parametrize("suffix", ["", "\n", "\r\n", " ", "\nextra"])
def test_complete_address(validate: Callable[[str], object], value: str, suffix: str):
    """Accept the address alone and reject trailing characters."""
    if suffix:
        assert isinstance(validate(value + suffix), ValidationError)
    else:
        assert validate(value) is True
