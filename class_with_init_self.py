class Car:
    def __init__(self, speed, color): #this serve as the constructor of the class but it is not a constructor
        print(speed)
        print(color)
        self.speed = speed #self is the same as this in java or C#
        self.color = color
        print('the __init__ is called')

#self arg will be provide by the python, and the self is conventional name for the first argument inside the class

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width


class Hello:
    def __init__(self, *args, **kwargs): 
        #the args take none or more values put in a tuple, the kwargs take none or more key-value pairs
        self.name = 'a static value' # we can provide static value


ford = Car(200, 'red')
honda = Car(201, 'blue')
print(ford.color)
print(ford.speed)

rect1 = Rectangle(25, 4)
rect2 = Rectangle(13, 2)
print(rect1.height * rect1.width)