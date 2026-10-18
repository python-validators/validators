"""HU-04: proposed enhancement; brackets are URL host syntax.

This test expresses a new requirement, not a defect in the current contract.
"""

# external
import pytest

import validators


@pytest.mark.parametrize(
    ("ip",),
    [
        ("[2001:db8::1]", ),
    ],
)
def test_ipv6_accepts_address_in_brackets(ip: str):
    """Accept iv6 address in brackets."""
    result = validators.ipv6(ip)
    assert result is True, repr(result)
