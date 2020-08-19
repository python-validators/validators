import re

from .utils import validator

SegWit_expression = r"\bbc(0([ac-hj-np-z02-9]{39}|[ac-hj-np-z02-9]{59})"
SegWit_expression += r"|1[ac-hj-np-z02-9]{8,87})\b$"

patterns = {
    "P2PKH": re.compile(r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$"),
    "SegWit": re.compile(SegWit_expression),
}


@validator
def btc_address(value):
    """
    Return whether or not given value is a valid bitcoin address.

    If the value is valid bitcoin address this function returns ``True``,
    otherwise :class:`~validators.utils.ValidationFailure`.

    Examples::

        >>> btc_address('3Cwgr2g7vsi1bXDUkpEnVoRLA9w4FZfC69')
        True

    :param value: Bitcoin address string to validate
    """
    response = False
    for _, pattern in patterns.items():
        if pattern.match(value):
            response = True

    return response
