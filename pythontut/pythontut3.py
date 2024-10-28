#!/usr/bin/python3
# We'll provide different output based on age
# 1 - 18 -> important
# 21, 50, > 65 -> important
# All others -> not important

# Receive age and store in age
age = eval(input('Enter age '))
# if age is both greater than or equal to 1 and less than or equal to 18 important
if (age >= 1) and (age <= 18):
    print("Important Birthday")

# if age is either 21 or 50 important
elif (age == 21) or (age == 50):
    print("Important Birthday")
# We check if age is less than 55 and then convert true to false and vice versa.
elif not(age < 65):
    print("Important Birthday")
# Else not important
else:
    print("Sorry, not important")
