import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
'''
 
game = [rock, paper, scissors]

user_choice = int(input('Make a choice, 0 for rock, 1 for paper, or 2 for scissors? '))
print("You chose: " + game[user_choice])
computer_choice = random.randint(0, 2)
print("Computer chose:" + game[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You must have chosen an invalid input, please try again.")
elif computer_choice == user_choice:
    print("It's a draw")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice ==2:
    print("You lose!")
elif user_choice == 1 and computer_choice == 0:
    print("You win")
elif computer_choice == 1 and user_choice == 0:
    print("You you lose")
elif user_choice == 2 and computer_choice == 1:
    print("You win")
elif computer_choice == 2 and user_choice == 1:
    print("You lose")
