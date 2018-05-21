#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    ### Vehicles
    ### Транспорт

    A battle vehicle has these additional properties:
    Бойові машини мають такі додаткові властивості:

    |   Property  |  Range  | Description                     |
    |-------------|---------|---------------------------------|
    |  operators  | \[1-3\] | The number of soldiers          |
                              required to operate the vehicle |
    | властивості | Діапазон | Опис                               |
    |-------------|----------|------------------------------------|
    |  Оператори  | \[1-3\]  | Кількість солдатів, необхідних     |
                               для керування транспортним засобом |

    The **recharge** property for a vehicle must be greater than 1000 (ms).
    Властивість **перезарядка** для транспортного засобу повинно перевищувати 1000 (мс).

    The total health of a vehicle unit is represented as the average health of all it's operators and the health of the vehicle.
    Загальний стан здоров'я транспортного засобу відображається як середнє значеення здоров'я всіх його операторів та здоров'я транспортного засобу.

    A vehicle is considered active as long as it self has any health and there is an vehicle operator with any health.
    Транспорт вважається активним, якщо він сам має якесь здоров'я, і ​​є оператор транспортного засобу з будь-яким здоров'ям.

    If the vehicle is destroyed, any remaining vehicle operator is considered as inactive (killed).
    Якщо транспортний засіб знищений, будь-який оператор, що залишився, вважається неактивним (убитий).

    #### Attack
    #### Атака

    The Vehicle attack success probability is determined as follows:
    Вірогідність успіху атаки транспорта визначається наступним чином:

    0.5 * (1 + vehicle.health / 100) * gavg(operators.attack_success)

    where **gavg** is the geometric average of the attack success of all the vehicle operators
    де **gavg** - геометричний середній показник успіху атаки всіх операторів транспортного засобу

    #### Damage
    #### Пошкодження

    The damage afflicted by a vehicle is calculated:
    Пошкодження, завданий транспортним засобом, розраховується:

    0.1 + sum(operators.experience / 100)

    The total damage inflicted on the vehicle is distributed to the operators as follows:
    Загальне пошкодження, завданий транспортному засобу, розподіляється операторам таким чином:

    - 60% of the total damage is inflicted on the vehicle
    - 60% загальної шкоди наноситься на транспортний засіб

    - 20% of the total damage is inflicted on a random vehicle operator
    - 20% від загальної шкоди наноситься випадковому оператору автомобіля

    - The rest of the damage is inflicted evenly to the other operators (10% each)
    - Решта пошкоджень наноситься рівномірно іншим операторам (по 10% кожен)
"""
from random import randint, choice

from unit_abc import Unit
from soldiers import Soldier


class Vehicle(Unit):

    def __init__(self, name, health, unit_type, operators):
        self.name = name
        self._health = health
        self.unit_type = unit_type
        self.experience = 0.01
        self.recharge = randint(1000, 2000)
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

        self._health = max(self._health - 0.6 * value, 0)

        damag_part = (0.3 * value) / len(self.operators)
        for operator in self.operators:
            operator.health = damag_part

        random_operator = choice(self.operators)
        random_operator.health = 0.1 * value

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
