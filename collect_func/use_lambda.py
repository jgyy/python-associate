# Creating a Lambda
def square(num):
    return num * num

square_lambda = lambda num : num * num

assert square(3) == square_lambda(3)
print(square(3) == square_lambda(3))
