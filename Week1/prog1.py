#    4 4 4 4
#     3 3 3
#      2 2
#       1

row= int(input("Enter number of rows: "))
for i in range(row, 0, -1): # To print rows
    for j in range(row, i, -1): # To print spaces
        print(end=" ")
    for k in range(0, i): # To print numbers
        print(i, end=" ")

    print(" ")
