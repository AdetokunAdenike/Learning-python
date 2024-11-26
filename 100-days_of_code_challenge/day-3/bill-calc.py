print('''
                                        o
                                         o |
                                         |
      .       .           ._._.    _                     .===.
      |`      |`        ..'\ /`.. |H|        .--.      .:'   `:.
     //\-...-/|\         |- o -|  |H|`.     /||||\     ||     ||
 ._.'//////,'|||`._.    '`./|\.'` |\\||:. .'||||||`.   `:.   .:'
 ||||||||||||[ ]||||      /_T_\   |:`:.--'||||||||||`--..`=:='...
''')
print("Welcome to the rollercoaster")

height = int(input('Enter height: '))
bill = 0

if height >= 120:
    print("Can ride")
    age = int(input('Enter age: '))
    if age < 12:
        bill = 5
        print("Your bill is $5")
    elif age <= 18:
        bill = 7
        print("Your bill is $7")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Your bill is $0")
    else:
        bill = 12
        print("Your bill is $12")

    want_photo = input('Do you want to take a photo? Yes or NO?').upper()
    if want_photo == "YES":
        bill += 3
    print(f"Your bill is ${bill}")
else:
    print("Sorry, can't ride")