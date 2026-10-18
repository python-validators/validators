"""HU-02: reject ASCII control characters in quoted SMTP local parts."""

# external
import pytest

import validators


@pytest.mark.parametrize(
    "control_code",
        [1, 2, 7, 11, 12, 14, 27, 31, 127],
)

def test_email_rejects_control_characters(control_code: int):
    """Reject selected ASCII control characters in quoted local parts."""
    email = f'"user{chr(control_code)}name"@example.com'

    result = validators.email(email)

    assert isinstance(result, validators.ValidationError), repr(result)