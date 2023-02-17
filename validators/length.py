"""Length."""
# -*- coding: utf-8 -*-

# project
from .between import between
from .utils import validator


@validator
def length(value: str, /, *, min_val: int = 0, max_val: int = 0):
    """Return whether or not the length of given string is within a specified range.

    Examples::

        >>> length('something', min_val=2)
        # Output: True

        >>> length('something', min_val=9, max_val=9)
        # Output: True

        >>> length('something', max_val=5)
        # Output: ValidationFailure(func=length, ...)

    Args:
        `value`:
            [Required] The string to validate.
        `min_val`:
            [Optional] The minimum required length of the string. If not provided,
            minimum length will not be checked.
        `max_val`:
            [Optional] The maximum length of the string. If not provided,
            maximum length will not be checked.
        Either one of `min_val` or `max_val` must be provided.

    Returns:
        A `boolean` if `value` is greater than `min_val` and
        less than `max_val`.

    .. versionadded:: 0.2
    """
    return between(len(value), min_val=min_val, max_val=max_val)
