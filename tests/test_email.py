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


@pytest.mark.parametrize("domain_part", ["example.\uff43\uff4f\uff4d", "exam\u00adple.com"])
def test_returns_failed_validation_on_idna_mapped_lookalike_domain(domain_part: str):
    """Test returns failed validation on email domains that only IDNA 2003 mapping makes valid."""
    assert isinstance(email(f"user@{domain_part}"), ValidationError)


@pytest.mark.parametrize(
    ("value", "ipv6_address", "ipv4_address"),
    [
        ("user@[192.0.2.1]", False, True),
        ("user@[2001:db8::1]", True, False),
    ],
)
def test_returns_true_on_address_literal(value: str, ipv6_address: bool, ipv4_address: bool):
    """Test returns true on an email whose domain is a bracketed IP address."""
    assert email(value, ipv6_address=ipv6_address, ipv4_address=ipv4_address)


@pytest.mark.parametrize(
    "value",
    [
        "user@[[192.0.2.1]]",
        "user@[192.0.2.1]]",
        "user@[[192.0.2.1]",
        "user@[[2001:db8::1]]",
        "user@[[[2001:db8::1]]]",
        "user@[2001:db8::1]]",
        "user@[2001:db8::1%]]",
        "user@[]",
    ],
)
def test_returns_failed_validation_on_address_literal_with_extra_brackets(value: str):
    """Test returns failed validation on an address literal with more than one pair of brackets."""
    assert isinstance(email(value, ipv6_address=True, ipv4_address=True), ValidationError)
