#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from squads import Squad


class Army():
    def __init__(self, name, squads):
        self.name = name
        self.squads = []
        for squad in squads:
            self.squads.append(Squad(
                squad["name"],
                squad["units"]
            ))
        self.strategy = ""

    def add_strategy(self, strategy):
        for squad in self.squads:
            squad.strategy = strategy
        self.strategy = strategy

    def add_enemies(self, enemies):
        for squad in self.squads:
            squad.enemies = enemies

    @property
    def health(self):
        return sum([squad.health for squad in self.squads])


if __name__ == '__main__':
    goblin = Army("Trol")
    print(goblin.name)
