from app.math_utils import add, divide
import pytest

def test_add():
    result = add(2, 3)
    assert result == 5


def test_add2():
    result2 = add(10, 5)
    assert result2 == 15


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
