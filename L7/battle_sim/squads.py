#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    ## Squads
## Команди

Squads are consisted out of a number of units (soldiers or vehicles),
that behave as a coherent group.
Команди складаються з ряду підрозділів (солдатів або транспортних засобів),
які ведуть себе як пов'язана група.

A squad is active as long as is contains an active unit.
Група є активною, якщо вона містить активного юніта.

#### Attack
#### Атака

The attack success probability of a squad is determined
as the geometric average o the attack success probability of each member.
Імовірність успішного удару команди визначається
як геометричний середній показник успіху атаки кожного члена.

#### Damage
#### Пошкодження

The damage received on a successful attack
is distributed evenly to all squad members.
Пошкодження, отримане від успішної атаки,
рівномірно розподіляється серед усіх членів команди.

The damage inflicted on a successful attack
is the accumulation of the damage inflicted by each squad member.
Пошкодження, завдане успішній атаці,
це накопичення пошкодженнь, завданої кожним членом команди.
"""

from random import choice

from unit_abc import Unit
from soldiers import Soldier
from vehicles import Vehicle


class Squad(Unit):
    def __init__(self, name, units):
        self.name = name
        self.units = []
        self._health = None
        for unit in units:
            if unit["unit_type"] == "soldier":
                self.units.append(Soldier(
                    unit["name"],
                    unit["health"],
                    unit["unit_type"],
                ))
            elif unit["unit_type"] == "vehicle":
                self.units.append(Vehicle(
                    unit["name"],
                    unit["health"],
                    unit["unit_type"],
                    unit["operators"]
                ))
        self.strategy = ""
        self.enemies = []
        self.enemy = None

    @property
    def health(self):
        self._health = sum([unit.health for unit in self.units])
        return self._health

    @health.setter
    def health(self, value):
        print("setter", self.enemy.name)
        foo = value / len(self.enemy.units)
        for i in self.enemy.units:
            i.health = foo
        print(self.enemy.health)

    def attack_prob(self):
        multiplication = 1
        for unit in self.units:
            multiplication *= unit.attack_prob()
        success_prob = pow(multiplication, 1 / len(self.units))
        return float(success_prob)

    def attack(self):

        if self.strategy == "random":
            self.enemy = choice(self.enemies)
        elif self.strategy == "weakest":
            self.enemy = min(self.enemies, key=lambda sq: sq.health)
        elif self.strategy == "strongest":
            self.enemy = max(self.enemies, key=lambda sq: sq.health)

        print(self.name, self.strategy, "attack", self.enemy.name)
        print(self.health, "vs", self.enemy.health)
        print(str(self.attack_prob()), ">", str(self.enemy.attack_prob()))
        for i in range(10):
            print(self.attack_prob() > self.enemy.attack_prob())
        if self.attack_prob() > self.enemy.attack_prob():
            print("Good", self.enemy.name)
            self.enemy.health = 100
        else:
            print("wrong")

    def damage(self):
        pass

    @property
    def is_alive(self):
        return sum([unit.alive for unit in self.units]) > 0


if __name__ == '__main__':
    goblins = [
        {
            "name": "trol #1",
            "health": 82,
            "unit_type": "soldier"
        },
        {
            "name": "trol #2",
            "health": 96,
            "unit_type": "soldier"
        },
        {
            "name": "trol #3",
            "health": 56,
            "unit_type": "soldier"
        }
    ]
    elfs = [
        {
            "name": "elf #1",
            "health": 92,
            "unit_type": "soldier"
        },
        {
            "name": "elf #2",
            "health": 76,
            "unit_type": "soldier"
        },
        {
            "name": "elf #3",
            "health": 86,
            "unit_type": "soldier"
        }
    ]
    dwarfs = [
        {
            "name": "dwarf #1",
            "health": 55,
            "unit_type": "soldier"
        },
        {
            "name": "dwarf #2",
            "health": 84,
            "unit_type": "soldier"
        },
        {
            "name": "dwarf #3",
            "health": 90,
            "unit_type": "soldier"
        }
    ]

    goblin = Squad("Goblin", goblins)
    elf = Squad("Elf", elfs)
    dwarf = Squad("Dwarf", dwarfs)

    goblin.strategy = "weakest"
    elf.strategy = "strongest"
    dwarf.strategy = "random"

    goblin.enemies = [elf, dwarf]
    elf.enemies = [goblin, dwarf]
    dwarf.enemies = [goblin, elf]

    goblin.attack()
    elf.attack()
    dwarf.attack()

    print(goblin.name, goblin.health)
    print(elf.name, elf.health)
    print(dwarf.name, dwarf.health)
