#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    
"""

from unit_abc import Unit
from soldiers import Soldier
# from random import random, randint


class Vehicle(Unit):

    def __init__(self, name, health, unit_type, operators):
        self.name = name
        self._health = health
        self.unit_type = unit_type
        self.experience = 0.01
        self.recharge = 100
        self.operators = []
        for operator in operators:
            self.operators.append(Soldier(
                operator["name"],
                operator["health"],
                operator["unit_type"]
            ))

    def add_operator(self, soldier):
        self.operators.append(soldier)

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health -= value * 0.6

    def is_alive(self):
        if not self.health:
            for soldier in self.operators:
                soldier.health = 0
            return False
        else:
            for soldier in self.operators:
                return soldier.is_alive()
        return False

    def attack_prob(self):
        # ganv_op = gavg(operators.attack_success)
        multiplication = 1
        for soldier in self.operators:
            multiplication *= soldier.attack_prob()
        ganv_op = pow(multiplication, 1 / len(self.operators))
        success_prob = 0.5 * (1 + self.health / 100) * ganv_op
        return success_prob

    def damage(self):
        oper_exp = [
            soldier.experience / 100
            for soldier in self.operators
        ]
        return 0.1 + sum(oper_exp)
