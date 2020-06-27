import sys

try:
    if len(sys.argv) < 2:
        raise IndexError('Not enough arguments')
except IndexError as err:
    print("IndexError: " + str(err))
else:
    name = sys.argv[1]
    print(f"Name is {name}")
