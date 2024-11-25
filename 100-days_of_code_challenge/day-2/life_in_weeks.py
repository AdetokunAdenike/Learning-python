#!/usr/bin/evn python3
"""
A program that calculates how many weeks we have left
by deducting current age from 90 years.
"""
print("Welcome to Life in Weeks. Asuming you will live up until 90 years, check how many weeks you have left from now.")
age = int(input('Enter your current age: '))
life_time = 90 - age
weeks_left = life_time * 52

print(f"You have {weeks_left} weeks left.")