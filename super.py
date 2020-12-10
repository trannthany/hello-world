class Parent:
    def __init__(self, name):
        print('Parent __init__', name)

class Parent2:
    def __init__(self, name):
        print('Parent2 __init__', name)


class Child(Parent, Parent2):
    def __init__(self):
        print('Child __init__')
        #super().__init__("Max") this for only one inheritance (only one super class), super allow child class to call its parent class's constructor
        
        # for multiple super classe inheritances 
        Parent.__init__(self, "Thany") #this requires to prove self in the parameter
        Parent2.__init__(self, "Laura")


child = Child()

#the super() allows us to refer to the super class

#__mro__ is a method resolution order show the order of the method are called in the Child class

print(Child.__mro__)