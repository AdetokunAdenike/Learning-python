import random

names_string = input('Enter names: ')
names = names_string.split()
num_items = len(names)

person_to_pay = random.choice(names)
print(person_to_pay +" is going to pay for the meal today!")