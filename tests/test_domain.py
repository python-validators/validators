"""Test Domain."""

# external
import pytest

# local
from validators import ValidationError, domain


@pytest.mark.parametrize(
    ("value", "rfc_1034", "rfc_2782"),
    [
        ("example.com", False, False),
        ("exa_mple.com", False, True),
        ("xn----gtbspbbmkef.xn--p1ai", False, False),
        ("underscore_subdomain.example.com", False, True),
        ("something.versicherung", False, False),
        ("someThing.versicherung.", True, False),
        ("11.com", False, False),
        ("3.cn.", True, False),
        ("_example.com", False, True),
        ("example_.com", False, True),
        ("_exa_mple_.com", False, True),
        ("a.cn", False, False),
        ("sub1.sub2.sample.co.uk", False, False),
        ("somerandomexample.xn--fiqs8s", False, False),
        ("kräuter.com.", True, False),
        ("über.com", False, False),
    ],
)
def test_returns_true_on_valid_domain(value: str, rfc_1034: bool, rfc_2782: bool):
    """Test returns true on valid domain."""
    assert domain(value, rfc_1034=rfc_1034, rfc_2782=rfc_2782)


@pytest.mark.parametrize(
    ("value", "consider_tld", "rfc_1034", "rfc_2782"),
    [
        ("example.com", True, False, False),
        ("exa_mple.com", True, False, True),
        ("xn----gtbspbbmkef.xn--p1ai", True, False, False),
        ("underscore_subdomain.example.com", True, False, True),
        ("someThing.versicherung.", True, True, False),
        ("11.com", True, False, False),
        ("3.cn.", True, True, False),
        ("_example.com", True, False, True),
        ("example_.com", True, False, True),
        ("somerandomexample.xn--fiqs8s", True, False, False),
        ("somerandomexample.onion", True, False, False),
    ],
)
def test_returns_true_on_valid_top_level_domain(
    value: str, consider_tld: bool, rfc_1034: bool, rfc_2782: bool
):
    """Test returns true on valid top level domain."""
    assert domain(value, consider_tld=consider_tld, rfc_1034=rfc_1034, rfc_2782=rfc_2782)


@pytest.mark.parametrize(
    ("value", "rfc_1034", "rfc_2782"),
    [
        ("example.com/.", True, False),
        ("example.com:4444", False, False),
        ("example.-com", False, False),
        ("example.", False, False),
        ("-example.com", False, False),
        ("example-.com.", True, False),
        ("_example.com", False, False),
        ("_example._com", False, False),
        ("example_.com", False, False),
        ("example", False, False),
        ("example.com!", True, False),
        ("example?.com", True, False),
        ("__exa__mple__.com", False, True),
        ("a......b.com", False, False),
        ("a.123", False, False),
        ("foo.ba_r", False, False),
        ("foo.ba_r", False, True),
        ("example.co_uk", False, False),
        ("123.123", False, False),
        ("123.123.123.", True, False),
        ("123.123.123.123", False, False),
    ],
)
def test_returns_failed_validation_on_invalid_domain(value: str, rfc_1034: bool, rfc_2782: bool):
    """Test returns failed validation on invalid domain."""
    assert isinstance(domain(value, rfc_1034=rfc_1034, rfc_2782=rfc_2782), ValidationError)


@pytest.mark.parametrize(
    ("value", "consider_tld", "rfc_1034", "rfc_2782"),
    [
        ("example.266", True, False, False),
        ("exa_mple.org_", True, False, True),
        ("xn----gtbspbbmkef.xn-p1ai", True, False, False),
        ("underscore_subdomain.example.flat", True, False, True),
        ("someThing.versicherung.reddit.", True, True, False),
        ("11.twitter", True, False, False),
        ("3.cnx.", True, True, False),
        ("_example.#13", True, False, True),
        ("example_.fo-ul", True, False, True),
        ("somerandomexample.xn-n-fiqs8s", True, False, False),
    ],
)
def test_returns_failed_validation_invalid_top_level_domain(
    value: str, consider_tld: bool, rfc_1034: bool, rfc_2782: bool
):
    """Test returns failed validation invalid top level domain."""
    assert isinstance(
        domain(value, consider_tld=consider_tld, rfc_1034=rfc_1034, rfc_2782=rfc_2782),
        ValidationError,
    )


def _name_of_length(length: int):
    """Build a dotted name of exactly `length` characters, ending with `.com`."""
    labels: list[str] = []
    remaining = length - len(".com")
    while remaining > 0:
        size = min(61, remaining)
        if remaining - size == 1:  # avoid leaving a lone "." behind
            size -= 1
        labels.append("a" * size)
        remaining -= size + 1
    name = ".".join(labels) + ".com"
    assert len(name) == length
    return name


@pytest.mark.parametrize(
    "value",
    [
        # total length: at most 253 characters (RFC 1035)
        _name_of_length(253),
        # label length: at most 63 characters (RFC 1035)
        "a" * 63 + ".com",
        # a label may start with a digit (RFC 1123)
        "1host.example.com",
        # the limit is in octets of the encoded name, not characters: 189 characters
        # here, but 225 octets once IDNA-encoded
        ".".join(["ü" * 30] * 6) + ".com",
    ],
)
def test_returns_true_on_domain_within_rfc_length_limits(value: str):
    """Test returns true on domain within RFC length limits."""
    assert domain(value)


@pytest.mark.parametrize(
    "value",
    [
        _name_of_length(254),
        _name_of_length(255),
        # many short, dot-separated labels that exceed 253 characters; see #413
        ".".join(["kld8MXQh6YalMqKRbfs895gMjW5T4p2EwToPoCSThPHHbXgmXc"] * 4)
        + ".kld8MXQh6YalMqKRbfs895gMjW5T4p2EwToPoCSThPHHbXgmXcab",
        "a" * 64 + ".com",
        # fewer than 253 characters (220), but 262 octets once IDNA-encoded
        ".".join(["ü" * 30] * 7) + ".com",
        # the example from #407 (261 characters)
        "www." + ".".join(["abcdefghijklmnop"] * 15) + ".fr",
        # a label must not start or end with a hyphen
        "-host.example.com",
        "host-.example.com",
    ],
)
def test_returns_failed_validation_on_domain_beyond_rfc_limits(value: str):
    """Test returns failed validation on domain beyond RFC limits."""
    assert isinstance(domain(value), ValidationError)
