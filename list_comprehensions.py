# List comprehensions
# the i**3 is the rule
cubes = [i**3 for i in range(10)]
print(cubes)

# List comprehensions can also contain an if statement to enforce a condition on value in the list
evens = [i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

#Trying to create a list in a very extensive range will result in a MemoryError
# even = [2*1 for i in range(10*100)]
# this issue is solved by generators