"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, addit_cargo):
        try:
            if self.cargo + addit_cargo <= self.max_cargo:
                self.cargo += addit_cargo
                print("----> load", addit_cargo)
            else:
                raise CargoOverload
        finally:
            print("!!!__CargoOverload__!!!")
        # except CargoOverload:
        #     raise CargoOverload

    def remove_all_cargo(self):
        try:
            print("----> remove all cargo")
            return self.cargo
        finally:
            self.cargo = 0


# if __name__ == "__main__":
#     my_plane = Plane(100000, False, 1000, 200, 400)
#     print("Max cargo is", my_plane.max_cargo, ", current cargo is", my_plane.cargo)
#     my_plane.load_cargo(20)
#     print("Max cargo is", my_plane.max_cargo, ", current cargo is", my_plane.cargo)
#     my_plane.load_cargo(20)
#     print("Max cargo is", my_plane.max_cargo, ", current cargo is", my_plane.cargo)
#     my_plane.load_cargo(1200)
#     print("Max cargo is", my_plane.max_cargo, ", current cargo is", my_plane.cargo)
#     print(my_plane.remove_all_cargo())
#     print("Max cargo is", my_plane.max_cargo, ", current cargo is", my_plane.cargo)