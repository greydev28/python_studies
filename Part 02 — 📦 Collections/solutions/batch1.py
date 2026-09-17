players = [
    "James",
    "David",
    "Musa",
    "Ibrahim",
    "Samuel"
]
'''count = 0
print(players)
players.append("grey")
players.remove("James")
print(players)
for player in players:
    count+=1
print(count)'''
#first squad
def first_squad():
    
     for player in players:
          print(player)
          
     
def add_player(name):
     players.append(name)
def remove_player(name):
     players.remove(name)
def count_player():
     print(len(players))

add_player("james")
remove_player("David")
first_squad()
count_player()


food_list = ["rice","beans","egg","fruit","garri"]
print(food_list)
print(food_list[0])
print(food_list[-1])
food_list[0] = "vegetable"
print(food_list)

squad_manager= []
def add_to_squad_manager(name):
    if name not in squad_manager:
            squad_manager.append(name)
            print(f"{name} - added successfully")
    else:
         print(f'{name} already exist')
def remove_from_squad_manager(name):
    if name in squad_manager:
        squad_manager.remove(name)
        print(f'{name} has be removed')
    else:
        print(f'{name} could be found sorry!')
def counter():
     return len(squad_manager)
def show_squad():
     if not squad_manager:
          print("squad list is empty")
     for player in squad_manager:
            print(player)
    
def show_menu():
     print("1 add new player")
     print("2 remove player")
     print("3 show quad")
     print("4 count players")
     print("5 exit")


def main():
     while True:
          show_menu()
          choice = input("please make enter a choice?  ")
          if choice == "1":
               name = input("what your name? ")
               cleaned_name = name.lower().strip()
               if cleaned_name:    
                  add_to_squad_manager(cleaned_name)
          elif choice == "2":
               name = input("what name do you want remove")
               cleaned_name = name.lower().strip()
               remove_from_squad_manager(cleaned_name)
          elif choice == "3":
               print("=== current squad ===")
               show_squad()
               print("=====================")
          elif choice == "4":
               print(f'total player: {counter()}')
          elif choice == "5":
               print("have a great day!")
               break
main()
          

