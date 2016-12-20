# -*- coding: utf-8 -*-
import pytest

from validators import image, ValidationFailure

#https://i.imgur.com/DKUR9Tk.png is Grumpy Cat


@pytest.mark.parametrize('address', [
    u'https://i.imgur.com/DKUR9Tk.png',
    u'https://i.imgur.com/DKUR9Tk.png?fb'
])
def test_returns_true_on_valid_image_url(address):
    assert image(path)


@pytest.mark.parametrize('address', [
    u'http://www.google.com/'
])
def test_returns_false_on_invalid_image_url(address):
    assert isinstance(image(address), ValidationFailure)
