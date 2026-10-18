"""HU-02: accept @ inside a quoted local part."""

# external
import pytest

import validators


@pytest.mark.parametrize(
    ("email",),
    [
        ('"user@name"@example.com', ),
    ],
)
def test_email_accepts_at_sign_inside_quoted_local_part(email: str):
    """The email accepts at sign inside quoted local part character."""
    result = validators.email(email)
    assert result is True, repr(result)
