"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):

    cargo = 0

    def __init__(self, max_cargo=0):
        self.max_cargo = max_cargo

    def load_cargo(self, addit_cargo):
        try:
            if self.cargo + addit_cargo <= self.max_cargo:
                self.cargo += addit_cargo
                print("----> load", addit_cargo)
            else:
                raise CargoOverload
        except CargoOverload:
            print("!!!___Cargo Overload___!!!")

    def remove_all_cargo(self):
        try:
            print("----> remove all cargo")
            return self.cargo
        finally:
            self.cargo = 0


my_plane = Plane(400)
print("Max cargo is", my_plane.max_cargo, ", current cargo is", my_plane.cargo)
my_plane.load_cargo(20)
print("Max cargo is", my_plane.max_cargo, ", current cargo is", my_plane.cargo)
my_plane.load_cargo(20)
print("Max cargo is", my_plane.max_cargo, ", current cargo is", my_plane.cargo)
my_plane.load_cargo(1200)
print("Max cargo is", my_plane.max_cargo, ", current cargo is", my_plane.cargo)
print(my_plane.remove_all_cargo())
print("Max cargo is", my_plane.max_cargo, ", current cargo is", my_plane.cargo)





    # def __init__(self, weight, started, fuel, fuel_consumption):
    #     super().__init__(weight, started, fuel, fuel_consumption)
    #     self.cargo = None
    #     self.max_cargo = None


