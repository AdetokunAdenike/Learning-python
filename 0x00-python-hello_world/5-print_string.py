#!/usr/bin/env python3
""" A program that prints 3 times a string followed by first 9 xter """


#!/usr/bin/python3
str = "Holberton School"
print("{}\n{}".format(3 * str, str[:9]))
"""
Other ways to do this
1. Using + to concatenate string
print((str * 3) + "\n" + str[:9])
2. Using f-strings
print(f"{str * 3}\n{str[:9]}")
3. Using join() method
print("\n".join([str * 3, str[:9]]))
4. Using multiline string
print(f""""""{str * 3} {str[:9]}"""""")
5. Multiple arguments
print(str * 3, str[:9], sep="\n")
6. Escape xter
print(str * 3 + "\n" + str[:9])
7. Using a loop
result = ""
for part in [str * 3, str[:9]]:
    result += part + "\n"
print(result, end="")
8. Using print() inside a function
def print_custom(str):
    print(f"{str * 3}\n{str[:9]}")

print_custom("Holberton School")
9. Using write() with sys.stdout
sys.stdout.write(f"{str * 3}\n{str[:9]}\n")

"""
