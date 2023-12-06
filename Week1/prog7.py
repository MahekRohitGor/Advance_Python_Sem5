# Map Reduce Filter

# The map() function applies a given function to all items in an input iterable (e.g., list, tuple) and returns a new iterable containing the results. The general syntax of map is:

# map(function, sequence)
# map(lambda x: x*2, list) Every element in list gets doubled

numbers = [1,2,3,4,5]
doubled_numbers = map(lambda x: x*2, numbers)
print(list(doubled_numbers))


# In Python 3, reduce() is no longer a built-in function, but it's available in the functools module. It applies a function of two arguments cumulatively to the items of an iterable from left to right, reducing the iterable to a single value. The general syntax of reduce is:
# from functools import reduce
# reduce(function, iterable[, initializer])
# function: The function that takes two arguments and performs the reduction operation.
# iterable: The sequence of elements to be reduced.
# initializer (optional): An initial value to start the reduction. If provided, the function will be applied to the initial value and the first element of the iterable.

from functools import reduce
numbers = [2,4,6,8,10]
mulnum = reduce(lambda x,y: x*y, numbers)

print(mulnum)

# The filter() function creates a new iterable containing only the elements from the original iterable for which the given function returns True. The general syntax of filter is:
# filter(function, iterable)
# function: The function that returns True or False based on some condition.
# iterable: The sequence of elements to be filtered.

numbers = [1,2,3,4,5,6,7,8,9,10]
filtered_number = filter(lambda x: x%3==0, numbers)
print(list(filtered_number))
