import os
import imghdr

from io import BytesIO
from .url import url

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

from .utils import validator, ValidationFailure


def _image_url(path):
    result = False

    try:
        if url(path):
            response = urlopen(path)
            data = BytesIO(response.read())
            if imghdr.what(data) is not None:
                result = True
            else:
                result = False
    except ValidationFailure:
        result = False

    return result


def _image_file(path):
    result = False

    if os.path.exists(path):
        if imghdr.what(path) is not None:
            result = True
        else:
            result = False

    return result


@validator
def image(path):
    """
    Return whether or not a file is a valid image type.

    If the file is a valid image type this function returns ``True``, otherwise
    :class:`~validators.utils.ValidationFailure`.

    Examples::
        >>> image('pic.jpg')
        True

        >>> image('https://i.imgur.com/DKUR9Tk.png')
        True

    :param path: The path to the file to evaluate.
    """

    result = False

    if _image_url(path):
        result = True
    elif _image_file(path):
        result = True
    else:
        result = False

    return result
