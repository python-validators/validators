"""HU-02: accept the IPv6: prefix in an SMTP address literal."""

# external
import pytest

import validators


@pytest.mark.parametrize(
    ("email",),
    [
        ("usuario@[IPv6:2001:db8::1]", ),
    ],
)
def test_email_accepts_ipv6_literal_with_prefix(email: str):
    """Email accepts ipv6 literal with prefix."""
    result = validators.email(
        email, ipv6_address=True
    )
    assert result is True, repr(result)
