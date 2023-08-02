"""Length."""

# local
from .between import between
from .utils import validator


@validator
def length(value: str, /, *, min_val: int = 0, max_val: int = 0):
    """Return whether or not the length of given string is within a specified range.

    Examples:
        >>> length('something', min_val=2)
        # Output: True
        >>> length('something', min_val=9, max_val=9)
        # Output: True
        >>> length('something', max_val=5)
        # Output: ValidationError(func=length, ...)

    Args:
        value:
            The string to validate.
        min_val:
            The minimum required length of the string. If not provided,
            minimum length will not be checked.
        max_val:
            The maximum length of the string. If not provided,
            maximum length will not be checked.

    Returns:
        (Literal[True]):
            If `len(value)` is in between the given conditions.
        (ValidationError):
            If `len(value)` is not in between the given conditions.

    > *New in version 0.2.0*.
    """
    return between(len(value), min_val=min_val, max_val=max_val) if value else False
