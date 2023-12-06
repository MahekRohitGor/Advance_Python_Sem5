# Different types of error and handling only one error at a time
def handle_error():
    try:
        result = 5/0
    except ZeroDivisionError:
        print("Caught Zero Division Error")

    try:
        value = "hello world"+5
    except TypeError:
        print("Cannot concatenate string with integer")

    try:
        num = int("hello")
    except ValueError:
        print("Error: ValueError")

    try:
        with open("filename.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("File was not found: filename.txt ")

# Handling Multiple Exception
def handle_multiple_exceptions():
    try:
        num = int(input("Enter a number: "))
        res = 10/num
        print("Result after division: ", res)
        list1 = [1,2,3,4]
        index = int(input("Enter index"))
        number = list1[index]
        print("Number at index ${index} is ${number}")

    except (ZeroDivisionError, IndexError):
        print("Division by zero or Index out of bound Error")


# CUSTOM EXCEPTIONS

class InvalidAgeException(Exception):
    "Your age is below 18"
    pass

if __name__ == "__main__":
    handle_error()
    handle_multiple_exceptions()

try:
    number = int(input("Enter a number: "))
    if number < 18:
        raise InvalidAgeException
    else:
        print("You can vote")

except InvalidAgeException:
    print("Exception : Invalid Age")

