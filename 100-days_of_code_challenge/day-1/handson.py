# b = int(input('Enter number: '))

# if(b % 2 == 0):
#     print(str(b) + " " + "is even")
# else:
#     print(str(b) + " " + "is odd")

#A member of the elite club must be at least 150CM tall and over 18
print("Welcome to the Elites club")
height = int(input('Enter your height: '))

if height >= 150:
    print("Your are qualified, welcome to the team!")
    age = int(input('Enter your age: '))
    if age >= 18:
        print("You pass the age requirement.")
    else:
        print("You are too young.")
else:
    print("You are not qualified, please get taller.")

yes_vip = 1
no_vip = 0
if ()