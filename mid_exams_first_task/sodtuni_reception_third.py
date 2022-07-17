
first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students_count = int(input())

all_efficiency_per_hour = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
needed_hours = 0

while students_count >= 0:
    students_count -= all_efficiency_per_hour
    needed_hours += 1

    if needed_hours % 4 == 0:
        needed_hours += 1

print(f"Time needed: {needed_hours}h.")
