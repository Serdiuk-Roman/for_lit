#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Unit(metaclass=ABCMeta):

    @property
    @abstractmethod
    def health(self):
        pass

    @abstractmethod
    def attack_prob(self):
        pass

    @property
    @abstractmethod
    def damage(self):
        pass

    @abstractmethod
    def is_alive(self):
        pass

    def recharge(self):
        pass

    # если речардж достиг нуля то
    # можна брать юнита и атаковать


class Clock:
    def __init__(self):
        self.i = 0

    def tick(self):
        self.i += 1

    def time(self):
        return self.i
