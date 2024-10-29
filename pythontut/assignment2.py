#!/usr/bin/env python3
# Have the user enter their investment amount and expected interest
# Each year thier investment will increase by their investment + their investment * interest rate is
# Print out the earnings after a 10 year period

# Ask for the money invested + the interest rate
investment = input('Enter investment: ')
interest = input('Enter interest: ')
# Convert the value to a float
investment = float(investment)
# Convert value to a float and round the percentage to 2 digits
interest = float(interest) * .01
# Cycle through 10 years using a for loop and range from 0 to 9
for i in range(10):
    investment = investment + (investment * interest)
# Output the results
print("investement after 10 years: {:.2f}".format(investment))
