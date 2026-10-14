"""HU-02: reject SOH in an address intended for SMTP (RFC 5321)."""
import validators


def test_email_rejects_soh_control_character():
    # The Python escape introduces the actual ASCII SOH character.
    email = '"user\x01name"@example.com'
    result = validators.email(email)
    assert isinstance(result, validators.ValidationError), repr(result)
