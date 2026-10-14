"""HU-04: require a prefix length in the documented strict CIDR mode."""
import validators


def test_ipv4_strict_cidr_rejects_dotted_netmask():
    # The network is valid, but its representation is not CIDR prefix notation.
    result = validators.ipv4("192.168.1.0/255.255.255.0", strict=True)
    assert isinstance(result, validators.ValidationError), repr(result)
