import pytest

from validators.indian_cards import aadhar_card , pan_card
from validators import ValidationFailure


@pytest.mark.parametrize('value', [
    '3675 9834 6012'
    '5046 3182 4299'
])
def test_returns_true_on_valid_aadhar_card(value):
    assert aadhar_card(value)

@pytest.mark.parametrize('value', [
    '3675 9834 6012 8',
    '417598346012',
    '3675 98AF 60#2'
])
def test_returns_failed_validation_on_invalid_aadhar_card(value):
    result = aadhar_card(value)
    assert isinstance(result, ValidationFailure)

@pytest.mark.parametrize('value', [
    'ABCDE9999K'
    'AAAPL1234C'
])
def test_returns_true_on_valid_pan_card(value):
    assert pan_card(value)

@pytest.mark.parametrize('value', [
    'ABC5d7896B',
    '417598346012',
    'AAAPL 1234C'
    'AaaPL1234C'
])

def test_returns_failed_validation_on_invalid_pan_card(value):
    result = pan_card(value)
    assert isinstance(result, ValidationFailure)
