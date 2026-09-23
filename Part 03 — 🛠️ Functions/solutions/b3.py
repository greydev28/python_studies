#lambda function that thriple a number
tripple_number = lambda x:x**3
print(tripple_number(3))

#lambda function for even number
is_even = lambda x:x % 2 == 0 
print(is_even(2))
#function anotation
def sum_number(a: int, b: int) ->int:
    return a + b
print(sum_number(2,4))

#sort 

players = [
    ("ada",4),
    ("grey",10),
    ("grace",9),
    ("linus",6)
]

x= sorted(players, key=lambda player:player[1] )
print(x)


#create function that add value twice

def double(value):
    return value * 2
def another_func(func,value):
    return func(value)
x = another_func(double,2)
print(x)


players_profile =[
    {"name": "grey", "position": 10, "goals": 10,"age": 29,"assist": 10},
    {"name": "moses", "position": 11, "goals": 2,"age": 30,"assist": 7},
    {"name": "lucky", "position": 15, "goals": 4,"age": 19,"assist": 6},
    {"name": "ada", "position": 12, "goals": 3,"age": 27,"assist": 5},
    {"name": "wizkid", "position": 18, "goals": 6,"age": 28, "assist": 4},
    {"name": "davido", "position": 7, "goals": 1,"age": 32, "assist": 11},
    {"name": "slyvester", "position": 13, "goals": 5,"age": 34,"assist": 3}
]

'''def clean_name(name):
    return name.strip().lower()

def add_players_details():
    name = input("entere scorer name? ")
    clean_scorer_name = clean_name(name)
    position = int(input("enter player position? "))
    asists_name = input("enter assist name? ")
    assist_name = clean_name(asists_name)
    age = int(input("enter age "))
    goals_scored = int(input("enter number goals? "))
    number_assist = int(input("enter number of asist? "))
    for player in players_profile:
        if player['goals'] > 1:
            player['goals'] += 1
        elif assist_name > 1:
            player['number_assist'] += 1
    players_profile.append({
            "name": clean_scorer_name,
            "position": position,
            "assists" : assist_name,
            "number_assist": number_assist,
            "age" : age,
            "goals": goals_scored
        })
    return players_profile

profile = add_players_details
print(profile())'''

sorted_by_goals = sorted(players_profile,key=lambda player: player['goals'])
sort_by_number_assist = sorted(players_profile,key=lambda player:player['assist'])
sort_by_age = sorted(players_profile, key=lambda player:player['age'])


def main():
  while True:
      print("======what you do want?====")
      print("1==== sort by goals")
      print("2==== sort by asists")
      print("3==== sort by age")

      choice = input("make your choice? ")
      if  choice not in ("1","2","3"):
          return None
      if choice == "1":
          print(sorted_by_goals)
      if choice == "2":
          print(sort_by_number_assist)
      if choice == "3":
          print(sort_by_age)

main()