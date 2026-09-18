#debugging

# 🐞 Debugging Lab


player = (
    "James",
    22,
    "CDM"
)

#player.append("Captain")
#this will throw an AttrobutError because this a tuples... its item can't be modified

#practice
#easy

five_colours = ("red","blue","green","black","gray")
print(five_colours[1])
print(five_colours[-1])
print(len(five_colours))

#medium

player = ("grey",22,10)

name,age,position = player
print(name)
print(age)
print(position)


def rectangle(length,width):
    area = length * width
    perimeter = 2 * (length  + width)
    return area, perimeter

area, perimeter = rectangle(2,4)
print(area)
print(perimeter)

#hard

def student_result(*args):
    highest = args[0]
    lowest = args[0]
    total_count = 0
    average = None
    for i in args:
        if i > highest:
            highest = i
        elif i < lowest:
            lowest = i
        total_count += i
        print(f'total:{total_count}')
    average = total_count/len(args)
    return average,highest,lowest
average,highest,lowest = student_result(1,3,4,5,6,7,7,8)
print(average)
print(highest)

def match_summary(home_goals, away_goals):
    goal_difference = None
    winner = ""
    if home_goals > away_goals:
        winner = 'the winner "HOME"'
        goal_difference = home_goals - away_goals
    elif home_goals < away_goals:
          winner = 'the winner "away"'
          goal_difference = away_goals - home_goals
    else:
       winner = "Draw"
       goal_difference = away_goals - home_goals
    total_goals = home_goals + away_goals
    return winner,total_goals,goal_difference 

winner,total_goals,goal_difference = match_summary(3,3)
print(winner)
print(total_goals)
print(goal_difference)
  