# -*- coding: utf-8 -*-
import pytest
from validators import finnish_business_id, ValidationFailure


@pytest.mark.parametrize(('value',), [
    ('2336509-6',),  # Supercell
    ('0112038-9',),  # Fast Monkeys
    ('2417581-7',),  # Nokia
])
def test_returns_true_on_valid_business_id(value):
    assert finnish_business_id(value)


@pytest.mark.parametrize(('value',), [
    (None,),
    ('',),
    ('1233312312',),
    ('1333333-8',),
    ('1231233-9',),
])
def test_returns_failed_validation_on_invalid_email(value):
    assert isinstance(finnish_business_id(value), ValidationFailure)
