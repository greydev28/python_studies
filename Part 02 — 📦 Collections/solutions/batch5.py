academy_name = "Grey Football Academy system"
academy_location= ("20 omaiye street otukpo",)
academy_players = []
academy_players_position = {10,7,12,14,15}

new_player =  True

'''def student_info(name):
    for name,position in zip(academy_players,academy_players_positon):
        if name not in academy_players_info:
            academy_players_info[name] = position
        else:
            print(f'{name}')
    return academy_players_info'''

def add_Player(name,position):
    if position not in academy_players_position:
                print(f'{position} - not found')
                return
    for player in academy_players:
        if player['position'] == position:
            print("sorry position has taken")
            return
    academy_players.append( {"name":name,"position":position})
    return academy_players
        
def remove_player(name):
    for i, player in enumerate(academy_players):
          if player["name"] == name:
               academy_players.pop(i)        
    return academy_players

def find_player(name):
      for i,player in enumerate(academy_players):
            if player["name"] == name:
                  return academy_players[i]
      return academy_players

def display_squad():
     return academy_players

def count_players():
      return len(academy_players)

def show_available_positions():
      available_positions = []
      taken_position = [player['position'] for player in academy_players]
      for position in academy_players:
            if position in taken_position:
                  continue
            available_positions.append(position)
      return available_positions
                  
                 
add_Player("grey",10)
add_Player("ben",7)
find_player("grey")
print(find_player("ben"))

print(display_squad())
print(count_players())
print(show_available_positions())
    