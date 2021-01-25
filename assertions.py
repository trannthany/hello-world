# Assertion is a sanity-check that you can turn on or turn off when you have finished testing the program
# an expression is tested, and if the result comes up false, an exception is raised
# assertions are carried out through use of the assert statement

# print(1)
# assert 2 + 2 == 4
# print(2)
# assert 1 + 1 == 3
# print(3)

# The assert can take a second argument that is passed to the AssertionError raised if the assertion fails
temperature = -10
assert (temperature >= 0), "Colder than absolute zero!"