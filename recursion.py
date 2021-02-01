# Recursion is a very important concept in functional programming
# Recursion is a function that calls itself

def factorial(x):
    if x == 1: # this is the base case to allow the function exits the recursion
        return 1
    else:
        return x * factorial(x -1)

print(factorial(5))

# Recursion can also be indirect
# One function can call a second which calls the first which calls the second and so on

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

print(is_odd(17))
print(is_even(1))