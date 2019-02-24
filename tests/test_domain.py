# -*- coding: utf-8 -*-
import pytest

from validators import domain, ValidationFailure


@pytest.mark.parametrize('value', [
    'example.com',
    'xn----gtbspbbmkef.xn--p1ai',
    'underscore_subdomain.example.com',
    'something.versicherung',
    '11.com',
    'somerandomexample.xn--fiqs8s',
    'ktbooks.1.v77.faidns.com',
    'us.2.cqcounter.com',
    'ms127.0.0.101341.club',
    '1.adbrite.com',
])
def test_returns_true_on_valid_domain(value):
    assert domain(value)


@pytest.mark.parametrize('value', [
    'example.com/',
    'example.com:4444',
    'example.-com',
    'example.',
    '-example.com',
    'example',
    'a......b.com'
])
def test_returns_failed_validation_on_invalid_domain(value):
    assert isinstance(domain(value), ValidationFailure)
