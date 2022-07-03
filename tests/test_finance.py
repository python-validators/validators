# -*- coding: utf-8 -*-
import pytest

import validators

#good values
@pytest.mark.parametrize('value', [
    '912796X38',
    '912796X20',
    '912796x20'
])
def test_returns_true_on_valid_cusip(value):
    assert validators.cusip(value)

#bad values 
@pytest.mark.parametrize('value', [
    '912796T67',
    '912796T68',
    'XCVF',
    '00^^^1234',
    '1234567890'
])
def test_returns_failed_validation_on_invalid_cusip(value):
    result = validators.cusip(value)
    assert isinstance(result, validators.ValidationFailure)



#good values
@pytest.mark.parametrize('value', [
    '0263494',
    '0540528',
    'B000009'
])
def test_returns_true_on_valid_sedol(value):
    assert validators.sedol(value)

#bad values 
@pytest.mark.parametrize('value', [
    '0540526',
    'XCVF',
    '00^^^1234',
    'A000009'
])
def test_returns_failed_validation_on_invalid_sedol(value):
    result = validators.sedol(value)
    assert isinstance(result, validators.ValidationFailure)




#good values
@pytest.mark.parametrize('value', [
    'US0004026250',
    'JP000K0VF054',
    'US0378331005'
])
def test_returns_true_on_valid_isin(value):
    assert validators.isin(value)

#bad values 
@pytest.mark.parametrize('value', [
    '010378331005'
    'XCVF',
    '00^^^1234',
    'A000009'
])
def test_returns_failed_validation_on_invalid_isin(value):
    result = validators.isin(value)
    assert isinstance(result, validators.ValidationFailure)
