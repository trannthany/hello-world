from polygon import Polygon
#from the file name, import "the class", you can import multiple class if there are more in the files
class Triangle(Polygon):
    def area(self):
        return self.get_height() * self.get_width() /2