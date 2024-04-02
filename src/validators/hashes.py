"""Hashes."""

# standard
import re

# local
from .utils import validator


@validator
def base58(value: str, /):
    """Return whether or not given value is a valid base58 hash.

    Examples:
        >>> base58('14pq6y9H2DLGahPsM4s7ugsNSD2uxpHsJx')
        # Output: True
        >>> base58('cUSECm5YzcXJwP')
        # Output: ValidationError(func=base58, args={'value': 'cUSECm5YzcXJwP'})

    Args:
        value:
            base58 string to validate.

    Returns:
        (Literal[True]): If `value` is a valid base58 hash.
        (ValidationError): If `value` is an invalid base58 hash.
    """
    return re.match(r"^[1-9A-HJ-NP-Za-km-z]+$", value) if value else False


@validator
def base64(value: str, /):
    """Return whether or not given value is a valid base64 hash.

    Examples:
        >>> base64('Y2hhcmFjdGVyIHNldA==')
        # Output: True
        >>> base64('cUSECm5YzcXJwP')
        # Output: ValidationError(func=base64, args={'value': 'cUSECm5YzcXJwP'})

    Args:
        value:
            base64 string to validate.

    Returns:
        (Literal[True]): If `value` is a valid base64 hash.
        (ValidationError): If `value` is an invalid base64 hash.
    """
    return (
        re.match(r"^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$", value)
        if value
        else False
    )


@validator
def md5(value: str, /):
    """Return whether or not given value is a valid MD5 hash.

    Examples:
        >>> md5('d41d8cd98f00b204e9800998ecf8427e')
        # Output: True
        >>> md5('900zz11')
        # Output: ValidationError(func=md5, args={'value': '900zz11'})

    Args:
        value:
            MD5 string to validate.

    Returns:
        (Literal[True]): If `value` is a valid MD5 hash.
        (ValidationError): If `value` is an invalid MD5 hash.
    """
    return re.match(r"^[0-9a-f]{32}$", value, re.IGNORECASE) if value else False


@validator
def sha1(value: str, /):
    """Return whether or not given value is a valid SHA1 hash.

    Examples:
        >>> sha1('da39a3ee5e6b4b0d3255bfef95601890afd80709')
        # Output: True
        >>> sha1('900zz11')
        # Output: ValidationError(func=sha1, args={'value': '900zz11'})

    Args:
        value:
            SHA1 string to validate.

    Returns:
        (Literal[True]): If `value` is a valid SHA1 hash.
        (ValidationError): If `value` is an invalid SHA1 hash.
    """
    return re.match(r"^[0-9a-f]{40}$", value, re.IGNORECASE) if value else False


@validator
def sha224(value: str, /):
    """Return whether or not given value is a valid SHA224 hash.

    Examples:
        >>> sha224('d14a028c2a3a2bc9476102bb288234c415a2b01f828ea62ac5b3e42f')
        # Output: True
        >>> sha224('900zz11')
        # Output: ValidationError(func=sha224, args={'value': '900zz11'})

    Args:
        value:
            SHA224 string to validate.

    Returns:
        (Literal[True]): If `value` is a valid SHA224 hash.
        (ValidationError): If `value` is an invalid SHA224 hash.
    """
    return re.match(r"^[0-9a-f]{56}$", value, re.IGNORECASE) if value else False


@validator
def sha256(value: str, /):
    """Return whether or not given value is a valid SHA256 hash.

    Examples:
        >>> sha256(
        ...     'e3b0c44298fc1c149afbf4c8996fb924'
        ...     '27ae41e4649b934ca495991b7852b855'
        ... )
        # Output: True
        >>> sha256('900zz11')
        # Output: ValidationError(func=sha256, args={'value': '900zz11'})

    Args:
        value:
            SHA256 string to validate.

    Returns:
        (Literal[True]): If `value` is a valid SHA256 hash.
        (ValidationError): If `value` is an invalid SHA256 hash.
    """
    return re.match(r"^[0-9a-f]{64}$", value, re.IGNORECASE) if value else False


@validator
def sha512(value: str, /):
    """Return whether or not given value is a valid SHA512 hash.

    Examples:
        >>> sha512(
        ...     'cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce'
        ...     '9ce47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af9'
        ...     '27da3e'
        ... )
        # Output: True
        >>> sha512('900zz11')
        # Output: ValidationError(func=sha512, args={'value': '900zz11'})

    Args:
        value:
            SHA512 string to validate.

    Returns:
        (Literal[True]): If `value` is a valid SHA512 hash.
        (ValidationError): If `value` is an invalid SHA512 hash.
    """
    return re.match(r"^[0-9a-f]{128}$", value, re.IGNORECASE) if value else False
