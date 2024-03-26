# Install and Use

## Installation

Execute the following command:

```text
pip install validators
```

> It's preferable to use `pip` within a virtual environment.

## Usage

```python
import validators
print(validators.email('someone@example.com'))
```

### To raise validation error

1. Either set the environment variable `RAISE_VALIDATION_ERROR` to `True`

    ```console
    $ export RAISE_VALIDATION_ERROR=True
    $ python -c "from validators import url; print(url('https//bad_url'))"
    Traceback (most recent call last):
    File "<string>", line 1, in <module>
    File "/path/to/lib/validators/utils.py", line 87, in wrapper
        raise ValidationError(func, _func_args_as_dict(func, *args, **kwargs))
    validators.utils.ValidationError: ValidationError(func=url, args={'value': 'https//bad_url'})
    ```

2. Or pass `r_ve=True` to each caller function:

    ```console
    $ python -c "from validators.card import visa; print(visa('bad_visa_number', r_ve=True))"
    Traceback (most recent call last):
    File "<string>", line 1, in <module>
    File "/path/to/lib/validators/utils.py", line 87, in wrapper
        raise ValidationError(func, _func_args_as_dict(func, *args, **kwargs))
    validators.utils.ValidationError: ValidationError(func=visa, args={'value': 'bad_visa_number'})
    ```
