class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update  # private copy of original update() method


class MappingSubclass(Mapping):
    def update(self, keys=[], values=[]):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

    def print_something(self):
        print("Printing something")

    updates = print_something

if __name__ == "__main__":
    print(dir(Mapping))
    print(dir(MappingSubclass))
