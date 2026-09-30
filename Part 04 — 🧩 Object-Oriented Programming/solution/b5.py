class Book:
    def __init__(self,name):
         self.name = name
    def __str__(self):
         return f'Name: {self.name}'
book = Book("grey")
print(book)

class Playlist:
     def __init__(self):
          self.player = ["wizkid","davido"]

     def __str__(self):
          return f"{self.player}"

     def __len__(self):
          return len(self.player)
     def __eq__(self,other):
          return self.name == other.name
music = Playlist()
print(len(music))

class FootballTeam:
     def __init__(self,team_name):
          self.team_name = team_name
          self.players = []
     def add(self,name):
          self.players.append(name)
     def __str__(self):
          return f"Team {self.team_name} with {len(self.players)} players"

     def __len__(self):
          return (len(self.players))
my_team = FootballTeam("grey")
my_team.add("tony")
my_team.add("chris")
my_team.add("ranking")
print(len(my_team))
print(my_team)


my_team2 = FootballTeam("football")
print(my_team2.team_name)
my_team2.add("tony")
my_team2.add("chris")
my_team2.add("ranking")
print(len(my_team2))


class Book:

    def __str__(self):

        return "Python"

book = Book()

print(book)