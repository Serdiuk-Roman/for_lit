#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from squads import Squad


class Army():
    def __init__(self, name, squads, clock):
        self.clock = clock
        self.name = name
        self.squads = []
        for squad in squads:
            self.squads.append(Squad(
                squad["name"],
                squad["units"],
                self.clock
            ))
        self.strategy = ""

    def add_strategy(self, strategy):
        self.strategy = strategy

    @property
    def health(self):
        return sum([squad.health for squad in self.squads])

    def is_alive(self):
        self.squads = [
            squad
            for squad in self.squads
            if squad.is_alive()
        ]
        return len(self.squads) > 0

    def is_active(self):
        return True in [unit.is_active() for unit in self.squads]


if __name__ == '__main__':
    goblin = Army("Trol")
    print(goblin.name)
