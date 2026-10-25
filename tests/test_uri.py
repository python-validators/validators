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
        # urlsplit would silently strip these control characters
        "telnet://example.com\n",
        "telnet://exa\nmple.com",
        "telnet://example.com\t",
    ],
)
def test_invalid_telnet_uri(value: str):
    """Test invalid telnet URI."""
    assert not uri(value)


@pytest.mark.parametrize(
    "value",
    [
        "file:///tmp/readme.txt",
        "ipfs://QmYwAPJzv5CZsnAzt8auVZRnGiUncKEy6PBDoDeZ7hA9Rx/readme.txt",
        "magnet:?xt=urn:btih:0123456789012345678901234567890123456789",
        "tel:+1234567890",
        "data:text/plain;base64,SGVsbG8=",
        "urn:isbn:9780140328721",
        "urc:example",
    ],
)
@pytest.mark.parametrize("invalid_char", ["\x00", "\t", "\n", "\r", " ", "\x7f"])
def test_rejects_raw_ascii_controls_and_spaces_in_uri(value: str, invalid_char: str):
    """Test rejects raw ASCII controls and spaces in URI."""
    assert not uri(value + invalid_char)


@pytest.mark.parametrize(
    "value",
    [
        "file:///tmp/readme%20name.txt",
        "ipfs://QmYwAPJzv5CZsnAzt8auVZRnGiUncKEy6PBDoDeZ7hA9Rx/readme%0A.txt",
        "magnet:?xt=urn:btih:0123456789012345678901234567890123456789&dn=readme%20name",
        "data:text/plain,hello%20world",
    ],
)
def test_accepts_percent_encoded_characters_in_uri(value: str):
    """Test accepts percent encoded characters in URI."""
    assert uri(value)
