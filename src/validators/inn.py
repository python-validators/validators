"""Inn."""

# from .utils import validator


# @validator
def inn(value: str, /):
    """Return whether or not given value is a valid russian individual tax number.

    Examples:
        >>> inn('7736050003')
        # Output: True
        >>> inn('781100086042')
        # Output: True

    Args:
        value:
            Individual tax number string to validate

    Returns:
        (Literal[True]): If `value` is a valid russian individual tax number.
        (ValidationError): If `value` is an invalid russian individual tax number.

    Returns:

    """
    if not value:
        return False

    try:
        digits = list(map(int, value))
        # company
        if len(digits) == 10:
            weight_coefs = [2, 4, 10, 3, 5, 9, 4, 6, 8, 0]
            control_number = sum([d * w for d, w in zip(digits, weight_coefs)]) % 11
            return (control_number % 10) == digits[-1] if control_number > 9 else control_number == digits[-1]
        # person
        elif len(digits) == 12:
            weight_coefs1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 0, 0]
            control_number1 = sum([d * w for d, w in zip(digits, weight_coefs1)]) % 11
            weight_coefs2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8, 0]
            control_number2 = sum([d * w for d, w in zip(digits, weight_coefs2)]) % 11
            print(control_number1, control_number2, value)
            return ((control_number1 % 10) == digits[-2] if control_number1 > 9 else control_number1 == digits[-2] and
                    (control_number2 % 10) == digits[-1] if control_number2 > 9 else control_number2 == digits[-1])
        else:
            return False
    except ValueError:
        return False
