"""HU-04: require a prefix length in the documented strict CIDR mode."""

# external
import pytest

import validators


@pytest.mark.parametrize(
    ("ip",),
    [
        ("192.168.1.0/255.255.255.0", ),
    ],
)
def test_ipv4_strict_cidr_rejects_dotted_netmask(ip: str):
    """The network is valid, but its representation is not CIDR prefix notation."""
    result = validators.ipv4(ip, strict=True)
    assert isinstance(result, validators.ValidationError), repr(result)
