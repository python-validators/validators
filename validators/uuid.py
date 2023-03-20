"""UUID."""
# -*- coding: utf-8 -*-

# standard
from typing import Union
from uuid import UUID
import re

# local
from .utils import validator


@validator
def uuid(value: Union[str, UUID], /):
    """Return whether or not given value is a valid UUID-v4 string.

    This validator is based on [WTForms UUID validator][1].

    [1]: https://github.com/wtforms/wtforms/blob/master/src/wtforms/validators.py#L539

    Examples:
        >>> uuid('2bc1c94f-0deb-43e9-92a1-4775189ec9f8')
        # Output: True
        >>> uuid('2bc1c94f 0deb-43e9-92a1-4775189ec9f8')
        # Output: ValidationFailure(func=uuid, ...)

    Args:
        value:
            UUID string or object to validate.

    Returns:
        (Literal[True]):
            If `value` is a valid UUID.
        (ValidationFailure):
            If `value` is an invalid UUID.

    > *New in version 0.2.0*.
    """
    if not value:
        return False
    if isinstance(value, UUID):
        return True
    try:
        return UUID(value) or re.match(
            r"^[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}$", value
        )
    except ValueError:
        return False
