# lambda syntax allows function to be created on the fly.
# this is known as anonymous
# this practice is used when passing a simple function as an argument to another function
# lambda funciton is not powerful as named functions
# lambda function can only do things that require a single expression - usually equivalent to a single line of code

def my_func(f, arg):
    return f(arg)

my_func(lambda x: 2*x*x, 5)

#this is a conventional named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

# write the named function in lambda syntax
print((lambda x: x**2 + 5*x + 4) (-4))

# lambda functions can be assigned to variables, and used like normal functions
double = lambda x: x * 2
print(double(7))

add = lambda x, y: x + y
print(add(4, 5))
# It is usually better to define a named function using def instead

# Sololearn