"""HU-02: reject SOH in an address intended for SMTP (RFC 5321)."""

# external
import pytest

import validators


@pytest.mark.parametrize(
    ("email",),
    [
        ('"user\x01name"@example.com', ),
    ],
)
def test_email_rejects_soh_control_character(email: str):
    """The Python escape introduces the actual ASCII SOH character."""
    result = validators.email(email)
    assert isinstance(result, validators.ValidationError), repr(result)
