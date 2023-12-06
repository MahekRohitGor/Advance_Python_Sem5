#Program to calculate sum of all values in a column of a CSV file. Display suitable error messages if
#the column name doesn't exist or the column doesn't have numeric values.
# import csv
# Number = []
# sum = 0
# files = open("data.csv", "r")
# reader = csv.DictReader(files)
# for col in reader:
#     Number.append(col['Number'])

# for i in Number:
#     sum += int(i)

# print("Sum is: " + str(sum))

import csv

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

column_name = 'Number'  # The column you want to calculate the sum for
sum = 0

try:
    with open("data.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            value = row.get(column_name)
            if value is not None and is_numeric(value):
                sum += float(value)
            else:
                raise ValueError(f"Non-numeric value or missing value in column '{column_name}'.")

    print(f"Sum is: {sum}")

except FileNotFoundError:
    print("Error: File not found.")
except ValueError as e:
    print("Error:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
