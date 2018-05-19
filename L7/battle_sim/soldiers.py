from unit_abc import Unit
from random import random, randint
# from time import time


class Soldier(Unit):
    def __init__(self, name, army):
        self.name = name
        self.army = army
        self.health = randint(range(50, 100))
        self.experience = 0
        self.recharge = 100

    def health(self):
        pass

    def attack(self):
        success_prob = (
            0.5 * (1 + self.health / 100) *
            random(50 + self.experience, 100) / 100
        )
        return success_prob

    def damage(self):
        return 0.05 + self.experience / 100

    def is_alive(self):
        return self.health > 0

    # def recharge(self):
        # bench = False
        # if bench:
        #     return False
        # else:
        #     rech_time 