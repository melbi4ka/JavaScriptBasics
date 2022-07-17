from math import ceil

first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students_count = int(input())

all_efficiency = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
hours_per_all = ceil(students_count / all_efficiency)
breaks = 0

if hours_per_all > 3:
    if hours_per_all % 3 != 0:
        breaks = hours_per_all // 3
    else:
        breaks = (hours_per_all // 3) - 1

new_hours_per_all = hours_per_all + breaks

print(f"Time needed: {new_hours_per_all}h.")







