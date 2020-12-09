class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
    
    #get and set are ways to access and change the class attributes which are encapsulated
    def set_speed(self, value):
        self.speed = value

    def get_speed(self):
        return self.speed



class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20
        self.__c = 30
        self.__name = name

    def set_name(self, value):
        self.__name = value

    def get_name(self):
        return self.__name



ford = Car(100, 'blue')
ford.speed = 'djslkdfjsdjf'
#therefor we need encapsulation, we don't want anyone to get a direct access into the class attributes and mess it up

hello = Hello('thany')
print(hello.a)
print(hello._b) # _b is a partial private attribute, it doesn't prevent direct access but the python programmers know and respect it
#print(hello.__c) this throw an AttributeError because __c is a true private attribute which prevents a direct access

hello.__name = 'Jonathan' #even though it does throw an error, this preven __name attribute get changed directly
print(hello.get_name())

hello.set_name('Jonathan') #the attrubutes can be change via a set method
print(hello.get_name())