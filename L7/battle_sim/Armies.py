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

    @property
    def is_active(self):
        return True


if __name__ == '__main__':
    goblin = Army("Trol")
    print(goblin.name)
