class Polygon:
    __width = None
    __height = None

    def set_values (self, width, height):
        self.__width = width
        self.__height = height
    
    def get_width(self):
        return self.__width
    
    def get_height(self):
        return self.__height

class Rectangle(Polygon):
    def area(self):
        return self.get_height() * self.get_width()

class Triangle(Polygon): #The Triangle class is heriting from the Polygon class
    def area(self):
        return self.get_height() * self.get_width() /2

rect = Rectangle()
tri = Triangle()

rect.set_values(25, 4)
tri.set_values(25, 4)

print(rect.area())
print(tri.area())