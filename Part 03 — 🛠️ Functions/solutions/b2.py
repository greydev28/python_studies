
def maximum(*args):
    maximum_number = args[0]
    for i in args:
        if i > maximum_number:
            maximum_number = i
    return maximum_number


maximum_number = maximum(1,2,3,4,5,6,7,7,9)
print(maximum_number)

def greet(name="friend"):
    return f'goodmorning  {name}'

print(greet())


def exams_scores(*args):
    total_score = 0
    total_student = len(args)
    for arg in args:
        total_score += arg
    average_score = total_score/total_student
    return average_score
average = exams_scores(78,76,46,25,57)
print(average)

def player_profile(**kwargs):
    player_details = []
    player_details.append(kwargs)
    return player_details

player_details = player_profile(name = "grey",age = 29,profession = "Ai engineer")


player_details = player_profile(name = "john",age = 25,profession = "Ai engineer")
print(player_details)

users = []


def passwordvalidator(password:str)->str:
   if password == "":
       print("invalid password")
       return False
   if len(password) < 8:
       return False,"character must be equal to 8"
   has_letter = any(char.isalpha() for char in password)
   has_number = any(char.isdigit() for char in password)
   if not (has_number and has_letter):
       return False,"please enter a valid password"
   return True,"password valid"

print(passwordvalidator("abadkgsh23ssgs"))



def create_account():
    username = input("enter fullname ")
    clean_name = username.strip().lower()
    password = input("enter password 8 characters")
    passwordvalidator(password)
    for user in users:
        if  user["name"] in users:
            print("sorry user already")
            return login()
    users.append({"name":clean_name,"password":password})
    return users
users = create_account()
print(users)


