#!/usr/bin/python3
# If age is 5 goto kindergaten
# age 6 through 17 goes to grades 1 through 12
# If age is greater than 17, say go to college
# Try to complete with 10 or less lines

age = eval(input('Enter age: '))

if age < 5:
    print("Too young for school")
elif age == 5:
    print("Go to kindergaten")
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to {} grade".format(grade))
else:
    print("Go to college")
