from unittest.mock import Mock
from .. import module

def test_big():
    dataframe = Mock()
    dataframe.shape = (2000000, 1)
    assert my_module.is_dataframe_big(dataframe) is True

def test_not_big():
    dataframe = Mock()
    dataframe.shape = (100, 1)
    assert my_module.is_dataframe_big(dataframe) is False
