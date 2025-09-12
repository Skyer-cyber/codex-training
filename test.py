from src.calculator import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 4) == 6  # 这个测试会失败，用于练习

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5
    
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
