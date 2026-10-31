# [Syntactiq Migration Engine]: Refactored according to objective: 'Modernize codebase to Python 3.12+, enforce typing contracts, and synthesize pytest assertion suites'
from typing import Any, Dict, List, Optional, Union

"""Crypto addresses."""

# local
from .bsc_address import bsc_address
from .btc_address import btc_address
from .eth_address import eth_address
from .trx_address import trx_address

__all__ = ("bsc_address", "btc_address", "eth_address", "trx_address")
