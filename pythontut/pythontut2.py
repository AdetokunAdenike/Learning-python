#!/usr/bin/python3
# Store the user input of 2 numbers and the operator
num1, operator, num2 = input('Enter calculations ').split()
# Convert the strings into integers
num1 = int(num1)
num2 = int(num2)
# If + then we need to provide output based on addition
# Pint result
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
elif operator == "%":
    print("{} % {} = {}".format(num1, num2, num1 % num2))
else:
    print("Error, start again")
