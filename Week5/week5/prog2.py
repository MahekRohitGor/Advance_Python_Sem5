import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def divide_by_zero(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        logging.error("Error Message: Division by zero error")
    else:
        logging.info(f"The result is {result}")


num1 = int(input("Enter a Number 1: "))
num2 = int(input("Enter NUmber 2: "))

divide_by_zero(num1,num2)


