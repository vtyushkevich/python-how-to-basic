"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle


class Car(Vehicle):

    def __init__(self, weight, started, fuel, fuel_consumption):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.engine = None
        self.volume = None
        self.pistons = None

    def set_engine(self, engine):
        self.volume = engine.volume
        self.pistons = engine.pistons
