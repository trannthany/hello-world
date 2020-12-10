from polygon import Polygon
#from the file name, import "the class", you can import multiple class if there are more in the files
from shape import Shape
class Rectangle(Polygon, Shape): #inheritance from multiple classes
    def area(self):
        return self.get_height() * self.get_width()