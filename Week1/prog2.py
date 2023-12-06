# Difference between list and tuple
# Lists are mutable and tuples are immutable

list1 = [1,2,3,4]
tuple1 = (1,2,3,4)

list1[2] = 5
tuple1[2] = 7 # Will show an error because tuple is immutable i.e it cannot be modified

print(list1)
print(tuple1)