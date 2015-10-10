# -*- coding: utf-8 -*-
import pytest

from validators import url, ValidationFailure


@pytest.mark.parametrize(('address', 'require_tld'), [
    ('http://foobar.dk', True),
    ('http://foobar.dk', True),
    ('http://foobar.museum/foobar', True),
    ('http://127.0.0.1/foobar', True),
    ('http://127.0.0.1:9000/fake', True),
    ('http://localhost/foobar', False),
    ('http://foobar', False),
])
def test_returns_true_on_valid_url(address, require_tld):
    assert url(address, require_tld=require_tld)


@pytest.mark.parametrize(('address',), [
    ('http://foobar',),
    ('foobar.dk',),
    ('http://127.0.0/asdf',),
    ('http://foobar.d',),
    ('http://foobar.12',),
    ('http://localhost:abc/a',),
])
def test_returns_failed_validation_on_invalid_url(address):
    assert isinstance(url(address), ValidationFailure)
