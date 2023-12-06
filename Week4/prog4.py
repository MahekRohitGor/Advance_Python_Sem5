from functools import reduce
def square(x):
    return x*x

square_using_lambda = lambda x: x*x
print("Square: ", square_using_lambda(10))

numbers = [1,2,3,4,5]
mapped_result = list(map(lambda x: x*3, numbers))

print("Mapped Result: ", mapped_result)

filtered_result = list(filter(lambda x: x%3 == 0, numbers))
print("FIltered Result: ", filtered_result)

reduced_result = reduce(lambda x,y: x+y, numbers)
print("Reduced Data: ", reduced_result)