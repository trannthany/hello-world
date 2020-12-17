import math_func
import pytest

#pytest allows us to add decorators and use -m

@pytest.mark.number
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(3) == 5

@pytest.mark.number
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(2) == 3

@pytest.mark.strings
def test_add_strings():
    result = math_func.add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Heldlo' not in result

@pytest.mark.strings
def test_product_strings():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello ' in result


# to run the test
# pytest test_math_func.py
# pytest test_math_func.py -v
# the -v gives you more details

# the test function names must start with the word test_
# the testing file .py (module) names must start with the word test_ for the command "py.test" to work
# if the testing file .py (module) doesn't start with the word test we have to use "pytest file_name.py -v"

# to run just one function in the test
# pytest test_math_func.py::test_add

# run the test that contains only the word "add"
# pytest -v -k "add"

# run the test that contains the word "add" or "string". We can use and operator 
# pytest -v -k "add or string"
# pytest -v -k "add and string"

# "mark" the -m needs import pytest 
# note: we run the script in the command line if the IDE show an error line, just ignore it because we have used pip to install not the IDE
# pytest -v -m number # runs all the tests that have marked with number
# pytest -v -m strings # runs all the tests that have marked with strings

# pytest -v -x # the -x will allow the pytest to exit when there is any failure
# pytest -v -x --tb=no # the --tb=no skips the text trace
# pytest -v --maxfail=2 # --maxfail waits until there are 2 maximum failures to exit
