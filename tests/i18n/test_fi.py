# -*- coding: utf-8 -*-
import pytest

from validators import fi_business_id, fi_ssn, ValidationFailure


@pytest.mark.parametrize(('value',), [
    ('2336509-6',),  # Supercell
    ('0112038-9',),  # Fast Monkeys
    ('2417581-7',),  # Nokia
])
def test_returns_true_on_valid_business_id(value):
    assert fi_business_id(value)


@pytest.mark.parametrize(('value',), [
    (None,),
    ('',),
    ('1233312312',),
    ('1333333-8',),
    ('1231233-9',),
])
def test_returns_failed_validation_on_invalid_email(value):
    assert isinstance(fi_business_id(value), ValidationFailure)


@pytest.mark.parametrize(('value',), [
    ('010101-0101',),
    ('010101+0101',),
    ('010101A0101',),
])
def test_returns_true_on_valid_ssn(value):
    assert fi_ssn(value)


@pytest.mark.parametrize(('value',), [
    (None,),
    ('',),
    ('101010-0102',),
    ('10a010-0101',),
    ('101010-0\xe401',),
    ('101010b0101',)
])
def test_returns_failed_validation_on_invalid_ssn(value):
    assert isinstance(fi_ssn(value), ValidationFailure)
