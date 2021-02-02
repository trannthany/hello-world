# classes are created using the keyword class
class Cat:
    #legs = 4
    def __init__(self, name, color, legs=4): #constructor
        self.color = color
        self.legs = legs
        self.name = name
        print("you've invoked the Cat's contructor")
    
    def meow(self): #method
        print("Meow == hoomaan!!, bring me food!!")

cat1 = Cat("Felix", "ginger")
cat2 = Cat("Bubble", "dog-colored")
cat3 = Cat("Stumpy", "brown", 3)

# The __init__ method is the constructor, every time you instance an object the __init__ is called
# self is the first parameter and it isn't explicitly passed. Python adds the self argument to the list for you
# the self.color and self.legs are the class attributes to access these attribute you use dot operator

print(cat1.color)
# classes can have other methods must have self as their first parameter and can be assessed by using dot operator
cat1.meow()