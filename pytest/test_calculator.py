from calculator import Calculator, CalculatorError
import pytest


def test_add():
    calc = Calculator()
    result = calc.add(2, 3)
    assert result == 5


def test_add_weird_stuff():
    calc = Calculator()
    with pytest.raises(CalculatorError):
        result = calc.add("one", 2)


def test_subtract():
    calc = Calculator()
    result = calc.subtract(3, 2)
    assert result == 1


def test_multiply():
    calc = Calculator()
    result = calc.multiply(10, 2)
    assert result == 20


def test_divide():
    calc = Calculator()
    result = calc.divide(8, 4)
    assert result == 2

