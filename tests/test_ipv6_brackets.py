"""HU-04: proposed enhancement; brackets are URL host syntax.

This test expresses a new requirement, not a defect in the current contract.
"""
import validators


def test_ipv6_accepts_address_in_brackets():
    result = validators.ipv6("[2001:db8::1]")
    assert result is True, repr(result)
