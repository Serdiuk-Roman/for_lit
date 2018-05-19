from unit_abc import Unit


class Squad(Unit):
    def __init__(self, *units):
        self.units = list(units)
