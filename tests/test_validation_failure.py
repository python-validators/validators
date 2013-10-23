import validators
import six


obj_repr = (
    "ValidationFailure(func=number_range, "
    "args={'max': 5, 'value': 3, 'min': 4})"
)


class TestValidationFailure(object):
    def setup_method(self, method):
        self.obj = validators.number_range(3, min=4, max=5)

    def test_boolean_coerce(self):
        assert not bool(self.obj)
        assert not self.obj

    def test_repr(self):
        assert repr(self.obj) == obj_repr

    def test_unicode(self):
        assert six.text_type(self.obj) == obj_repr

    def test_arguments_as_properties(self):
        assert self.obj.value == 3
        assert self.obj.min == 4
        assert self.obj.max == 5
