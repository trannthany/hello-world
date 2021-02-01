#https://www.youtube.com/watch?v=8DvywoWv6fI&t=6354s

# constructor (use very rarely)

class PartyAnimal:
    x = 0
    def __init__(self): # this is called when an object is created
        print("I am constructed")

    def __del__(self): # this is called when an object is destroyed
        print("I am destructed", self.x)
    
    def party(self): 
        self.x = self.x + 1
        print('So far', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42 # when an stops pointing to PartyAnimal(), the object gets destroyed
print('an contains', an)