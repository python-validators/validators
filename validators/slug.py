import re
from .utils import validator


slug_regex = re.compile(r'^[-a-zA-Z0-9_]+$')


@validator
def slug(value):
    """
    Validates whether or not given value is valid slug (contains only
    alphanumeric characters, hyphens or underscores).

    Examples::

        >>> assert not slug('my.slug')

        >>> assert slug('my-slug-2134')

    .. versionadded:: 0.6

    :param value: value to validate
    """
    return slug_regex.match(value)
