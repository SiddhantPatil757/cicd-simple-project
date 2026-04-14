from src.calculator import add, subtract , multiplication , division

def test_add():
    assert add(2,3) == 5

def test_subtract():
    assert subtract(5,3) == 2

def test_multiplication():
    assert multiplication(5,3) == 15

def test_division():
    assert division(10,5) == 2



