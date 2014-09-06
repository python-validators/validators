import re
from .utils import validator


slug_regex = re.compile(r'^[-a-zA-Z0-9_]+$')


@validator
def slug(value):
    """
    Validate whether or not given value is valid slug.

    Valid slug can contain only alphanumeric characters, hyphens and
    underscores.

    Examples::

        >>> assert not slug('my.slug')

        >>> assert slug('my-slug-2134')

    .. versionadded:: 0.6

    :param value: value to validate
    """
    return slug_regex.match(value)
