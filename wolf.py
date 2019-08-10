"""
This script serve as the backend logic for the game, its meant to carry the first night but may be extended
"""

import random
import wolf_cli as wc

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
        self.game_roles = {} # Populated only after game starts
        # Randomly assign characters.
        self.assign_role()
        
    def assign_role(self):
        roles = ["WOLF"] * self.wolf_count + ["VILLAGER"] * self.villager_count +\
            ["HUNT"] * self.hunt + ["WITCH"] * self.witch + ["IDIOT"] * self.idiot +\
            ["PERCEIVAL"]
        random.shuffle(roles)
        self.roles = roles
        self.players = [[role, ""] for role in self.roles]

    def take_seat(self, uid, index):
        # Return false when role has been taken.
        if self.players[index][1]:
            return False, ""
        self.players[index][1] = uid
        return True, self.roles[index]

    def who_sits_here(self, index):
        if self.players[index][1]:
            return self.players[index][1]
        return False

    def unseat(self, index):
        if self.START_FLAG: # Cannot unseat after you started
            return False
        self.players[index][1] = ""
        return True

    def start_game(self):
        if all(e[1] for e in self.players):
            self.START_FLAG = True
            self.game_roles = {e[1]: e[0] for e in self.players}
            wc.wolf_start()
            return True
        return False

    def set_kill(self, index):
        if index >= self.total_player:
            return False
        self.killed = index
        self.WOLF_FLAG = True
        wc.perceival_start()
        return True

    def predict(self, index):
        if index >= self.total_player:
            return False
        self.PREDICT_FLAG = True
        wc.witch_start()
        return self.roles[index]

    def get_kill(self):
        return self.killed
        
    def cure(self, action):
        if action:
            self.killed = -1
        self.CURE_FLAG = True   
        wc.end_night()

    def result(self):
        wc.announce_result(self.killed)

