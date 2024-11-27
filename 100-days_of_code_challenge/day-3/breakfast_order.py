print("Thank you for choosing Nikki English Breakfasts!")

size = input('What size do you want? S, M, or L ').upper()
add_butter = input('Do you want butter? Y or N ').upper()
extra_egg = input('Our standard is two eggs, do you want extra eggs? Y or N ').upper()
extra_bread = input('Our standard is two slices, do you want extra slice? ').upper()

bill = 0

if size == "S":
    bill += 2500
elif size == "M":
    bill += 3500
else:
    bill += 5000
if add_butter == "Y":
        bill += 200
if extra_egg == "Y":
        bill += 500
if extra_bread == "Y":
        bill += 500
print(f"Your final bill is {bill} naira")