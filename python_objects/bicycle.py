# python -m python_objects.bicycle
from python_objects.vehicle import Vehicle

class Bicycle(Vehicle):
    default_tire = 'tire'

    def __init__(self, tires=None, distance_traveled=0, unit='mile'):
        super().__init__(distance_traveled, unit)
        if not tires:
            tires = [self.default_tire, self.default_tire]
        self.tires = tires

    def description(self):
        initial = super().description()
        return f"{initial} on {len(self.tires)} tires."

if __name__ == "__main__":
    bike = Bicycle()
    print(bike.tires)
    custom_bike = Bicycle(['front-tire', 'back-tire'])
    vehicle = Vehicle()
    print(vehicle.description())
    print(bike.description())
