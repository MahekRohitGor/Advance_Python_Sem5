# Date: 31st July 2023
# Write a program to define two functions, read_csv(filename) and calculate_average(data), and a main function 
#that reads data from a CSV file, calculates the average of all values in the CSV, and prints the 
#result to the console. The goal of the code is to calculate the average of the values stored in a CSV file
#and display it as output.

def read_csv(filename):
    data = [] # empty data list
    with open(filename, 'r') as file:  # Open file in read mode
        lines = file.readlines()
        for line in lines:
            values = line.strip().split(',')
            data.extend(map(float, values)) # Values are converted to float, map applies float to each value and then adds it to data list
    return data

def calculate_average(data):
    if not data:
        return None

    total = sum(data)
    average = total / len(data) # Find average
    return average

def main():
    filename = 'Syllabus/Week2/marks.csv' 
    data = read_csv(filename)
    
    if data:
        average = calculate_average(data) # Calculating Average
        if average is not None:
            print("Average:", average)
        else:
            print("No numerical data found in the marks.csv")
    else:
        print("marks.csv file is empty or not found.")

if __name__ == "__main__":
    main()
