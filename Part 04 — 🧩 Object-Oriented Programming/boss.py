class FootballAcademy:
    def __init__(self,name):
        self.name = name
        self.academy = []
    def add(self,players):
        self.academy.append(players)
    def total_player(self):
        return len(self.academy)
    def remove(self,player_name):
        self.academy = [player for player in self.academy if player.name != player_name]
        return self.academy
    def display(self):
        for player in self.academy:
            print(f"name => {player['name']}")
            print(f"position => {player['position']}")
            print(f"Age => {player['Age']}")
            if "save" in player: print(f'save => {player['save']}')
            if "shot_block" in player: print(f"shot_block => {player['shot_block']}")
            if "through_pass" in player: print(f"through_pass => {player['through_pass']}")
            if "finish_chance" in player: print(f"finish_chance =>{player['finish_chance']}")

class Players(FootballAcademy):
    def __init__(self,name,position,age):
       self.name = name
       self.position = position
       self.age = age
    def __str__(self):
        return 'f{self.name}-{self.position}'
    def add(self):
        self.academy.append({
            "name": self.name,
            "position" : self.position,
            "Age": self.age
        }
        )
        return self.academy
   
    def train(self):
        return f'{self.name}-{self.
        position} is training with team'
    def play(self):
        return f'{self.name}-{self.position} is playing with the team'

    
class Goalkeeper(Players):
    def __init__(self, name, position, age):
        super().__init__(name, position, age)
        self.save = 0
    def save_panalty(self):
        self.save+= 1
    def add(self):
        self.academy.append({
            "name": self.name,
            "position" : self.position,
            "Age": self.age,
            "save": self.save
        }
        )
        return self.academy
class Defender(Players):
    def __init__(self, name, position, age):
        super().__init__(name, position, age)
        self.shot = 0
    def block_shot(self):
        self.shot += 1
    def add(self):
        self.academy.append({
            "name": self.name,
            "position" : self.position,
            "Age": self.age,
            "shot_block": self.shot
        }
        )
        return self.players

class Midfielder(Players):
    def __init__(self, name, position, age):
        super().__init__(name, position, age)
        self.p_ass =0
    def through_pass(self):
        self.p_ass +=1
    def add(self):
        self.academy.append({
            "name": self.name,
            "position" : self.position,
            "Age": self.age,
            "through_pass": self.p_ass
        })
        return self.academy

class Forward(Players):
    def __init__(self, name, position, age):
        super().__init__(name, position, age)
        self.fini_shchance = 0
    def finish_chance(self):
        self.fini_shchance +=1
    def add(self):
        self.academy.append({
            "name": self.name,
            "position" : self.position,
            "Age": self.age,
            "finsih_chance": self.fini_shchance
        })
        return self.academy   
grey = Midfielder("grey","mf",29)
ben = Goalkeeper("ben","gk",21)
tony = Defender("tony","df",22)
chris = Forward("chris","fw",23)

ben.save_panalty()
grey.through_pass()
tony.block_shot()
tony.block_shot()
tony.block_shot()
chris.finish_chance()


ai_academy = FootballAcademy("ai academy")
ai_academy.add(grey)
ai_academy.add(ben)
ai_academy.add(tony)
ai_academy.add(chris)
ai_academy.remove("grey")
print(ai_academy.total_player())

