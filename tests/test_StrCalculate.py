import pytest
from src.StrCalculate import StrCalculate
@pytest.mark.parametrize("string, result_expected", [("",0), ("0",0)])

def test(string, result_expected):
    actual_result = StrCalculate(string)
    assert actual_result == result_expected