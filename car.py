class Car:
    pass #pass is used to declare an empty class or function

ford = Car()
honda = Car()
audi = Car()

#class's attribute, the class attributes can be added on the flight as long the class has been declared empty.
ford.speed = 200
honda.speed = 220
audi.speed = 250

ford.color = 'red'
honda.color = 'blue'
audi.color = 'black'

print(ford.speed)
print(ford.color)