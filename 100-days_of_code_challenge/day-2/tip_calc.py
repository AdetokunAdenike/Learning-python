#!/usr/bin/python3

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_bill = bill * (1 + (tip / 100))
print(f"Your final bill is {total_bill}")
bill_per_person = float(input('How many people are you sharing this bill with? '))
final_bill_per_person = total_bill / bill_per_person
print("Each person will pay ${:.2f}".format(final_bill_per_person))