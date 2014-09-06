import six
from .utils import validator


@validator
def truthy(value):
    """
    Validate that given value is not a falsey value.

    This validator is based on `WTForms DataRequired validator`_.

    .. _WTForms DataRequired validator:
       https://github.com/wtforms/wtforms/blob/master/wtforms/validators.py

    Examples::

        >>> assert truthy(1)

        >>> assert truthy('someone')

        >>> assert not truthy(0)

        >>> assert not truthy('    ')

        >>> assert not truthy(False)

        >>> assert not truthy(None)

    .. versionadded:: 0.2
    """
    return (
        not value or
        isinstance(value, six.string_types) and not value.strip()
    )
