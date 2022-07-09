from abc import ABC
from exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight, started, fuel, fuel_consumption):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        print("----> start")
        try:
            if not self.started:
                if self.fuel > 0:
                    self.started = True
                else:
                    raise LowFuelError
            else:
                print("____It's already started____")
        except LowFuelError:
            print("!!!___Low Fuel___!!!")

    def move(self, distance=0):
        print("----> move to", distance, "km")
        try:
            if self.fuel_consumption * distance / 100 <= self.fuel:
                self.fuel -= (self.fuel_consumption * distance / 100)
            else:
                raise NotEnoughFuel
        except NotEnoughFuel:
            print("!!!___Not Enough Fuel___!!!")

    def stop(self):
        print("----> stop")
        self.started = False


# my_car = Vehicle(1000, False, 10.0, 5.0)
# print("my_car.started =", my_car.started, ", my_car.fuel =", my_car.fuel, ", my_car.fuel_consumption =", my_car.fuel_consumption)
# my_car.start()
# print("my_car.started =", my_car.started, ", my_car.fuel =", my_car.fuel, ", my_car.fuel_consumption =", my_car.fuel_consumption)
# my_car.start()
# print("my_car.started =", my_car.started, ", my_car.fuel =", my_car.fuel, ", my_car.fuel_consumption =", my_car.fuel_consumption)
# my_car.move(200)
# print("my_car.started =", my_car.started, ", my_car.fuel =", my_car.fuel, ", my_car.fuel_consumption =", my_car.fuel_consumption)
# my_car.stop()
# print("my_car.started =", my_car.started, ", my_car.fuel =", my_car.fuel, ", my_car.fuel_consumption =", my_car.fuel_consumption)
# my_car.start()
# print("my_car.started =", my_car.started, ", my_car.fuel =", my_car.fuel, ", my_car.fuel_consumption =", my_car.fuel_consumption)




