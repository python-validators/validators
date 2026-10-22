"""Test Hostname."""

# external
import pytest

# local
from validators import ValidationError, hostname


@pytest.mark.parametrize(
    ("value", "rfc_1034", "rfc_2782"),
    [
        # simple hostname w/ optional ports
        ("ubuntu-pc:443", False, False),
        ("this-pc", False, False),
        ("lab-01a-notebook:404", False, False),
        ("4-oh-4", False, False),
        # simple, single-label hostname w/ trailing dot (RFC 1034); see #442
        ("this-pc.", True, False),
        ("ie.", True, False),
        # hostname w/ optional ports
        ("example.com:4444", False, False),
        ("kräuter.com.", True, False),
        ("xn----gtbspbbmkef.xn--p1ai:65535", False, False),
        ("_example.com", False, True),
        # ipv4 addr w/ optional ports
        ("123.123.123.123:9090", False, False),
        ("127.0.0.1:43512", False, False),
        ("123.5.77.88:31000", False, False),
        ("12.12.12.12:5353", False, False),
        # ipv6 addr w/ optional ports
        ("[::1]:22", False, False),
        ("[dead:beef:0:0:0:0000:42:1]:5731", False, False),
        ("[0:0:0:0:0:ffff:1.2.3.4]:80", False, False),
        ("[0:a:b:c:d:e:f::]:53", False, False),
    ],
)
def test_returns_true_on_valid_hostname(value: str, rfc_1034: bool, rfc_2782: bool):
    """Test returns true on valid hostname."""
    assert hostname(value, rfc_1034=rfc_1034, rfc_2782=rfc_2782)


@pytest.mark.parametrize(
    ("value", "rfc_1034", "rfc_2782"),
    [
        # bad (simple hostname w/ optional ports)
        ("ubuntu-pc:443080", False, False),
        ("this-pc-is-sh*t", False, False),
        ("lab-01a-note._com_.com:404", False, False),
        ("4-oh-4:@.com", False, False),
        # trailing dot is only allowed with rfc_1034; see #442
        ("this-pc.", False, False),
        # bad (hostname w/ optional ports)
        ("example.com:-4444", False, False),
        ("xn----gtbspbbmkef.xn--p1ai:65538", False, False),
        ("_example.com:0", False, True),
        ("kräuter.com.:81_00", True, False),
        # bad (ipv4 addr w/ optional ports)
        ("123.123.123.123:99999", False, False),
        ("127.0.0.1:", False, False),
        ("123.5.-12.88:8080", False, False),
        ("12.12.12.12:$#", False, False),
        # bad (ipv6 addr w/ optional ports)
        ("[::1]:[22]", False, False),
        ("[dead:beef:0:-:0:-:42:1]:5731", False, False),
        ("[0:0:0:0:0:ffff:1.2.3.4]:-65538", False, False),
        ("[0:&:b:c:@:e:f:::9999", False, False),
    ],
)
def test_returns_failed_validation_on_invalid_hostname(value: str, rfc_1034: bool, rfc_2782: bool):
    """Test returns failed validation on invalid hostname."""
    assert isinstance(hostname(value, rfc_1034=rfc_1034, rfc_2782=rfc_2782), ValidationError)


@pytest.mark.parametrize(
    "value",
    [
        # total length: at most 253 characters (RFC 1035)
        ".".join(["a" * 63, "a" * 63, "a" * 63, "a" * 61]),
        # label length: at most 63 characters (RFC 1035)
        "a" * 63 + ".com",
        # a label may start with a digit (RFC 1123)
        "1host.example.com",
        # the limit is in octets of the encoded name, not characters
        ".".join(["ü" * 30] * 6) + ".com",
    ],
)
def test_returns_true_on_hostname_within_rfc_length_limits(value: str):
    """Test returns true on hostname within RFC length limits."""
    assert hostname(value)


@pytest.mark.parametrize(
    "value",
    [
        # many short, dot-separated labels that exceed 253 characters; see #413
        ".".join(["kld8MXQh6YalMqKRbfs895gMjW5T4p2EwToPoCSThPHHbXgmXc"] * 4)
        + ".kld8MXQh6YalMqKRbfs895gMjW5T4p2EwToPoCSThPHHbXgmXcab",
        ".".join(["a" * 63, "a" * 63, "a" * 63, "a" * 62]),
        "a" * 64 + ".com",
        # fewer than 253 characters (220), but 262 octets once IDNA-encoded
        ".".join(["ü" * 30] * 7) + ".com",
        # a label must not start or end with a hyphen, nor contain an underscore
        "-host.example.com",
        "host-.example.com",
        "ho_st.example.com",
    ],
)
def test_returns_failed_validation_on_hostname_beyond_rfc_limits(value: str):
    """Test returns failed validation on hostname beyond RFC limits."""
    assert isinstance(hostname(value), ValidationError)


@pytest.mark.parametrize(
    "value",
    [
        "ubuntu-pc\n",
        "ubuntu-pc:443\n",
        "example.com:443\n",
        "127.0.0.1:22\n",
        "[::1]:22\n",
        "[dead:beef:0:0:0:0000:42:1]:5731\n",
    ],
)
def test_rejects_trailing_newline_in_hostnames_and_ports(value: str):
    """Test rejects trailing newline in hostnames and ports."""
    assert isinstance(hostname(value), ValidationError)


@pytest.mark.parametrize(
    "value", ["\u017ferver", "\u212aelvin", "\u0131ntranet", "\u0130ntranet:8080"]
)
def test_returns_failed_validation_on_non_ascii_simple_hostname(value: str):
    """Test returns failed validation on non-ASCII case equivalents in simple hostnames."""
    assert isinstance(hostname(value), ValidationError)


@pytest.mark.parametrize("value", ["example.\uff43\uff4f\uff4d", "exam\u00adple.com:443"])
def test_returns_failed_validation_on_idna_mapped_lookalike_hostname(value: str):
    """Test returns failed validation on hostnames that only IDNA 2003 mapping makes valid."""
    assert isinstance(hostname(value), ValidationError)


@pytest.mark.parametrize("value", ["10.0.0.\u0661", "123.5.77.\u06688:31000"])
def test_returns_failed_validation_on_ipv4_lookalike_hostname(value: str):
    """Test returns failed validation on dotted names whose last label is non-ASCII digits."""
    assert isinstance(hostname(value), ValidationError)


@pytest.mark.parametrize(
    "value",
    [
        "example.com:443",
        "xn--e1afmkfd.xn--p1ai",
        "пример.рф",
        "пример.рф:8080",
    ],
)
def test_returns_true_on_valid_top_level_domain_hostname(value: str):
    """Test returns true on hostname with a TLD allowed by IANA."""
    assert hostname(value, consider_tld=True)


@pytest.mark.parametrize(
    "value",
    [
        "example.flat:443",
        "пример.рфы",
    ],
)
def test_returns_failed_validation_on_invalid_top_level_domain_hostname(value: str):
    """Test returns failed validation on hostname with a TLD not allowed by IANA."""
    assert isinstance(hostname(value, consider_tld=True), ValidationError)
