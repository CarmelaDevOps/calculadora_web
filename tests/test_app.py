import pytest

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def test_suma():
    assert suma(2, 3) == 5

def test_resta():
   assert resta(5, 2) == 3

def test_multiplicacion():
    assert multiplicacion(4, 3) == 12

def test_division():
    assert division(10, 2) == 5

def test_division_por_cero():
    with pytest.raises(ValueError):
        division(5, 0)
