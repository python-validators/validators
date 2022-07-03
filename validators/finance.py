

from .utils import validator

def cusipChecksum( cusip ) :

    check = 0 
    val = None  # just to be extra safe - should not be needed but ...

    for digitIndex in range(9) :
        c = cusip[digitIndex]
        if c >= '0' and c <= '9' :
            val = ord(c) - ord('0')
        elif c >= 'A' and c <= 'Z' :
            val = 10 + ord(c) - ord('A')
        elif c >= 'a' and c <= 'z' :
            val = 10 + ord(c) - ord('a')
        elif c == '*' :
            val = 36
        elif c == '@' :
            val = 37
        elif c == '#' :
            val = 38
        else :
            return False
        
        if digitIndex & 1 :
            val = val + val

        check = check + (val // 10) + (val % 10)

    return (check % 10) == 0


@validator
def cusip(value):
    """
    Return whether or not given value is a valid CUSIP.

    If the value is a valid CUSIP this function returns ``True``, otherwise
    :class:`~validators.utils.ValidationFailure`.

    Examples::

        >>> cusip('037833DP2')
        True

        >>> cusip('037833DP3')
        ValidationFailure(func=cusip, ...)

    .. versionadded:: 0.20

    :param value: CUSIP string to validate
    """
    return len(value)==9 and cusipChecksum(value) 



def isinChecksum( value ) :

    check = 0 
    val = None  # just to be extra safe - should not be needed but ...

    for digitIndex in range(12) :
        c = value[digitIndex]
        if c >= '0' and c <= '9' and digitIndex>1 :
            val = ord(c) - ord('0')
        elif c >= 'A' and c <= 'Z' :
            val = 10 + ord(c) - ord('A')
        elif c >= 'a' and c <= 'z' :
            val = 10 + ord(c) - ord('a')
        else :
            return False
        
        if digitIndex & 1 :
            val = val + val

    return  (check %10) == 0


@validator
def isin(value):
    """
    Return whether or not given value is a valid ISIN.

    If the value is a valid ISIN this function returns ``True``, otherwise
    :class:`~validators.utils.ValidationFailure`.

    Examples::

        >>> isin('037833DP2')
        True

        >>> isin('037833DP3')
        ValidationFailure(func=isin, ...)

    .. versionadded:: 0.20

    :param value: ISIN string to validate
    """
    return len(value)==12 and isinChecksum(value) 




@validator
def sedol(value):
    """
    Return whether or not given value is a valid SEDOL.

    If the value is a valid SEDOL this function returns ``True``, otherwise
    :class:`~validators.utils.ValidationFailure`.

    Examples::

        >>> sedol('2936921')
        True

        >>> sedol('29A6922')
        ValidationFailure(func=sedol, ...)

    .. versionadded:: 0.20

    :param value: SEDOL string to validate
    """
    if len(value)!=7 :
        return False 

    weights = [ 1, 3, 1, 7, 3, 9, 1 ]
    check = 0 
    for digitIndex in range(7) :
        c = value[digitIndex]
        if c in 'AEIOU' :
            return False 

        val = None
        if c >= '0' and c <= '9' :
            val = ord(c) - ord('0')
        elif c >= 'A' and c <= 'Z' :
            val = 10 + ord(c) - ord('A')
        else :
            return False
        check += val * weights[digitIndex] 

    return (check%10)==0
