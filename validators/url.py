import re

from .utils import validator

regex = (r'^(http(s)?://)?(www\.)?((\w|-)+)(\.(\w|-)+)+(:\d*)?(/(\w|-|\&|\=|\#)*)*')

pattern = re.compile(regex)


@validator
def url(value):
    """
    Return whether or not given value is a valid URL.

    If the value is valid URL this function returns ``True``, otherwise
    :class:`~validators.utils.ValidationFailure`.

    This validator is based on `WTForms URL validator`_.

    .. _WTForms URL validator:
       https://github.com/wtforms/wtforms/blob/master/wtforms/validators.py

    Examples::

        >>> url('http://foobar.dk')
        True

        >>> url('http://foobar.d')
        ValidationFailure(func=url, ...)

    .. versionadded:: 0.2

    :param value: URL address string to validate
    """

    return pattern.match(value)
