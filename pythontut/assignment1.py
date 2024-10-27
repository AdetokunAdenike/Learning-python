#!/usr/bin/python3
# Recieve miles and convert to kilometers
# Kilometers = miles * 1.60934
# Enter miles 5
# 5 miles equals 8.04 kilometers
miles = input('Enter miles ')
miles = int(miles)
kilometers = miles * 1.60934
print("{} miles equals {} kilometers".format(miles, kilometers))
