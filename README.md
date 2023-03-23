# validators - Python Data Validation for Humans™

[![Tests][tests-badge]][tests-link] [![Bandit][bandit-badge]][bandit-link] [![Version Status][vs-badge]][vs-link] [![Downloads][dw-badge]][dw-link]

Python has all kinds of data validation tools, but every one of them seems to
require defining a schema or form. I wanted to create a simple validation
library where validating a simple value does not require defining a form or a
schema.

```python
>>> import validators

>>> validators.email('someone@example.com')
True
```

## Resources

- [Documentation](https://python-validators.github.io/validators/)
- [Issue Tracker](https://github.com/python-validators/validators/issues)
- [Security](https://github.com/python-validators/validators/blob/master/SECURITY.md)
- [Code](https://github.com/python-validators/validators/)

[//]: #(Links)

[bandit-badge]: https://github.com/python-validators/validators/actions/workflows/bandit.yml/badge.svg
[bandit-link]: https://github.com/python-validators/validators/actions/workflows/bandit.yml
[tests-badge]: https://github.com/python-validators/validators/actions/workflows/main.yml/badge.svg
[tests-link]: https://github.com/python-validators/validators/actions/workflows/main.yml
[vs-badge]: https://img.shields.io/pypi/v/validators.svg
[vs-link]: https://pypi.python.org/pypi/validators/
[dw-badge]: https://img.shields.io/pypi/dm/validators.svg
[dw-link]: https://pypi.python.org/pypi/validators/
