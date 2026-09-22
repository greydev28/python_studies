academy_name = "Grey Football Academy system"
academy_location= ("20 omaiye street otukpo",)
academy_players = []
academy_players_position = {10,7,12,14,15}



def add_player(name,position):
    if position not in academy_players_position:
                print(f'{position} - not found')
                return
    for player in academy_players:
        if player['position'] == position:
            print("sorry position has taken")
            return
        academy_players.append( {"name":name,"position":position})
        print("registration was successfully")
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
      return "name not found"

def display_squad():
     return academy_players
def count_players():
      return len(academy_players)

def show_available_positions():
      available_positions = []
      taken_position = [player['position'] for player in academy_players]
      for position in academy_players_position:
            if position in taken_position:
                  continue
            available_positions.append(position)
      return available_positions
def menu():
      print("=======show menu=====")
      print("1...add a new player")
      print("2...remove player")
      print("3...find player")
      print("4.... display_squad")
      print("5....  count_player")
      print("6.... show available positions")
      print("7....exit")


def main():
      new_player =  True
      while new_player:
            menu()
            choice = input("what your choice? ")

            if choice == "1":
                  player_name = input("what is your name? ")
                  cleaned_name = player_name.strip().lower()
                  try:
                        player_position = int(input("what position are you interested in? "))
                  except ValueError:
                        print("enter a valid")
                  else:
                        add_player(cleaned_name,player_position)

            elif choice == "2":
                  player_name = input("enter player name ")
                  cleaned_name = player_name.strip().lower()
                  remove_player(cleaned_name)       

            elif choice == "3":
                  player_name = input("enter player name ")
                  cleaned_name = player_name.strip().lower()
                  print(find_player(cleaned_name))

            elif choice == "4":
                  print(display_squad())
            elif choice == "5":
                  print(count_players())
            elif choice == "6":
                  print(show_available_positions())
            else:
                  print("have a nice day")
                  new_player = False
main()