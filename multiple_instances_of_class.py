# https://www.youtube.com/watch?v=8DvywoWv6fI&t=6354s

class PartyAnimal:
    name = ""
    x = 0
    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")
    
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()
s.party()
j.party()
