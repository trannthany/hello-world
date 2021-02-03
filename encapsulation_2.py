# encapsulation is data hiding which hide details of a class and provide a clean standard interface for those who want to use the class
# Python encapsulation concept is different, there is no arbitrary restrictions on accessing part of a class
# However, there are ways to dicourage people from accessing parts of class (mostly Python relies on people's integrity)
# Python private method is a method that external code is discouraged from using

# Private methods and attributes have a single underscore are weakly inforced
# This means that it does not stop external code from accessing them
# It only prevents "from module_name import *" from importing variables that start with a single underscore

# Strongly private methods and attributes have a double underscore at the beginning of their names
# This means that they cannot be accessed from outside the class
# The purpose of this is to prevent bugs if there are subclasses that have methods or attributes with the same names

class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)
    
    def push(self, value):
        self._hiddenlist.insert(0, value)
    
    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Qeuue({})".format(self._hiddenlist)

class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)


queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)
print(queue.__repr__())

s = Spam()
s.print_egg()
print(s._Spam__egg) # this is how we access the __egg inside the Spam class object_name._Spam__egg
#print(s.__egg) this will throw a traceback, we cannot access __egg this way