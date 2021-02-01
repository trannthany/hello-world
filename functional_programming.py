# Functional programming is a style of programming that is based around functions.
# A key part of functional programming is higher-order functions. 
# Higher-order functions take other functions as arguments, or return them as results.

# the apply_twice function takes another function as its argument, and calls it twice inside its body
def apply_twice(func, arg):
    return func(func(arg))

def add_five(x): 
    return x + 5

print(apply_twice(add_five, 10))


# Pure functions
# Functional programming seeks to use pure functions.
# A pure functions have no side effects, and return a value that depends only on their arguments.
# E.g. cos(x) always return the same result for the same value of x

def pure_function(x, y):
    temp = x + 2 * y
    return temp / (2*x + y)

some_list = []
# the impure_function always change the state of some_list
def impure_function(arg):
    some_list.append(arg)

# Avantages of pure function are easier to run in parallel, test, and momoization
# Disavantages of pure function are over complicate I/O task which require side effects and can be difficult to write in some situation 
