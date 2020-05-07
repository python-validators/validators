# -*- coding: utf-8 -*-
import pytest

from validators import (
    amex,
    card_number,
    diners,
    discover,
    jcb,
    mastercard,
    unionpay,
    ValidationFailure,
    visa
)

visa_cards = [
    '4242424242424242',
    '4000002760003184'
]
mastercard_cards = [
    '5555555555554444',
    '2223003122003222'
]
amex_cards = [
    '378282246310005',
    '371449635398431'
]
unionpay_cards = [
    '6200000000000005'
]
diners_cards = [
    '3056930009020004',
    '36227206271667'
]
jcb_cards = [
    '3566002020360505'
]
discover_cards = [
    '6011111111111117',
    '6011000990139424'
]


@pytest.mark.parametrize(
    "value",
    visa_cards
    + mastercard_cards
    + amex_cards
    + unionpay_cards
    + diners_cards
    + jcb_cards
    + discover_cards,
)
def test_returns_true_on_valid_card_number(value):
    assert card_number(value)


@pytest.mark.parametrize('value', [
    '4242424242424240',
    '4000002760003180',
    '400000276000318X'
])
def test_returns_failed_on_valid_card_number(value):
    assert isinstance(card_number(value), ValidationFailure)


@pytest.mark.parametrize('value', visa_cards)
def test_returns_true_on_valid_visa(value):
    assert visa(value)


@pytest.mark.parametrize(
    "value",
    mastercard_cards
    + amex_cards
    + unionpay_cards
    + diners_cards
    + jcb_cards
    + discover_cards,
)
def test_returns_failed_on_valid_visa(value):
    assert isinstance(visa(value), ValidationFailure)


@pytest.mark.parametrize('value', mastercard_cards)
def test_returns_true_on_valid_mastercard(value):
    assert mastercard(value)


@pytest.mark.parametrize(
    "value",
    visa_cards
    + amex_cards
    + unionpay_cards
    + diners_cards
    + jcb_cards
    + discover_cards,
)
def test_returns_failed_on_valid_mastercard(value):
    assert isinstance(mastercard(value), ValidationFailure)


@pytest.mark.parametrize('value', amex_cards)
def test_returns_true_on_valid_amex(value):
    assert amex(value)


@pytest.mark.parametrize(
    "value",
    visa_cards
    + mastercard_cards
    + unionpay_cards
    + diners_cards
    + jcb_cards
    + discover_cards,
)
def test_returns_failed_on_valid_amex(value):
    assert isinstance(amex(value), ValidationFailure)


@pytest.mark.parametrize('value', unionpay_cards)
def test_returns_true_on_valid_unionpay(value):
    assert unionpay(value)


@pytest.mark.parametrize(
    "value",
    visa_cards
    + mastercard_cards
    + amex_cards
    + diners_cards
    + jcb_cards
    + discover_cards,
)
def test_returns_failed_on_valid_unionpay(value):
    assert isinstance(unionpay(value), ValidationFailure)


@pytest.mark.parametrize('value', diners_cards)
def test_returns_true_on_valid_diners(value):
    assert diners(value)


@pytest.mark.parametrize(
    "value",
    visa_cards
    + mastercard_cards
    + amex_cards
    + unionpay_cards
    + jcb_cards
    + discover_cards,
)
def test_returns_failed_on_valid_diners(value):
    assert isinstance(diners(value), ValidationFailure)


@pytest.mark.parametrize('value', jcb_cards)
def test_returns_true_on_valid_jcb(value):
    assert jcb(value)


@pytest.mark.parametrize(
    "value",
    visa_cards
    + mastercard_cards
    + amex_cards
    + unionpay_cards
    + diners_cards
    + discover_cards,
)
def test_returns_failed_on_valid_jcb(value):
    assert isinstance(jcb(value), ValidationFailure)


@pytest.mark.parametrize('value', discover_cards)
def test_returns_true_on_valid_discover(value):
    assert discover(value)


@pytest.mark.parametrize(
    "value",
    visa_cards
    + mastercard_cards
    + amex_cards
    + unionpay_cards
    + diners_cards
    + jcb_cards,
)
def test_returns_failed_on_valid_discover(value):
    assert isinstance(discover(value), ValidationFailure)
