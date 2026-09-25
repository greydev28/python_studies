players = [
    {"name": "Daniel", "age": 22, "goals": 15, "assists": 2},
    {"name": "Ibrahim", "age": 23, "goals": 5, "assists": 11},
    {"name": "James", "age": 17, "goals": 2, "assists": 4},
    
]

'''def sort_players(players,keyfunction):
  return keyfunction(players)

def goals_key(players):
    players.sort(key= lambda player:player["goals"])
    return players

def assists_key(players):
   return sorted(players,key= lambda player:player["assists"] ,reverse=True)

def youngest_key(players):
   return sorted(players,key= lambda player:player["age"])

print(sort_players(players,goals_key))
print(sort_players(players,assists_key))
print(sort_players(players,youngest_key))'''

goals_key = sorted(players,key= lambda player:player["goals"])
print(goals_key)
assists_key = sorted(players,key= lambda player:player["assists"] ,reverse=True)
print(assists_key)  
youngest_key = sorted(players,key= lambda player:player["age"]) 
print(youngest_key)


#debugging 
def add_player(player,squad=None):
  if squad is None:
    squad = []
  squad.append(player)
  return squad
print(add_player({"name": "John", "age": 20, "goals": 10, "assists": 5},players))

def multiply(x):
    return x * 2

def calculate(func, value):
    return func(value)

print(
    calculate(multiply, 8)
)