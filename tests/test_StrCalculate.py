import pytest
from src.StrCalculate import StrCalculate
@pytest.mark.parametrize("string, result_expected", [("",0), ("0",0), ("1",1), ("2",2), ("1,1", 2), ("0,2",2), ("3",3), ("1,2",3), ("2,1",3), ("0,3",3), ("4,5",9),("7,6",13),("19,7",26),("24,31",55),("147,854",1001)])

def test(string, result_expected):
    actual_result = StrCalculate(string)
    assert actual_result == result_expected