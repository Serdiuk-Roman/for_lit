#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unit_abc import Unit
from random import randint
# from time import time


class Soldier(Unit):
    def __init__(self, name, health, unit_type, clock):
        self.clock = clock
        self.name = name
        self._health = health
        self.unit_type = unit_type
        self.experience = 0  # 0 - 50
        self.recharge = randint(100, 200)
        self.end_recharge_time = 0

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = max(self._health - value, 0)

    def attack_prob(self):
        success_prob = (
            0.5 * (1 + self.health / 100) *
            randint(round(50 + self.experience), 100) / 100
        )
        return success_prob

    @property
    def damage(self):
        return 0.05 + self.experience / 100

    def is_alive(self):
        return self.health > 0

    def start_recharge(self):
        self.end_recharge_time = self.clock.time() + self.recharge

    def is_active(self):
        return self.clock.time() > self.end_recharge_time

    def level_up(self):
        # print("soldat_exp ", self.experience)
        if self.experience > 50:
            return
        self.experience += 0.1


if __name__ == '__main__':
    pass
