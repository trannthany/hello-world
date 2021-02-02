# itertools is a module of a standard library that contains serveral functionw, that require in functional programmig
# function count counts up infinitely from a value
# function cycle infinitely iterates through an iterable such as a string or a list
# function repeat repeats an object either infinitely or a specific number of times

from itertools import count, accumulate, takewhile, product, permutations

# for i in count(3):
#     print(i)
#     if i >= 11:
#         break


# There are many functions in itertools that operate on iterables in a similar way to map and filter
# Function takewhile takes items from an iterable while a predicate function remains true,
# Function chain combines several iterables into one long one
# Function accumulate returns a running total of values in an iterable

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x<= 6, nums)))

# product and permutation are used to accomplish a task with all possible combinations of some items
letters = ("A", "B", "C")
print(list(product(letters, range(2))))
print(list(permutations(letters)))