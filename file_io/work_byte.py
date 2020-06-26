xmen = 'xmen.txt'

# bytes Object
my_bytes = b"This is a byte"
print(my_bytes)
print(bytes(b"This is a byte"))
print(bytes(10))
print(bytes(range(10)))
print(my_bytes)
print(my_bytes[0])
print(my_bytes[0:2])

# Bytearrays
print(bytearray())
print(bytearray(10))
print(bytearray(range(10)))
print(bytearray(b'Bytes'))
b_array = bytearray(10)
b_array[0:1] = b'T'
print(b_array)
b_array[1] = 0x10
print(b_array)

# Using bytes Mode for Files
with open(xmen, 'rb') as my_file:
    my_file.read()

with open(xmen, 'rb') as my_file:
    my_file.readlines()

# Reading into Bytearrays
my_file = open(xmen, 'rb')
b_array = bytearray(10)
print(my_file.readinto(b_array))
print(b_array)
new_b_array = bytearray(my_file.read(10))
print(new_b_array)
