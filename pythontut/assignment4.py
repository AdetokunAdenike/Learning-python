#!/usr/bin/env python3
""" Guess the secret number """

secret_num = 9

while True:
    guess = int(input('Guess a number between 1 to 10: '))

    if guess == secret_num:
        print("You guessed right")
        break
    else:
        print("Wrong, try again")
