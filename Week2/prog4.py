# Date: 31st July 2023
# Reading a Gradebook File
# You have a CSV file named "grades.csv" that contains student names and their corresponding grades. 
# Each line in the file consists of a student name followed by a comma and their grade. 
# Implement a program to read the file in read mode ('r') and calculate the average grade for the students.

total_grades = 0
num_of_students = 0

with open('Syllabus/Week2/grades.csv', 'r') as file: # Open file grades.csv in read mode
    lines = file.readlines()

    for line in lines:
        name, grade = line.strip().split(',') # We will seperate the name and grades which are seperated by commas

        total_grades += float(grade) # add all the grades and save it in total_grades
        num_of_students += 1 # increase number of students by one

if num_students > 0: # check if file contains the number of students or not
    average = total_grades / num_students # Find average of all the marks
    print("Average Grade of students in Grades.csv file: ", average) #Print the average marks
else:
    print("No data found in the Grades.csv file.") # If there is not data in the file then print no data found