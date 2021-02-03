# Properties provide a way of customizing access to instance attributes
# They are created by putting the property decorator above a method,
# this means when the instance attribute with the same name as the method is accessed, the method will called instead
# One common use of a property is to make an attribute read-only

# Properties can also be set by defining setter/getter functions
# The setter function sets the corresponding property's value
# The getter gets the value
# To define a setter, I need to use a decorator of the same name as the property, followed by a dot and the setter keyword
# The same applies to defining getter functions


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False
    
    @property
    def pineapple_allowed(self): # is this a getter?
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "Ssss":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")
    # @pineapple_allowed.getter
    # def pineapple_allowed(self)
    #     return 

    # @property
    # def pineapple_allowed(self):
    #     return False
    
    
    
    
class Person:
    def __init__(self, age):
        self.age = int(age)
    
    @property
    def isAdult(self):
        if self.age > 18:
            return True
        else:
            return False






person = Person("26")
print(person.isAdult)

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)

# this throws a traceback, we cannot set any value to it
# but now we have set a setter then it will work fine
pizza.pineapple_allowed = True
 
print(pizza.pineapple_allowed)