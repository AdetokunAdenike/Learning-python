year = int(input('Enter year: '))

# if (year % 4 == 0):
#     if(year % 100 == 0):
#         if (year % 400 == 0):
#             print("Leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("It is a Leap year")
# else:
#     print("Not a leap year")

if (year%4==0 and year%100!=0 or year%400==0):
    print("Leap year")
else:
    print("Not leap year")