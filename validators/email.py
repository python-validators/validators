import re

from .utils import validator

user_regex = re.compile(
    # dot-atom
    r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+"
    r"(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*$"
    # quoted-string
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|'
    r"""\\[\001-\011\013\014\016-\177])*"$)""",
    re.IGNORECASE
)
domain_regex = re.compile(
    # domain
    r'(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+'
    r'(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?$)'
    # literal form, ipv4 address (SMTP 4.1.3)
    r'|^\[(25[0-5]|2[0-4]\d|[0-1]?\d?\d)'
    r'(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\]$',
    re.IGNORECASE)
domain_whitelist = ['localhost']


@validator
def email(value, whitelist=None, only_whitelist=False):
    """
    Validate an email address.

    This validator is based on `Django's email validator`_. Returns
    ``True`` on success and :class:`~validators.utils.ValidationFailure`
    when validation fails.

    Examples::

        >>> email('someone@example.com')
        True

        >>> email('bogus@@')
        ValidationFailure(func=email, ...)

    .. _Django's email validator:
       https://github.com/django/django/blob/master/django/core/validators.py

    .. versionadded:: 0.1

    :param value: value to validate
    :param whitelist: domain names to whitelist
    :param only_whitelist: specify whether to fail non whitelisted domains

    :copyright: (c) Django Software Foundation and individual contributors.
    :license: BSD
    """
    if not value or '@' not in value:
        return False

    if whitelist is None:
        whitelist = domain_whitelist

    user_part, domain_part = value.rsplit('@', 1)

    if not user_regex.match(user_part):
        return False

    # skip domain regex check if user specified it explicitly in whitelist
    if only_whitelist:
        return domain_part in whitelist

    # check if domain is good
    if not (domain_regex.match(domain_part) or domain_part in whitelist):
        # Try for possible IDN domain-part
        try:
            domain_part = domain_part.encode('idna').decode('ascii')
            return domain_regex.match(domain_part)
        except UnicodeError:
            return False

    # No whitelist and email passes user_regex and domain passes domain_regex.
    return True
