class Vehicle:
    # Constructor of the class
    def __init__(self, name):
        self.name = name

    # Abstract method, defined by convention only
    def brand(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Car(Vehicle):
    def brand(self):
        return f"Car name: {self.name}"


class Bike(Vehicle):
    def brand(self):
        return f"Bike name: {self.name}"


if __name__ == "__main__":
    vehicles = [Car("BMW"), Car("Audi"), Bike("Bajaj")]

    for vehicle in vehicles:
        print(vehicle.brand())
