#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from random import shuffle, choice
# from exceptions import FileNotFoundError
from Armies import Army


class Battle_sim():
    def __init__(self):
        self.armies = []
        self.losers = []
        self.gen_list = [
            "USA.json",
            "ZIM.json",
            "Mordor.json",
            "Mars.json",
            "Elf.json",
            "China.json",
            "Arab.json"
        ]
        self.strategy_list = [
            "random",
            "weakest",
            "strongest",
        ]

    def init_armies(self):
        # the choice of the number of armies
        while True:
            print("Enter the number of armies")
            print("from 2 to 7")
            number_of_armies = input(
                "default: 2\n\t> ")
            if number_of_armies == "":
                number_of_armies = 2
                break
            try:
                number_of_armies = int(number_of_armies)
            except ValueError:
                print("Doh!")
                continue
            if 2 <= number_of_armies <= 7:
                break

        # unit generation
        shuffle(self.gen_list)
        for number in range(number_of_armies):
            file_name = self.gen_list[number]
            with open(file_name) as input_file:
                input_data = json.loads(input_file.read())
                self.armies.append(Army(
                    input_data["armies"][0]["name"],
                    input_data["armies"][0]["squads"],
                ))

        # add strategy
        for army in self.armies:
            print("Enter the number to select a strategy for", army.name)
            print("1 - random\n2 - weakest\n3 - strongest")
            print("default : accidental")
            while True:
                number_of_strategy = input("\t> ")
                if number_of_strategy == "":
                    number_of_strategy = choice([1, 2, 3])
                    break
                try:
                    number_of_strategy = int(number_of_strategy)
                except ValueError:
                    print("Doh!")
                    continue
                if 1 <= number_of_strategy <= 3:
                    break
            army_strategy = self.strategy_list[number_of_strategy - 1]
            army.add_strategy(army_strategy)

        # show squads
        squad_list = [
            (squad.name, squad.health)
            for army in self.armies
            for squad in army.squads
        ]
        for squad in squad_list:
            print(squad)

    def start_game(self):
        print("START GAME")
        while True:
            for army in self.armies:
                print(army.name, "::", army.health)

            for army in self.losers:
                print(army.name, "#")

            attack_army = choice(list(
                army
                for army in self.armies
                if army.is_active
            ))
            attack_squad = choice(list(
                squad
                for squad in attack_army.squads
                if squad.is_active
            ))
            defend_armies = [
                army
                for army in self.armies
                if army != attack_army
            ]
            defend_squads = [
                squad
                for army in defend_armies
                for squad in army.squads
            ]
            attack_squad.attack(defend_squads, attack_army.strategy)

            # clear list of armies
            losers_army = [
                army
                for army in self.armies
                if not army.is_alive()
            ]
            self.losers.extend(losers_army)
            self.armies = [
                army
                for army in self.armies
                if army.is_alive()
            ]

            if len(self.armies) == 1:
                break
        print(self.armies.pop().name, "WIN")


if __name__ == "__main__":
    test_game = Battle_sim()
    test_game.init_armies()
    test_game.start_game()
