five_colour = {
    "red",
    "white",
    "blue",
    "green",
    "gray"
}

dictionary_item = {}

def add_to_set(color):
    for color in five_colour:
        if color not in five_colour:
             five_colour.add(color)
             print(f'{color} has been added succefully')
        else:
            print(f'{color} - already')
            return
           

def remove_from_set(color):
    for color in five_colour:
        if color in five_colour:
            five_colour.remove(color)
        else:
            print(f'{color} - jotfound')

def convert_to_dict():
    for color in five_colour:
        if color not in dictionary_item:
            dictionary_item[color] = 1
        else:
            dictionary_item[color]+=1

def show_menu():
    print("1... add a color")
    print("2... remove a color")
    print("3... comvert to dictionary")
    print("4... stop")

def main():
    while True:
        show_menu()
        choice = input("what do you want? ")

        if choice == "1":
            enter_color = input("please enter the color  ")
            add_to_set(enter_color)
        elif choice == "2":
            enter_color = input("please enter the color  ")
            remove_from_set(enter_color)
        elif choice == "3":
            print(convert_to_dict())
        elif choice == "4":
            print("thanks for your time")
            break
main()


