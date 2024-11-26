print("The compatibility calculator is calculating your score...")
name1 = input('Your name: ')
name2 = input('Their name: ')
name1_name2 = (name1 + name2).lower()

t = name1_name2.count("t")
r = name1_name2.count("r")
u = name1_name2.count("u")
e = name1_name2.count("e")
first_word = t + r + u + e

l = name1_name2.count("l")
o = name1_name2.count("o")
v = name1_name2.count("v")
e = name1_name2.count("e")
second_word = l + o + v + e

total_count = int(str(first_word) + str(second_word))

if total_count < 10 or total_count > 90:
    print(f"Your score is {total_count}, you go together like coke and mentos")
if 40 >= total_count <= 50:
    print(f"Your score is {total_count}, you are alright together.")
print(f"Your score is {total_count}")

# for letter in "true love":
#     if letter != " ":
#         total_count += name1_name2.count(letter)
# print(f"Your score is {total_count}")