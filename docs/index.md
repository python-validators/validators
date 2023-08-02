# validators - Python Data Validation for Humans™

[![PyCQA][pycqa-badge]][pycqa-link] [![SAST][sast-badge]][sast-link] [![Package][package-badge]][package-link] [![Docs][docs-badge]][docs-link] [![Version][vs-badge]][vs-link] [![Downloads][dw-badge]][dw-link]

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
- [Bugtracker](https://github.com/python-validators/validators/issues)
- [Security](https://github.com/python-validators/validators/blob/master/SECURITY.md)
- [Code](https://github.com/python-validators/validators/)

[//]: #(Links)
[sast-badge]: https://github.com/python-validators/validators/actions/workflows/sast.yaml/badge.svg
[sast-link]: https://github.com/python-validators/validators/actions/workflows/sast.yaml
[pycqa-badge]: https://github.com/python-validators/validators/actions/workflows/pycqa.yaml/badge.svg
[pycqa-link]: https://github.com/python-validators/validators/actions/workflows/pycqa.yaml
[package-badge]: https://github.com/python-validators/validators/actions/workflows/package.yaml/badge.svg
[package-link]: https://github.com/python-validators/validators/actions/workflows/package.yaml
[docs-badge]: https://github.com/python-validators/validators/actions/workflows/docs.yaml/badge.svg
[docs-link]: https://github.com/python-validators/validators/actions/workflows/docs.yaml
[vs-badge]: https://img.shields.io/pypi/v/validators.svg
[vs-link]: https://pypi.python.org/pypi/validators/
[dw-badge]: https://img.shields.io/pypi/dm/validators.svg
[dw-link]: https://pypi.python.org/pypi/validators/
