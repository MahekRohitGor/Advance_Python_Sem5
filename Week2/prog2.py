# Develop a feedback collection program that allows users to submit their feedback.
# The program should prompt the user to enter their name (optional) and their feedback.
# The collected feedback should be stored in a file named "feedback.txt".
# The program should provide a menu with two options: "1. Submit feedback" and "2. Exit".
# If the user chooses option 1, the program should collect the feedback.
# If the user chooses option 2, the program should exit. Any other choice should result in an error message.

def collect_feedback():
    name = str(input("Enter you name (Optional): "))
    feedback = str(input("Enter Feedback: "))
    with open("Syllabus/Week2/feedback.txt", "a") as f:
        if bool(name):
            f.write("Name: {} \n".format(name))
        f.write("Feedback: {} \n".format(feedback))
    print("Feedback Submitted Successfully")


def main():
    while True:
        print("1. Submit Feedback")
        print("2. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            collect_feedback()
        elif choice == 2:
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
m

