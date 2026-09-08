"""UUID."""

# standard
import re
from typing import Union
from uuid import UUID

# local
from .utils import validator


@validator
def uuid(value: Union[str, UUID], /):
    """Return whether or not given value is a valid UUID-v4 string.

    This validator is based on [WTForms UUID validator][1].

    [1]: https://github.com/wtforms/wtforms/blob/master/src/wtforms/validators.py#L539

    Examples:
        >>> uuid('2bc1c94f-0deb-43e9-92a1-4775189ec9f8')
        True
        >>> uuid('2bc1c94f 0deb-43e9-92a1-4775189ec9f8')
        ValidationError(func=uuid, args={'value': '2bc1c94f 0deb-43e9-92a1-4775189ec9f8'})

    Args:
        value:
            UUID string or object to validate.

    Returns:
        (Literal[True]): If `value` is a valid UUID.
        (ValidationError): If `value` is an invalid UUID.
    """
    if not value:
        return False
    if isinstance(value, UUID):
        return True
    # Deliberately not delegating to the stdlib UUID() constructor here:
    # it accepts far more than this validator documents or tests, e.g.
    # `urn:uuid:...`-prefixed and `{braced}` forms, and any UUID version
    # (not just v4). A regex keeps acceptance limited to the plain
    # (optionally dashed) hex form shown in the docstring and tests.
    return bool(re.match(r"^[0-9a-fA-F]{8}-?([0-9a-fA-F]{4}-?){3}[0-9a-fA-F]{12}$", value))
