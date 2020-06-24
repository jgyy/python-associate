class Vehicle:
    """
    Vehicle models a vehicle w/ tires and an engine
    """
    default_tire = 'tire'

    def __init__(self, engine="", tires="", distance_traveled=0, unit='miles'):
        self.distance_traveled = distance_traveled
        self.unit = unit
        self.engine = engine
        self.tires = tires
        self.serial_number = ''

    @classmethod
    def bicycle(cls, tires=None):
        if not tires:
            tires = [cls.default_tire, cls.default_tire]
        return cls(None, tires)

    def description(self):
        return f"A {self.__class__.__name__} that has traveled {self.distance_traveled} {self.unit}"


if __name__ == "__main__":
    civic = Vehicle('4-cylinder', ['front-driver', 'front-passenger', 'rear-driver', 'rear-passenger'])
    print(civic.tires)
    print(civic.engine)
    honda = Vehicle('4-cylinder', ['front-driver', 'front-passenger', 'rear-driver', 'rear-passenger'])
    print(honda.engine)
    print(honda.tires)
    print(honda.description)
    honda.description()
    honda.serial_number = '1234'
    print(honda.serial_number)
    del honda.serial_number

    bike = Vehicle.bicycle()
    print(bike)
    bike.description()
    print(bike.engine)
    print(bike.tires)
