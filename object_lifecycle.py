# the lifecycle of an object is made up of its creation, manipulations and destruction
# the first stage of the life-cycle of an object is the definition of the class to which it belongs
# the next stage is the instantiation of an instance, when __init__ is called
# Memory is allocated to store the instance
# just before this occurs, the __new__ method of the class is called. This is usually overridden only in the special cases
# Eventually, when an object is finished being used, it get destroyed
# The destruction of an object occurs when its reference count reaches zero
# the del statement reduces the reference count of an object by one, and this often leads to its deletion
# the magic method method for the del statement is __del__
# The process of deleting objects when they are no longer needed is called garbage collection

a = 42 # create object <42>
b = a # increase ref. count of <42>
c = [a] # increase ref. cout of <42>

del a # decrease ref. count of <42>
b = 100 # decrease ref. count of <42>
c[0] = -1 # decrease ref. count of <42>