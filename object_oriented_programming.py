#https://www.youtube.com/watch?v=8DvywoWv6fI&t=6354s
# a sample class
class PartyAnimal:
    x = 0 #data
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal() # instanciate an object
an.party()
an.party()
an.party()

# dir() and type() allows to inspect the object
print(dir(an))
print(type(an))