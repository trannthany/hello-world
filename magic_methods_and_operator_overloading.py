# Magic methods are special methods which have double underscores at the beginning and end of their names
# They are also know as dunders
# e.g. of a magic method (dunder) __init__ , whihc is a magic method creating an instance
# One common use of them is operator overloading
# Operator overloading allow operator such as + and * to be used on them
# An example magic method is __add__ for +

import random

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

class SpecialString:
    def __init__(self, cont):
        self.cont = cont
    
    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])
    
    def __gt__(self, other):
        for index in range(len(other.cont) + 1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)


first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)

# More magic methods for common operators:
# __sub__ for -
# __mul__ for *
# __truediv__ for /
# __floordiv__ for //
# __mod__ for %
# __pow__ for **
# __and__ for &
# __xor__ for ^
# __or__ for |
# __lt__ for <
# __le__ for <=
# __eq__ for ==
# __ne__ for !=
# __gt__ for >
# __ge__ for >=
# if the __ne__ is not implemented, it returns the opposite of __eq__


spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam/hello)
eggs = SpecialString("eggs")
spam > eggs

# There are several magic methods for making classes act like containers
# __len__ for len()
# __getitem__ for indexing
# __setitem__ for assigning to indexed values
# __delitem__ for deleting indexed values
# __iter__ for iteration over objects (e.g. in for loops)
# __contains__ for in

class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]
    
    def __len__(self):
        return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])