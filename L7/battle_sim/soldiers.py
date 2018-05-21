#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unit_abc import Unit
from random import randint
# from time import time


class Soldier(Unit):
    def __init__(self, name, health, unit_type):
        self.name = name
        self._health = health
        self.unit_type = unit_type
        self.experience = 0
        self.recharge = 100

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health -= value

    def attack_prob(self):
        success_prob = (
            0.5 * (1 + self.health / 100) *
            randint(50 + self.experience, 100) / 100
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