# -*- coding: utf-8 -*-
import pytest

from validators import ir_national_code
import random

# from https://gist.github.com/Alireza2n/5708c361ca8417dec0f355d8eb51bc2b
def random_national_code_generator():
    number_list = []
    _sum = 0
    out = ""
    for i in reversed(range(2, 11)):
        _j = random.randint(0, 9)
        number_list.append(str(_j))
        _sum += _j * i
    _m = _sum % 11
    if _m < 2:
        number_list.append(str(_m))
    elif _m >= 2:
        number_list.append(str(11 - _m))
    return out.join(number_list)

@pytest.mark.parametrize(('value',), [
    (random_national_code_generator(),),
    (random_national_code_generator(),),
    ('1111111111',), # same number is not invalid http://www.fardanews.com/fa/news/127747

])
def test_returns_true_on_valid_national_code(value):
    assert ir_national_code(value)

@pytest.mark.parametrize(('value',), [
    (None,),
    ('0000000000',),
    ('1234567890',),
    ('123456789',),
    ('',),
])
def test_returns_True_on_not_valid_national_code(value):
    assert not ir_national_code(value)
