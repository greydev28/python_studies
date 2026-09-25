#football Academy Manager

players = [
]



def cleaned(name):
  return name.strip().title()

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
      print("age not accepted in academy")
      return
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

def show_players(players):
  for player in players:
    print(f'Name: {player["name"]}\nAge: {player["age"]}\nPosition: {player["position"]}\nGoal: {player["goals"]}\nAssists: {player["assists"]}\n')

def count_players(players):
  return len(players)

def topscorer(players):
  topscorer_player_container = []
  topscorer_player = players[0]["goals"]
  for player in players:
    if topscorer_player < player["goals"]:
      topscorer_player = player["goals"]
  for player in players:
       if topscorer_player == player["assists"]:
          topscorer_player_container.append(player['name'])
  return topscorer_player_container

def most_assists(players):
  most_assist_container = []
  most_assists_player = players[0]["assists"]
  for player in players:
    if most_assists_player < player["assists"]:
      most_assists_player = player["assists"]
  for player in players:
      if most_assists_player == player["assists"]:
         most_assist_container.append(player['name'])
  return most_assist_container


def youngest_player(players):
  youngest_player_container = []
  youngest_player = players[0]["age"]
  for player in players:
    if player["age"] < youngest_player:
      youngest_player = player["age"]
  for player in players:
    if player["age"] == youngest_player:
      youngest_player_container.append(player['name'])
  return youngest_player_container

def average_age(players):
  total = 0
  total_player = len(players)
  for player in players:
    total += player["age"]
  average = total / total_player
  return average

def average_goals():
  total = 0
  active_goals = 0

  if active_goals == 0:
    return 0.0
  for player in players:
    if player['goals'] > 0:
      active_goals += 1
      total += player["goals"]
  average_goals_scored = total / active_goals
  return average_goals_scored
  

def academy_summary(players):
   print(f"Players: {count_players(players)}\nAverage Age: {average_age(players)}\nTop Scorer: {topscorer(players)}\nMost Assists: {most_assists(players)}\nYoungest: {youngest_player(players)}")
def menu():
  print("======student academy======")
  print("1...add player")
  print("2... remove player")
  print("3.... find player")
  print("4.... show players")
  print("5.... count players")
  print("6....  topscorer")
  print("7.... most assists")
  print("8.... youngest player")
  print("9...  Average age")
  print("10... avarage goals")
  print("11.... academy_summmary")
  print("12.... exit")   
  

def main():
  while True:
    menu()
    choice = input("make a choice ")
    unique_number = {"1","2","3","4","5","6","7","8","9","10","11"}
    if choice not in unique_number :
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
      show_players(players)
    elif choice == "5":
      count_players(players)
    elif choice == "6":
      topscorer(players)
    elif choice == "7":
      most_assists(players)
    elif choice == "8":
      youngest_player(players)
    elif choice == "9":
      average_age(players)
    elif choice == "10":
      average_goals(players)
    elif choice == "11":
      academy_summary(players)
    elif choice == "12":
      print("thanks for checking us out")
      break

      

main()
    