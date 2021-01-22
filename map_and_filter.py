# map and filter are built-in functions which are very useful higher-order functions that operate on lists
# (or similar objects called iterables)


# The map function takes a function and an iterable as arguments, and returns a new iterable with the function applied to each argument

def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

# we can achieve the same result using lambda
result2 = list(map(lambda x: x+5, nums))
print(result2)

# The filter function filters an iterable by removing items that don't match a predicate (a function that returns a Boolean)
result3 = list(filter(lambda x: x%2==0, nums))
print(result3)

def is_even(y):
    return y%2 == 0
result4 = list(filter(is_even, nums))
print(result4)