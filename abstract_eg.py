from abc import ABC, abstractmethod

#ABC is Abstract Base Class
class Shape(ABC): #Shape inherits from abc module
    @abstractmethod #abstractmethod decorator make the function below abstract
    def area(self): pass
    @abstractmethod #abstractmethod decorator make the function below abstract
    def perimeter(self): pass

class Square(Shape):
    def __init__(self, side):
        self.__side = side
    
    def area(self):
        return self.__side * self.__side
    
    def perimeter(self):
        return self.__side * 4


#shape = Shape() #the abc module prevents a declared abstract class from instantiating

sq = Square(4)
print(sq.area())
print(sq.perimeter())