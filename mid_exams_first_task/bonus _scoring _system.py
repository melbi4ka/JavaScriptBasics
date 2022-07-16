from math import ceil

number_students = int(input())
number_lectures = int(input())
additional_bonus = int(input())
total_bonus = 0
max_bonus = 0
max_attendance = 0


for student in range(number_students):
    attendance = int(input())
    total_bonus = (attendance / number_lectures) * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_attendance = attendance

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {max_attendance} lectures.")
