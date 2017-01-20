# -*- coding: utf-8 -*-
import pytest

from validators import email, ValidationFailure


@pytest.mark.parametrize(('value', 'whitelist'), [
    ('email@here.com', None),
    ('weirder-email@here.and.there.com', None),
    ('email@[127.0.0.1]', None),
    ('example@valid-----hyphens.com', None),
    ('example@valid-with-hyphens.com', None),
    ('test@domain.with.idn.tld.उदाहरण.परीक्षा', None),
    ('email@localhost', None),
    ('email@localdomain', ['localdomain']),
    ('"test@test"@example.com', None),
    ('"\\\011"@here.com', None),
])
def test_returns_true_on_valid_email(value, whitelist):
    assert email(value, whitelist=whitelist)


@pytest.mark.parametrize(('value',), [
    (None,),
    ('',),
    ('abc',),
    ('abc@',),
    ('abc@bar',),
    ('a @x.cz',),
    ('abc@.com',),
    ('something@@somewhere.com',),
    ('email@127.0.0.1',),
    ('example@invalid-.com',),
    ('example@-invalid.com',),
    ('example@inv-.alid-.com',),
    ('example@inv-.-alid.com',),
    # Quoted-string format (CR not allowed)
    ('"\\\012"@here.com',),
])
def test_returns_failed_validation_on_invalid_email(value):
    assert isinstance(email(value), ValidationFailure)


@pytest.mark.parametrize(('value', 'whitelist'), [
    ('email@here.com', ['foo.here.com']),
    ('weirder-email@here.and.there.com', ['here.and.there.org']),
    ('email@[127.0.0.1]', ['[127.0.0.2]']),
    ('example@valid-----hyphens.com', ['-----hyphens.com']),
    ('example@valid-with-hyphens.com', ['hyphens.com']),
    ('email@localhost', ['localdomain']),
    ('"test@test"@example.com', ['example.org', 'example.net', 'foo.org']),
    ('"\\\011"@here.com', ['there.com']),
])
def test_returns_failed_validation_on_bad_whitelist(value, whitelist):
    assert isinstance(email(value, whitelist=whitelist, only_whitelist=True),
                      ValidationFailure)


@pytest.mark.parametrize(('value', 'whitelist'), [
    ('email@here.com', ['here.com']),
    ('weirder-email@here.and.there.com', ['here.and.there.com']),
    ('email@[127.0.0.1]', ['[127.0.0.1]']),
    ('example@valid-----hyphens.com', ['valid-----hyphens.com']),
    ('example@valid-with-hyphens.com', ['valid-with-hyphens.com']),
    ('email@localhost', ['localdomain', 'localhost']),
    ('"test@test"@example.com', ['example.org', 'example.com', 'foo.org']),
    ('"\\\011"@here.com', ['here.com', 'test.org', 'zeta', 100]),
])
def test_returns_true_on_valid_email_and_only_whitelist(value, whitelist):
    assert email(value, whitelist=whitelist, only_whitelist=True)
