# Create a text file named "quiz.txt" that contains multiple-choice questions and their options. 
# Each question and its options are separated by newlines. 
# Implement a program to read the file in read mode ('r') and display the questions along with their options to the students

# file = open('Syllabus/quiz.txt', 'r')

# for ques in file:
#     print(ques)

with open("Syllabus\quiz.txt", "r") as f: # Open file in a read mode
    lines = f.readlines()

    questions = ""
    options = ""
    for line in lines:
        line = line.strip()
        if line.endswith("?"):
            if questions:
                print(questions)
                print(options)
                
            questions = line 
            options = ""
        else:
            options += line + '\n'
    print(questions)
    print(options)