class Vehicle:
    def __init__(self):
        self.tank = 800
        self.fuel = 700

    def drive(self):
        print(f"I driving somewhere")
        self.tank -= 50

    def refuel(self, fuel_amount):
        if self.fuel + fuel_amount <= self.tank:
            print("I'm refueled")
        else:
            print('To much Fuel!')


class LandVehicle(Vehicle):
    pass


class WaterVehicle(Vehicle):
    pass


class WheeledVehicle(LandVehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass
