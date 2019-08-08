import random

class WolfGame:

    def __init__(self, wolf_count=4, villager_count=4, hunt=1, witch=1, idiot=1):
        self.total_player = wolf_count + villager_count + hunt + witch + idiot + 1
        self.wolf_count = wolf_count
        self.villager_count = villager_count
        self.hunt = hunt
        self.witch = witch
        self.idiot = idiot
        self.START_FLAG = False
        self.WOLF_FLAG = False
        self.PREDICT_FLAG = False
        self.CURE_FLAG = False
        self.killed = -1 # Nobody

        # Randomly assign characters.
        self.assign_role()
        
    def assign_role(self)
        roles = ["WOLF"] * self.wolf_count + ["VILLAGER"] * self.villager_count +\
            ["HUNT"] * self.hunt + ["WITCH"] * self.witch + ["IDIOT"] * self.idiot +\
            ["PERCEIVAL"]
        random.shuffle(roles)
        self.roles = roles
        self.players = [[role, ""] for role in self.roles]

    def take_seat(self, uid, index):
        self.players[index][1] = uid

    def startable(self):
        if all(e[1] for e in self.players):
            self.START_FLAG = True
            return True
        return False

    def set_kill(self, index):
        self.killed = index
        self.WOLF_FLAG = True

    def predict(self, index):
        self.PREDICT_FLAG = True
        return self.roles[index]

    def get_kill(self):
        return self.killed
        
    def cure(self, action):
        if action:
            if not self.killed < 0:
                self.killed = -1
        self.CURE_FLAG = True   
            
