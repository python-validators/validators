# -*- coding: utf-8 -*-
import pytest
from validators import domain, ValidationFailure


@pytest.mark.parametrize(('value',), [
    ('example.com',),
])
def test_returns_true_on_valid_domain(value):
    assert domain(value)


@pytest.mark.parametrize(('value',), [
    ('example.com/',),
    ('example.com:4444',),
    ('example.-com',),
    ('example.',),
    ('example',),
])
def test_returns_failed_validation_on_invalid_domain(value):
    assert isinstance(domain(value), ValidationFailure)
