# Design a program that allows users to log their exercise activities and view their exercise logs. 
# The program should provide a user-friendly interface to input exercise details such as date, exercise type, duration, and calories burned. 
# The exercise logs should be stored in a file for future reference.

def log_exercise(): # Function to log the exercise details of the user
    date = input("Enter Date: ") # Take date as input
    exercise_type = str(input("Enter Exercise type: ")) # Take exercise type as input
    duration = float(input("Duration of exercise in hours: ")) # Take duration as input
    calories = input("Enter Calories burned: ") # Take calories burned as input

    with open('Syllabus/Week2/demo.txt', 'a') as f: # Open file in an append mode
        f.write("{}, {}, {}, {} \n".format(date, exercise_type, duration, calories)) # Write the data into file
        print("Exercise logged") # Prompt user that exercise looged successfully

def view_log(): # To View the detils of the file 
    with open("Syllabus/Week2/demo.txt", "r") as file1: # Open file in read mode
        for line in file1:
            print(line.strip())

def main():
    while True:
        print("1. Log Exercise")  # Give user choice to either enter the details or display the previous details of exercise
        print("2. View Log")
        print("3. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            log_exercise()
        elif choice == 2:
            view_log()
        elif choice == 3:
            break # Break the while loop when input is 3
        else:
            print("Invalid Input !")


if __name__ == "__main__":
    main() # Main function calling