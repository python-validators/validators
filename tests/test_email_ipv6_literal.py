"""HU-02: accept the IPv6: prefix in an SMTP address literal."""
import validators


def test_email_accepts_ipv6_literal_with_prefix():
    result = validators.email(
        "usuario@[IPv6:2001:db8::1]", ipv6_address=True
    )
    assert result is True, repr(result)
