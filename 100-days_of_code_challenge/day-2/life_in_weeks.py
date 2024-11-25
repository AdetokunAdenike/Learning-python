#!/usr/bin/evn python3
"""
A program that calculates how many weeks we have left
by deducting current age from 90 years.
"""
print("Welcome to Life In Weeks. Asuming you will live up until 90 years, check how many weeks you have left from now.")
age = int(input('Enter your current age: '))
life_time = 4692
age_in_weeks = age * 52
weeks_left = life_time - age_in_weeks

print("You have " + str(weeks_left) + " weeks left.")