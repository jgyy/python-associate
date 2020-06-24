class Vehicle:
    """
    Vehicle models a vehicle w/ tires and an engine
    """
    def __init__(self, distance_traveled=0, unit='miles'):
        print(f"__init__ from Vehicle with distance_traveled: {distance_traveled} and {unit}")
        self.distance_traveled = distance_traveled
        self.unit = unit

    def description(self):
        return f"A {self.__class__.__name__} that has traveled {self.distance_traveled} {self.unit}"

if __name__ == "__main__":
    print("NONE")
