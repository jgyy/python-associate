# python -m python_objects.amphibious_vehicle
from python_objects.boat import Boat
from python_objects.car import Car
from python_objects.vehicle import Vehicle
from python_objects.bicycle import Bicycle

class AmphibiousVehicle(Car, Boat):
    def __init__(self, engine, tires=[], distance_traveled=0, unit="miles"):
        super().__init__(
            engine=engine, tires=tires, distance_traveled=distance_traveled, unit=unit
        )
        self.boat_type = "motor"

    def travel(self, land_distance=0, water_distance=0):
        self.voyage(water_distance)
        self.drive(land_distance)

    def __str__(self):
        return f"<{self.__class__.__name__} {self.__dict__}>"

if __name__ == "__main__":
    water_car = AmphibiousVehicle('4 cylinder')
    print(water_car.description())
    water_car.travel(10, 15)
    print(water_car.description())
    print(dir(AmphibiousVehicle))
    print(hasattr(Boat, 'boat_type'))
    print(hasattr(Car, 'default_tire'))
    print(issubclass(Boat, Vehicle))
    print(issubclass(Boat, AmphibiousVehicle))
    print(issubclass(AmphibiousVehicle, Boat))
    print(isinstance(water_car, Bicycle))
    print(isinstance(water_car, AmphibiousVehicle))
    print(isinstance(water_car, Boat))
    print(water_car.__dict__)
    print(Boat.__dict__)
    print(type(water_car))
    print(Boat.__module__)
    print(str(water_car))
    print(water_car)
    
