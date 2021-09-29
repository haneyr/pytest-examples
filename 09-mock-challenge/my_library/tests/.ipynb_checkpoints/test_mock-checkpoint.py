from unittest.mock import Mock
from .. import module

def test_big():

    assert module.is_sum_of_series_big(series) is True


def test_not_big():

    assert module.is_sum_of_series_big(series) is False
