#!/usr/bin/python3
# -*- coding: utf-8 -*-


class AnimalError(Exception):
    def __init__(self, animal):
        super().__init__()
        self.animal = animal


class Animal:
    """Base class for animal

    bla-bla-car
    """

    def say(self):
        raise NotImplementetError

    def __init__(self, name):
        self.name = name


def butter(fn):
    def wrapper(self, msg):
        print("see butter")
        fn(self, msg)
    return wrapper


class Predator:
    def say(self):
        print("Rrrrr")


class Cat(Animal, Predator):
    """sss"""

    def __init__(self, name, color="red"):
        self.color = color
        super().__init__(name)

    def __str__(self):
        return "error: %s" % str(self.name)

    @butter
    def say(self, msg):
        if msg != "":
            print("Cat", self.name, "Meove", msg)
        else:
            raise AnimalError(self)


if __name__ is "__main__":
    black_cat = Cat("Black")
    vasia_car = Cat("Vasia", "brown")
    sharik_car = Cat("Sharik", "white")
    black_cat.say("qwe")
    vasia_car.say("rty")
    sharik_car.say("asd")

    try:
        sharik_car.say("")
    except AnimalError as e:
        print(e.animal)
