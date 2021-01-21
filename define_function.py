def initlog(*args):
    pass # Remember to implement this!

# the pass statement does nothing.

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    
    print()

fib(2000)

# Other names can also be used to point to the fib() function
print("using other names to point to fib() function")
print(fib)
ak_47 = fib
print(ak_47(2000))

# the function above does not fit to the actual definition of function
# a function take an input(s) and yields an output(s)
# the fib() returns None if I do not declare what to return (output)
print("Function that returns an output")
def fib2(n): 
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    
    return result

store_output = fib2(100)
print(store_output)
