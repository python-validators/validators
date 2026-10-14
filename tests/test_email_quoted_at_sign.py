"""HU-02: accept @ inside a quoted local part."""
import validators


def test_email_accepts_at_sign_inside_quoted_local_part():
    result = validators.email('"user@name"@example.com')
    assert result is True, repr(result)
