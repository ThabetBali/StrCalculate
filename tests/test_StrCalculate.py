from src.StrCalculate import StrCalculate


def test_StrCalculate_function():
    StrCalculate("")

def test_empty_string():
    assert StrCalculate("")==0