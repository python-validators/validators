"""eMail."""
# -*- coding: utf-8 -*-

# standard
import re

# local
from .utils import validator
from .domain import domain


@validator
def email(value: str, /):
    """Validate an email address.

    This was inspired from [Django's email validator][1].
    Also ref: [RFC 1034][2], [RFC 5321][3] and [RFC 5322][4].

    [1]: https://github.com/django/django/blob/main/django/core/validators.py#L174
    [2]: https://www.rfc-editor.org/rfc/rfc1034
    [3]: https://www.rfc-editor.org/rfc/rfc5321
    [4]: https://www.rfc-editor.org/rfc/rfc5322

    Examples:
        >>> email('someone@example.com')
        # Output: True
        >>> email('bogus@@')
        # Output: ValidationFailure(email=email, args={'value': 'bogus@@'})

    Args:
        value:
            eMail string to validate.

    Returns:
        (Literal[True]):
            If `value` is a valid eMail.
        (ValidationFailure):
            If `value` is an invalid eMail.

    > *New in version 0.1.0*.
    """
    if not value or value.count("@") != 1:
        return False

    username_part, domain_part = value.rsplit("@", 1)

    if len(username_part) > 64 or len(domain_part) > 253:
        # ref: RFC 1034 and 5231
        return False

    return (
        bool(domain(domain_part))
        if re.compile(
            # dot-atom
            r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*$"
            # quoted-string
            + r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*"$)',
            re.IGNORECASE,
        ).match(username_part)
        else False
    )
