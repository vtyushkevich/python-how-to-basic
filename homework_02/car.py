"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine: Engine):
        self.engine = engine


# if __name__ == "__main__":
#     my_car = Car(1000, 10.0, 5.0)
#     print("my_car.started =", my_car.started, ", my_car.fuel =", my_car.fuel, ", my_car.fuel_consumption =", my_car.fuel_consumption)
#     my_car.start()
#     print("my_car.started =", my_car.started, ", my_car.fuel =", my_car.fuel, ", my_car.fuel_consumption =", my_car.fuel_consumption)
#     my_car.start()
#     print("my_car.started =", my_car.started, ", my_car.fuel =", my_car.fuel, ", my_car.fuel_consumption =", my_car.fuel_consumption)
#     my_car.move(200)
#     print("my_car.started =", my_car.started, ", my_car.fuel =", my_car.fuel, ", my_car.fuel_consumption =", my_car.fuel_consumption)
#     my_car.stop()
#     print("my_car.started =", my_car.started, ", my_car.fuel =", my_car.fuel, ", my_car.fuel_consumption =", my_car.fuel_consumption)
#     my_car.start()
#     print("my_car.started =", my_car.started, ", my_car.fuel =", my_car.fuel, ", my_car.fuel_consumption =", my_car.fuel_consumption)
#     my_eng = Engine(10, 11)
#     print("my_car.volume =", my_car.volume, ", my_car.pistons =", my_car.pistons)
#     my_car.set_engine(my_eng)
#     print("my_car.volume =", my_car.engine.volume, ", my_car.pistons =", my_car.engine.pistons)