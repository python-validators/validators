import re
from .utils import validator


pattern = re.compile(r'^[0-9]{7}-[0-9]$')


@validator
def finnish_business_id(business_id):
    """
    Validates a Finnish Business ID. Each company in Finland has a distinct
    business id. For more information see `Finnish Trade Register`_

    .. _Finnish Trade Register:
        http://en.wikipedia.org/wiki/Finnish_Trade_Register

    ::

        >>> assert finnish_business_id('0112038-9')  # Fast Monkeys Ltd

        >>> assert not finnish_business_id('1234567-8')  # Bogus ID

    .. versionadded:: 0.4

    :param business_id: business_id to validate
    """
    if not business_id or not re.match(pattern, business_id):
        return False
    factors = [7, 9, 10, 5, 8, 4, 2]
    numbers = map(int, business_id[:7])
    checksum = int(business_id[8])
    sum_ = sum(f * n for f, n in zip(factors, numbers))
    modulo = sum_ % 11
    return (11 - modulo == checksum) or (modulo == 0 and checksum == 0)
