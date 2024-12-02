# student_heights = input().split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# sum = 0
# for height in student_heights:
#     sum += height
# print(sum)
# average = sum / (len(student_heights))
# print(round(average))

student_heights = input('Enter heights of students: ').split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height
print(f"Total height is {total_height}")

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"number of student is {number_of_students}")

average_height = round(total_height / number_of_students)
print("Average student height is " + str(average_height))