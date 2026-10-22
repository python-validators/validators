"""Test eMail."""

# external
import pytest

# local
from validators import ValidationError, email


@pytest.mark.parametrize(
    ("value",),
    [
        ("email@here.com",),
        ("weirder-email@here.and.there.com",),
        ("email@127.local.home.arpa",),
        ("example@valid-----hyphens.com",),
        ("example@valid-with-hyphens.com",),
        ("test@domain.with.idn.tld.उदाहरण.परीक्षा",),
        ("email@localhost.in",),
        ("Łókaść@email.com",),
        ("łemłail@here.com",),
        ("email@localdomain.org",),
        ('"\\\011"@here.com',),
    ],
)
def test_returns_true_on_valid_email(value: str):
    """Test returns true on valid email."""
    assert email(value)


@pytest.mark.parametrize(
    ("value",),
    [
        (None,),
        ("",),
        ("abc",),
        ("abc@",),
        ("abc@bar",),
        ("a @x.cz",),
        ("abc@.com",),
        ("something@@somewhere.com",),
        ("email@127.0.0.1",),
        ("example@invalid-.com",),
        ("example@-invalid.com",),
        ("example@inv-.alid-.com",),
        ("example@inv-.-alid.com",),
        ("john56789.john56789.john56789.john56789.john56789.john56789.john5@example.com",),
        ('"test@test"@example.com',),
        # Quoted-string format (CR not allowed)
        ('"\\\012"@here.com',),
        # Non-quoted space/semicolon not allowed
        ("stephen smith@example.com",),
        ("stephen;smith@example.com",),
    ],
)
def test_returns_failed_validation_on_invalid_email(value: str):
    """Test returns failed validation on invalid email."""
    assert isinstance(email(value), ValidationError)


@pytest.mark.parametrize(
    "local_part", ["person", "person.name", "\u0141\u00f3ka\u015b\u0107", '"person"']
)
def test_rejects_newline_after_local_part(local_part: str):
    """Test the whole local part, including its final character."""
    # 2026-10-11: A newline before the at-sign is not part of a valid local part.
    assert email(f"{local_part}@example.com") is True
    assert isinstance(email(f"{local_part}\n@example.com"), ValidationError)


@pytest.mark.parametrize(
    "address",
    ["2001:db8::1", "2001:db8:0:0:0:0:0:1", "::ffff:192.0.2.1"],
)
def test_accepts_tagged_ipv6_literal(address: str):
    """Accept RFC 5321 address literals when IPv6 addresses are enabled."""
    assert email(f"user@[IPv6:{address}]", ipv6_address=True) is True
    assert email(f"user@[ipv6:{address}]", ipv6_address=True) is True
    assert isinstance(email(f"user@[IPv6:{address}]"), ValidationError)
    assert isinstance(email(f"user@[IPv6:{address}]", ipv4_address=True), ValidationError)


@pytest.mark.parametrize(
    "address", ["", "example.com", "192.0.2.1", "2001:db8::xyz", "fe80::1%eth0"]
)
def test_rejects_invalid_tagged_ipv6_literal(address: str):
    """An IPv6 tag must identify a valid IPv6 address, never a hostname or IPv4."""
    assert isinstance(email(f"user@[IPv6:{address}]", ipv6_address=True), ValidationError)
    assert isinstance(
        email(f"user@[IPv6:{address}]", ipv6_address=True, ipv4_address=True), ValidationError
    )


def test_rejects_extra_brackets_around_tagged_ipv6_literal():
    """Do not strip repeated brackets while interpreting an IPv6 tag."""
    assert isinstance(email("user@[[IPv6:2001:db8::1]]", ipv6_address=True), ValidationError)


def test_preserves_legacy_email_address_literals():
    """Keep bare IPv6 and IPv4 literal support compatible."""
    assert email("user@[2001:db8::1]", ipv6_address=True) is True
    assert email("user@[192.0.2.1]", ipv4_address=True) is True
    assert email("user@[IPv6:2001:db8::1]", ipv6_address=True, ipv4_address=True) is True
    assert isinstance(email("invalid local@[IPv6:2001:db8::1]", ipv6_address=True), ValidationError)
