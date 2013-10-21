import re
from .utils import validator


pattern = re.compile(r'^[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}$')


@validator
def uuid(value):
    """
    Returns whether or not given value is a valid uuid. If the value is valid
    uuid this function returns True, otherwise `FailedValidation`.

    Examples::

        >>> import validators

        >>> validators.uuid('2bc1c94f-0deb-43e9-92a1-4775189ec9f8')
        True
        >>> validators.uuid('2bc1c94f 0deb-43e9-92a1-4775189ec9f8')
        False

    .. versionadded:: 0.2

    :param value: UUID string to validate
    """
    return pattern.match(value)
