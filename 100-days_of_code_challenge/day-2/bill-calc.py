print("Welcome to the rollercoaster")

height = int(input('Enter height: '))
bill = 0

if (height > 120):
    print("Can ride")
    age = int(input('Enter age: '))
    if age < 12:
        bill = 5
        print("Your bill is $5")
    elif age <= 18:
        bill = 7
        print("Your bill is $7")
    elif age > 18:
        bill = 12
        print("Your bill is $12")
    want_photo = input('Do you want to take a photo? Yes or NO?')
    if want_photo == "Yes":
        bill += 3
    print(f"Your bill is {bill}")
else:
    pri(int("Can't ride")