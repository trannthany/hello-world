from rectangle import Rectangle
from triangle import Triangle
#from the file name, import "the class", you can import multiple class if there are more in the files
rect = Rectangle()
tri = Triangle()

rect.set_values(25, 4)
tri.set_values(25, 4)

print(rect.area())
print(tri.area())

rect.set_color('red')
print(rect.get_color())