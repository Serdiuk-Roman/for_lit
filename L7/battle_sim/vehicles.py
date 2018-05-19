from unit_abc import Unit
from random import random, randint


class Vehicle(Unit):

    def __init__(self, name, army):
        self.name = name
        self.army = army
        self.health = randint(range(100, 200))
        self.experience = 0.01
        self.recharge = 100
        self.operators = []

    def add_operator(self, soldier):
        self.operators.append(soldier)

    def health(self):
        pass

    def is_alive(self):
        if not self.health:
            for soldier in self.operators:
                soldier.health = 0
            return False
        else:
            for soldier in self.operators:
                return soldier.is_alive()
        return False

    def attack(self):
        # ganv_op = gavg(operators.attack_success)
        multiplication = 1
        for soldier in self.operators:
            multiplication *= soldier.attack()
        ganv_op = pow(multiplication, 1 / len(self.operators))
        success_prob = 0.5 * (1 + self.health / 100) * ganv_op
        return success_prob

    def damage(self):
        oper_exp = [
            soldier.experience / 100
            for soldier in self.operators
        ]
        return 0.1 + sum(oper_exp)
