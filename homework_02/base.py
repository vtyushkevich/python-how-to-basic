from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        # print("----> start")
        try:
            if not self.started:
                if self.fuel > 0:
                    self.started = True
                else:
                    raise LowFuelError
            else:
                print("____It's already started____")
        finally:
            print("!!!__LowFuelError__!!!")
        # except LowFuelError:
        #     raise LowFuelError

    def move(self, distance=0):
        print("----> move to", distance, "km")
        try:
            if self.fuel_consumption * distance <= self.fuel:
                self.fuel -= (self.fuel_consumption * distance)
            else:
                raise NotEnoughFuel
        finally:
            print("!!!__NotEnoughFuel__!!!")
        # except NotEnoughFuel:
        #     raise NotEnoughFuel

    def stop(self):
        print("----> stop")
        self.started = False


# if __name__ == "__main__":
#     my_car = Vehicle(1000, 10, 5.0)
#     print("my_car.started =", my_car.started, ", my_car.fuel =", my_car.fuel, ", my_car.fuel_consumption =", my_car.fuel_consumption)
#     my_car.fuel = 0
#     print("my_car.started =", my_car.started, ", my_car.fuel =", my_car.fuel, ", my_car.fuel_consumption =", my_car.fuel_consumption)
#     my_car.start()
#     print("my_car.started =", my_car.started, ", my_car.fuel =", my_car.fuel, ", my_car.fuel_consumption =", my_car.fuel_consumption)


    # print("my_car.started =", my_car.started, ", my_car.fuel =", my_car.fuel, ", my_car.fuel_consumption =", my_car.fuel_consumption)
    # my_car.start()
    # print("my_car.started =", my_car.started, ", my_car.fuel =", my_car.fuel, ", my_car.fuel_consumption =", my_car.fuel_consumption)
    # my_car.move(200)
    # print("my_car.started =", my_car.started, ", my_car.fuel =", my_car.fuel, ", my_car.fuel_consumption =", my_car.fuel_consumption)
    # my_car.stop()
    # print("my_car.started =", my_car.started, ", my_car.fuel =", my_car.fuel, ", my_car.fuel_consumption =", my_car.fuel_consumption)
    # my_car.start()
    # print("my_car.started =", my_car.started, ", my_car.fuel =", my_car.fuel, ", my_car.fuel_consumption =", my_car.fuel_consumption)

