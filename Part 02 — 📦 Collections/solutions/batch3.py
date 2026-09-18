#practice
#easy

favourite_player = {
    "name": "saka",
    "club": "Arsenal",
    "position": 10
}

print(favourite_player["name"])
print(favourite_player["club"])
print(favourite_player["position"])

#MEDIUM

book = {
    "title": "deep work",
    "author" : "cal newport",
    "pages" : 304,
    "year" : 2016
}

print(book["title"])
print(book["author"])
print(book["pages"])
print(book["year"])

student = {

}
student["james"] = 100
student["greydev"] = 100
student["jane"] = 70
student["vincent"] = 90
student["prince"] = 60
student["newport"] = 50

print(student)

#hard 

academy = {
    "player1":{
        "name" : "saka",
        "position" : 10,
        "goals" : 200
    },
    "player2":{
            "name" : "odegard",
            "position" : 11,
            "goals" : 50
    }
}

academy["player3"] = {
    "name" : "raya",
    "position" : 22,
    "goals" : 0
}

for name, value in academy["player1"].items():
    print(name,value)

print(academy)
print(academy[0])
    
