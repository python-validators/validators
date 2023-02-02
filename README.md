# validators - Python Data Validation for Humans™

[![Build Status][bs-badge]][bs-link] [![Version Status][vs-badge]][vs-link] [![Downloads][dw-badge]][dw-link]

Python has all kinds of data validation tools, but every one of them seems to
require defining a schema or form. I wanted to create a simple validation
library where validating a simple value does not require defining a form or a
schema.

```py
>>> import validators

>>> validators.email('someone@example.com')
True
```

## Resources

- [Documentation](https://validators.readthedocs.io/)
- [Issue Tracker](http://github.com/kvesteri/validators/issues)
- [Code](http://github.com/kvesteri/validators/)

[bs-badge]: https://github.com/kvesteri/validators/workflows/GH/badge.svg
[bs-link]: https://github.com/kvesteri/validators/actions/workflows/main.yml
[vs-badge]: https://img.shields.io/pypi/v/validators.svg
[vs-link]: https://pypi.python.org/pypi/validators/
[dw-badge]: https://img.shields.io/pypi/dm/validators.svg
[dw-link]: https://pypi.python.org/pypi/validators/
