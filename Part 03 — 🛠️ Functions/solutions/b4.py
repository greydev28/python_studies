#football Academy Manager

players = []

def cleaned(name):
  return name.strip().lower()

def add_player():
    username = input("enter fullname? ")
    cleaned_username = cleaned(username)

    unique_position = {10,17,7,8,9,12}
    while True:

      enter_position = int(input("enter prefered position(10,17,7,8,9,12)  "))
      
      if enter_position not in  unique_position:
       return "invalid position"
    
      taken_position = any(player['position'] == enter_position for player in players) 
      if taken_position:
        continue
      break       
    try: 
      age = int(input("enter your age...  "))
    except ValueError:
        return "age not right format"

    if 12 < age > 30:
      return "age not accepted in academy"
    try:
      number_goals = int(input("enter number of goals? "))
      number_assists = int(input("number of assists made? "))
    except ValueError:
      print("enter a valid number")

    if number_assists < 0:
      return False
   
    
    players.append({
        "name": cleaned_username,
        "age":age,
        "position":enter_position,
        "goals": number_goals,
        "assists": number_assists
      })
    return players


def remove_player(name):
  for player in players:
    if player["name"] == name:
      players.remove(player)


def find_player(name):
  player_found = []
  for player in players:
    if player['name'] == name:
      player_found.append(player)
  return player_found

def show_players():
  for player in players:
    print(f'Name: {player["name"]}\nAge: {player["age"]}\nPosition: {player["position"]}\nGoal: {player["goals"]}\nAssists: {player["assists"]}\n')

def count_players():
  return len(players)

def menu():
  print("======student academy======")
  print("1...add player")
  print("2... remove player")
  print("3.... find player")
  print("4.... show players")
  print("5.... count players")
  print("6.... exit")   


def main():
  while True:
    menu()
    choice = input("make a choice ")
    if choice not in {"1","2","3","4","5","6"}:
      return f'{choice}- not available'
    if choice == "1":
      add_player() 
    elif choice == "2":
      enter_player_name = input("search for player with name.... ")
      clean_name = cleaned(enter_player_name)
      remove_player(clean_name)
    elif choice == "3":
       enter_player_name = input("search for player with name.... ")
       clean_name = cleaned(enter_player_name)
       found_player = find_player(clean_name)
       print(found_player)
    elif choice == "4":
       show_players()
    if choice == "5":
      return count_players()
    if choice == "6":
      print("thanks for watching out!!!")
      break

main()
    