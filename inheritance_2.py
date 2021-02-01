# https://www.youtube.com/watch?v=8DvywoWv6fI&t=6354s
# inheritance makes a new class and reuse an existing class and inherit all the capabilities

class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, nam):
        self.name= nam
        print(self.name, "constructed")
    
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)
    
class FootballFan(PartyAnimal):
    scores = 0
    def score_goal(self):
        self.scores = self.scores + 1
        self.party()
        print(self.name, "scores", self.scores)

s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.score_goal()