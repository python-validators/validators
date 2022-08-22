import re

from utils import validator

aadhar_card_regex = re.compile( ("^[2-9]{1}[0-9]{3}\\" +
             "s[0-9]{4}\\s[0-9]{4}$"))
pan_card_regex = re.compile("[A-Za-z]{5}\d{4}[A-Za-z]{1}")

@validator
def aadhar_card(value):
    """
    Validate an indian aadhar card number.

    Examples::

        >>> aadhar_card('3675 9834 6015')
        True

        >>> email('3675 ABVC 2133')
        ValidationFailure(func=aadhar_card, args={'value': '3675 ABVC 2133'})
    """
    if(re.search(aadhar_card_regex, value)):
        return True
    return False

@validator
def pan_card(value):
    """
    Validate a pan card number.

    Examples::

        >>> pan_card('ABCDE9999K')
        True

        >>> pan_card('ABC5d7896B')
        ValidationFailure(func=pan_card, args={'value': 'ABC5d7896B'})
    """
    if(re.search(pan_card_regex, value)):
        return True
    return False