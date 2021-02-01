# Set is disorder and it is fast for look up
# Set does not allow duplicate

x = set() # empty set

set_literal = {4, 32, 2, 2, 2}

print(set_literal)

print(3 in set_literal)
print(4 in set_literal)

#set is unordered and cannot be indexed and cannot have duplicate elements

set_literal.add(-7)
set_literal.remove(4)
print(set_literal)

# sets can be combined using mathematical operations such as union | , intersection & , difference - , symmetric difference ^
first_set = {1, 2, 3, 4, 5, 6}
second_set = {4, 5, 6, 7, 8, 9}

print(first_set | second_set)
print(first_set & second_set)
print(first_set - second_set)
print(second_set - first_set)
print(first_set ^ second_set)