# Class methods are different methods of objects
# Methods of objects are called by an instance of a class which is then passed to the self parameter of the method
# Class methods are called by a class which is passed to the cls parameter of the method
# Class methods are used as factory methods, which instantiate an instance of a class using different parameters than those usually passed to the clas constructor
# Class methods are marked with a classmethod decorator
# Technically the parameter self and cls are just convention; they could be changed to anything else
# self and cls are universally followed so it is wise to stick to using them
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    
    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)

# Static methods are similar to class methods, except they don't receive any additional arguments
# They are identical to normal functions that belong to a class
# They are marked with the staticmethod decorator

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
    
    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True



print("################")
square = Rectangle.new_square(5)
print(square.calculate_area())
rect = Rectangle(5, 10)
print(rect.calculate_area())
print("################")
ingredients = ["cheese", "onions", "spam", "pineapple", "Salami"]
if all(Pizza.validate_topping(i) for i in ingredients):
    #print(i) throw traceback
    pizza = Pizza(ingredients)
# Static methods behave like a plain functions, except for the fact that you can call them from an instance of the class
print("done")