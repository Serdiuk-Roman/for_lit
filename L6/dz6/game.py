from abc import ABCMeta


class Unit(metaclass=ABCMeta):

    @abstractmethod
    def attack(self, target):
        pass

    @abstractmethod
    def take_damage(self, dmg):
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
