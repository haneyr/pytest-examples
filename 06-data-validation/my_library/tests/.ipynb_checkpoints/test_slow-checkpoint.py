import pytest

# Python relative import
from .. import module


def test_not_three():
    result = module.load_data()
    assert result != 3

def test_object_type():
    result = module.load_data()
    assert isinstance(result, int)

def test_is_five():
    result = module.load_data()
    assert result == 5
