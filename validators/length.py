from .range import range
from .utils import validator


@validator
def length(value, min=None, max=None):
    """
    Returns whether or not the length of given string is within a specified
    range.

    Examples::


        >>> assert length('something', min=2)

        >>> assert length('something', min=9, max=9)

        >>> assert not length('something', max=5)


    :param value:
        The string to validate.
    :param min:
        The minimum required length of the string. If not provided, minimum
        length will not be checked.
    :param max:
        The maximum length of the string. If not provided, maximum length
        will not be checked.

    .. versionadded:: 0.2
    """
    if (min is not None and min < 0) or (max is not None and max < 0):
        raise AssertionError(
            '`min` and `max` need to be greater than zero.'
        )
    return range(len(value), min=min, max=max)
