import math_func

def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(3) == 5

def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(2) == 4
    
# to run the test
# pytest test_math_func.py
