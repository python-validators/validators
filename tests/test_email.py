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
