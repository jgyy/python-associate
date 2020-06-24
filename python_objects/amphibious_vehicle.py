# python -m python_objects.amphibious_vehicle
from python_objects.boat import Boat
from python_objects.car import Car

class AmphibiousVehicle(Car, Boat):
    def __init__(self, engine, tires=[], distance_traveled=0, unit="miles"):
        super().__init__(
            engine=engine, tires=tires, distance_traveled=distance_traveled, unit=unit
        )
        self.boat_type = "motor"

    def travel(self, land_distance=0, water_distance=0):
        self.voyage(water_distance)
        self.drive(land_distance)

if __name__ == "__main__":
    water_car = AmphibiousVehicle('4 cylinder')
    print(water_car.description())
    water_car.travel(10, 15)
    print(water_car.description())
