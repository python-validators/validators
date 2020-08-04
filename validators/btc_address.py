import re

from .utils import validator

pattern = re.compile(r"^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$")


@validator
def btc_address(value):
    return pattern.match(value)
