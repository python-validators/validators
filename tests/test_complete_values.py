"""Validate complete MAC addresses and regional identifiers."""

from typing import Callable

import pytest

from validators import ValidationError, mac_address
from validators.i18n.fi import fi_business_id, fi_ssn
from validators.i18n.fr import fr_ssn
from validators.i18n.ind import ind_aadhar


@pytest.mark.parametrize(
    "validate,value",
    [
        (mac_address, "01:23:45:67:ab:CD"),
        (mac_address, "01-23-45-67-ab-CD"),
        (fi_business_id, "0112038-9"),
        (fi_ssn, "010101-0101"),
        (fr_ssn, "1 84 12 76 451 089 46"),
        (fr_ssn, "1 84 12 76 451 089"),
        (ind_aadhar, "3675 9834 6015"),
    ],
)
@pytest.mark.parametrize("suffix", ["", "\n", "\r\n", " ", "\nextra"])
def test_complete_identifier(validate: Callable[[str], object], value: str, suffix: str):
    """Accept the identifier alone and reject any trailing characters."""
    if suffix:
        assert isinstance(validate(value + suffix), ValidationError)
    else:
        assert validate(value) is True
