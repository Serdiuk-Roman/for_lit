from abc import ABCMeta

class Unit(metaclass=ABCMeta):
    def __init__(self, health, recharge):
        self.health = health
        self.recharge = recharge

    @abstractmethod
    def attack(self, target):
        pass

    @abstractmethod
    def take_damage(self, dmg):
        pass

    @abstractmethod
    def is_active(self):
        pass

    # @property
    # @abstractmethod
    # is_alive
    # health
    # attack_power
    # если речардж достиг нуля то можна брать юнита и атаковать

    def recharge(self):
        pass

    def teek(self):
        pass


class Clock:
    def __init__(self):
        self.i = 0

    def tick(self):
        self.i += 1

    def time(self):
        return self.i


class Soldier(Unit):
    def __init__(self, health, recharge, experience):
        pass

    def attack(self):
        return 0.5 * (1 + self.health/100) * random(50 + self.experience, 100) / 100

    def damage(self):
        return 0.05 + self.experience / 100