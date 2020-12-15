import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    
    def setRadiu(self, radius):
        self.__radius = radius
    
    def getRadius(self):
        return self.__radius
    
    def area(self):
        return math.pi * self.__radius ** 2
    
    #overloading the + operator
    def __add__(self, circle_object): #we want to add radius of the 2 object
        return Circle(self.__radius + circle_object.__radius)
    
    #overloading < less than operator
    def __lt__(self, circle_object): #we want to add radius of the 2 object
        return (self.__radius < circle_object.__radius)
    #overloading > greater than operator
    def __gt__(self, circle_object): #we want to add radius of the 2 object
        return (self.__radius > circle_object.__radius)
    
    def __str__(self):
        return "Circle area = " + str(self.area()) + " square units"
#Python Operator Overloading will show the full list of the associated functions/methods that we need to implement

c1 = Circle(2)
c2 = Circle(3)

c3 = c1 + c2
print(c1.getRadius())
print(c2.getRadius())
print(c3.getRadius())
print(c1<c2)
print(c3>c2)
print(str(c3))
