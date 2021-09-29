from unittest.mock import Mock
from .. import my_module

def test_big():

    assert my_module.is_sum_of_series_big(series) is True


def test_not_big():

    assert my_module.is_sum_of_series_big(series) is False
