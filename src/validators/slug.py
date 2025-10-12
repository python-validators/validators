"""Slug."""

# standard
import re

# local
from .utils import validator

_SLUG_REGEXP = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


@validator
def slug(value: str, /):
    """Validate whether or not given value is valid slug.

    Valid slug can contain only lowercase alphanumeric characters and hyphens.
    It starts and ends with these lowercase alphanumeric characters.

    Examples:
        >>> slug('my-slug-2134')
        True
        >>> slug('my.slug')
        ValidationError(func=slug, args={'value': 'my.slug'})

    Args:
        value: Slug string to validate.

    Returns:
        (Literal[True]): If `value` is a valid slug.
        (ValidationError): If `value` is an invalid slug.
    """
    return _SLUG_REGEXP.match(value) is not None
