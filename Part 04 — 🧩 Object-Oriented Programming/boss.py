class FootballAcademy:
    def __init__(self):
        self.academy = []
    def add(self,players):
        self.academy.append(players)

class Players(FootballAcademy):
    def __init__(self,name,position,age):
       self.name = name
       self.position = position
       self.age = age
       self.players = []
    def add(self):
        pass
class Goalkeeper(Players):
    pass
class Defender(Players):
    pass
class Midfielder(Players):
    pass