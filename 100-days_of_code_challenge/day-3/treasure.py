print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')

print("Welcome to treasure island. Your mission is to find the treasure.")

x = input('You\'re at a cross-road, where do you want to go? Type "left" or "right"').lower()
if x == "left":
    y = input('There is an Island in the middle of the lake, would you like to swim or wait? Type "swim" or "wait"').lower()
    if y == "wait":
        z = input('You arrived at the Island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which door would you like to open? type "Blue" or "Red" or "Yellow"').lower()
        if z == "yellow":
            print("You Win")
        elif z == "red":
            print("You got burned by fire. Game Over")
        else:
            print("You got attacked by a beast. Game Over")
    else:
        print("You got attacked by a whale. Game Over")
else:
    print("You\'ve fallen over. Game Over")
