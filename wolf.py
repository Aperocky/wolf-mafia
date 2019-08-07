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

        # Randomly assign characters.
        self.assign_role()
        
    def assign_role(self)
        roles = ["WOLF"] * self.wolf_count + ["VILLAGER"] * self.villager_count +\
            ["HUNT"] * self.hunt + ["WITCH"] * self.witch + ["IDIOT"] * self.idiot +\
            ["PERCEIVAL"]
        random.shuffle(roles)
        self.roles = roles

    def 
        
