class Vehicle:
    """
    Vehicle models a vehicle w/ tires and an engine
    """

    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires
        self.serial_number = ''

    def description(self):
        print(f"A vehicle with an {self.engine} engine, and {self.tires} tires")

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
