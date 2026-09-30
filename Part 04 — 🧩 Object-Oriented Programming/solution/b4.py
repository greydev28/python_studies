#debugging lab

class Animal:
    def __init__(self,name):
        self.name = name

    def move(self):
        print(f'{self.name} is moving')

class Bird(Animal):
    def __init___(self,name):
        super().__init__(name)

    def move(self):
        print(f'{self.name} flies')

bird = Bird("bird")
bird.move()


class Employee:
    def __init__(self,name):
        self.name = name

    def work(self):
       print("we team of developers")

class Developer(Employee):
    def __init__(self,name):
        super().__init__(name)
    def work(self):
        print(f"name:{self.name} is a python developer")

class Designer(Employee):
    def __init__(self,name):
        super().__init__(name)
    def work(self):
        print(f"{self.name} is designer")

class Project_manager(Employee):
    def __init__(self,name):
        super().__init__(name)
    def work(self):
        print(f'{self.name} is product manager')

class Tester(Employee):
    def __init__(self, name):
        super().__init__(name)
    def work(self):
        print(f'{self.name} is a tester')

developer = Developer("greydev")
projectmanager = Project_manager("miracle")
designer = Designer("OBETECH")

Employees = [
    developer,projectmanager,designer
]
for employee in Employees:
    employee.work()

#hard and last

class Player:
    def __init__(self,name):
        self.name = name
    def play(self):
        print("team of players")

class Goalkeeper(Player):
    def __init__(self,name):
        super().__init__(name)
    def play(self):
        print(f'{self.name} is goalkeeper')
class Defender(Player):
    def __init__(self, name):
        super().__init__(name)
    def play(self):
        print(f'{self.name} is a defender')
class Midfielder(Player):
    def __init__(self, name):
        super().__init__(name)
    def play(self):
        print(f'{self.name} is a midfielder')

class Forward(Player):
    def __init__(self, name):
        super().__init__(name)
    def play(self):
        print(f'{self.name} is a forward')

goalkeeper = Goalkeeper("toni-cruz")
defender = Defender("saliba")
midfielder = Midfielder("messi")
forward = Forward("saka")

players = [
    goalkeeper,
    defender,
    midfielder,
    forward
]

for player in players:
    player.play()