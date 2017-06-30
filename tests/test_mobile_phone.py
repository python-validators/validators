"""Test the mobile_phone validator."""
import pytest

from validators import mobile_phone


@pytest.mark.parametrize(('value', 'locale'), [
    ('+254705890890', 'en-KE'),
    ('+1-202-555-0178', None),
    ('+1-202-555-0178', 'en-US'),
    ('+1-613-555-0178', None),
])
def test_returns_true_on_valid_mobile_phone(value, locale):
    """Test that mobile_phone will validate truthy."""
    assert mobile_phone.mobile_phone(value, locale=locale)


@pytest.mark.parametrize(('value', 'locale'), [
    ('+2547058908', 'en-KE'),
    ('+1-202-555-01', None),
    ('+61 1900 654 321', 'en-US'),
    ('+36 55 603 089', None),
    ('+1-613-555-01', None),
    ('+44 1632 960804', 'en-GB'),
])
def test_returns_false_on_valid_mobile_phone(value, locale):
    """Test falsey validation of mobile_phone."""
    with pytest.raises(AssertionError):
        assert mobile_phone.mobile_phone(value, locale=locale)
