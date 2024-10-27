"""Inn."""

# from .utils import validator


# @validator
def inn(value: str):
    """Description"""
    if not value:
        return False

    try:
        digits = list(map(int, value))
        # person
        if len(digits) == 10:
            weight_coefs = [2, 4, 10, 3, 5, 9, 4, 6, 8, 0]
            control_number = sum([d * w for d, w in zip(digits, weight_coefs)]) % 11
            return (control_number % 10) == digits[-1] if control_number > 9 else control_number == digits[-1]
        # company
        elif len(digits) == 12:
            weight_coefs1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 6, 0, 0]
            weight_coefs2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 0, 0, 0]
            pass
        # error inn
        else:
            return False
    except ValueError:
        return False

if "__main__" == __name__:
    print(inn('5260355389'))
