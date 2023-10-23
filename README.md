# validators - Python Data Validation for Humans™

[![PyCQA][pycqa-badge]][pycqa-link] [![SAST][sast-badge]][sast-link] [![Docs][docs-badge]][docs-link] [![Version][vs-badge]][vs-link] [![Downloads][dw-badge]][dw-link]

<!-- [![Package][package-badge]][package-link] -->

Python has all kinds of data validation tools, but every one of them seems to
require defining a schema or form. I wanted to create a simple validation
library where validating a simple value does not require defining a form or a
schema.

```python
>>> import validators
>>> 
>>> validators.email('someone@example.com')
True
```

## Email Validation using `validate_email`

You can use the `validate_email` library to check the validity of an email address.

```python
from validate_email_address import validate_email

email = "example@email.com"
is_valid = validate_email(email)

if is_valid:
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")
```

## URL Validation

To validate URLs in Python, you can use the `validators` library. Here's an example:

```python
from validators import url

url_to_validate = "https://www.example.com"
is_valid = url(url_to_validate)

if is_valid:
    print(f"{url_to_validate} is a valid URL.")
else:
    print(f"{url_to_validate} is not a valid URL.")
```

## Integer Validation

To validate if a string represents a valid integer in Python, you can use a custom function. Here's an example:

```python
def is_valid_integer(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False

num_str = "42"
if is_valid_integer(num_str):
    print(f"{num_str} is a valid integer.")
else:
    print(f"{num_str} is not a valid integer.")
```

## Date Validation using `dateutil`

To validate dates and parse them, you can use the `dateutil` library. Here's an example:

```python
from dateutil.parser import parse

date_str = "2023-10-23"
try:
    valid_date = parse(date_str)
    print(f"{date_str} is a valid date.")
except ValueError:
    print(f"{date_str} is not a valid date.")
```


## Resources

- [Documentation](https://python-validators.github.io/validators/)
- [Bugtracker](https://github.com/python-validators/validators/issues)
- [Security](https://github.com/python-validators/validators/blob/master/SECURITY.md)
- [Code](https://github.com/python-validators/validators/)

[//]: #(Links)
[sast-badge]: https://github.com/python-validators/validators/actions/workflows/sast.yaml/badge.svg
[sast-link]: https://github.com/python-validators/validators/actions/workflows/sast.yaml
[pycqa-badge]: https://github.com/python-validators/validators/actions/workflows/pycqa.yaml/badge.svg
[pycqa-link]: https://github.com/python-validators/validators/actions/workflows/pycqa.yaml
[docs-badge]: https://github.com/python-validators/validators/actions/workflows/docs.yaml/badge.svg
[docs-link]: https://github.com/python-validators/validators/actions/workflows/docs.yaml
[vs-badge]: https://img.shields.io/pypi/v/validators?logo=pypi&logoColor=white&label=version&color=blue
[vs-link]: https://pypi.python.org/pypi/validators/
[dw-badge]: https://img.shields.io/pypi/dm/validators?logo=pypi&logoColor=white&color=blue
[dw-link]: https://pypi.python.org/pypi/validators/

<!-- [package-badge]: https://github.com/python-validators/validators/actions/workflows/package.yaml/badge.svg
[package-link]: https://github.com/python-validators/validators/actions/workflows/package.yaml -->
