"""Test URI."""

# external
import pytest

# local
from validators.uri import uri


@pytest.mark.parametrize(
    "value",
    [
        "telnet://example.com",
        "telnet://example.com/",
        "telnet://example.com:23",
        "telnet://example.com:23/",
        "telnet://192.168.1.1",
        "telnet://192.168.1.1:23",
        "telnet://user:password@example.com",
        "telnet://user:password@example.com:23/",
    ],
)
def test_valid_telnet_uri(value: str):
    """Test valid telnet URI."""
    assert uri(value)


@pytest.mark.parametrize(
    "value",
    [
        "telnet://",
        "telnet://example.com/path",
        "telnet://example.com?query=1",
        "telnet://example.com#frag",
    ],
)
def test_invalid_telnet_uri(value: str):
    """Test invalid telnet URI."""
    assert not uri(value)
