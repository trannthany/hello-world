def my_func():
    yield 'a'
    yield 'b'
    yield 'c'


# return vs yield (return stops the function, yield remembers the state of the function)

x = my_func() # my_func() returns an iterator object

print(next(x))
print(next(x))
print(next(x))
#print(next(x)) # throw an error