# Inheritance provides a way to share functionality between classes

# A class that is inherited from is called a superclass
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

# A class that inherits from another class is called a subclass
class Cat(Animal):
    def purr(self):
        print("Puuuuuuurrrrrr.....")

class Dog(Animal):
    def bark(self):
        print("Woof!")

# Inheritance can also be indirect, one class can inherit from another, and that class can inherit from a third class
# The function super is a useful inheritance-related function that refers to the parent class, 
# The function super can be used to find the method with a certain name in an object's superclass
class Golden_Retriever(Dog):
    def smile(self):
        print(":)")
    def bark(self):
        #print("wung!")
        super().bark()


fido = Dog("Fido", "Brown")
print(fido.color)
fido.bark()

pirate = Golden_Retriever("Pirate", "Ginger")
print(pirate.color)
pirate.bark()
pirate.smile()