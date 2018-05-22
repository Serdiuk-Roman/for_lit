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
    def __init__(self, name, units, clock):
        self.clock = clock
        self.name = name
        self.units = []
        self._health = None
        for unit in units:
            if unit["unit_type"] == "soldier":
                self.units.append(Soldier(
                    unit["name"],
                    unit["health"],
                    unit["unit_type"],
                    self.clock
                ))
            elif unit["unit_type"] == "vehicle":
                self.units.append(Vehicle(
                    unit["name"],
                    unit["health"],
                    unit["unit_type"],
                    unit["operators"],
                    self.clock
                ))
        self.strategy = ""

    @property
    def health(self):
        self._health = sum([unit.health for unit in self.units])
        return self._health

    @health.setter
    def health(self, value):
        damag_part = value / len(self.units)
        for unit in self.units:
            unit.health = damag_part
        # print("health", self.name, self._health)

    def attack_prob(self):
        multiplication = 1
        for unit in self.units:
            multiplication *= unit.attack_prob()
        success_prob = pow(multiplication, 1 / len(self.units))
        return success_prob

    def attack(self, defend_squads, strategy):

        if strategy == "random":
            enemy = choice(defend_squads)
        elif strategy == "weakest":
            enemy = min(defend_squads, key=lambda sq: sq.health)
        elif strategy == "strongest":
            enemy = max(defend_squads, key=lambda sq: sq.health)

        attack_success = self.attack_prob()
        defend_success = enemy.attack_prob()
        print(attack_success, "vs", defend_success)
        if attack_success > defend_success:
            # damage to health
            print(
                strategy,
                self.name,
                round(self.health),
                "-->",
                enemy.name,
                round(enemy.health)
            )
            enemy.health = self.damage * attack_success
            for unit in self.units:
                unit.level_up()
                unit.start_recharge()
        else:
            print(
                "wrong",
                self.name,
                round(self.health),
                "-->",
                enemy.name,
                round(enemy.health)
            )

    @property
    def damage(self):
        full_damage = sum([
            unit.damage
            for unit in self.units
        ])
        print("full_damage : ", full_damage)
        return full_damage

    def is_alive(self):
        self.units = [
            unit
            for unit in self.units
            if unit.is_alive()
        ]
        return len(self.units) > 0

    def is_active(self):
        return True in [unit.is_active() for unit in self.units]


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

    enemies1 = [elf, dwarf]
    enemies2 = [goblin, dwarf]
    enemies3 = [goblin, elf]

    print(goblin.name, goblin.health)
    print(elf.name, elf.health)
    print(dwarf.name, dwarf.health)

    for i in range(3):

        goblin.attack(enemies1, "weakest")
        elf.attack(enemies2, "strongest")
        dwarf.attack(enemies3, "random")

        print(goblin.name, goblin.health)
        print(elf.name, elf.health)
        print(dwarf.name, dwarf.health)
