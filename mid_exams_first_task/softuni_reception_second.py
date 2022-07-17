
first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
students_count = int(input())

all_efficiency_per_sixty_min = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
needed_min_per_all_students = students_count * 60
min_per_all = needed_min_per_all_students / all_efficiency_per_sixty_min

hours_per_all = min_per_all // 60
rest_minutes = min_per_all % 60
if rest_minutes != 0:
    hours_per_all += 1

breaks = 0

if hours_per_all > 3:
    breaks = hours_per_all // 3

new_hours_per_all = hours_per_all + breaks

print(f"Time needed: {new_hours_per_all:.0f}h.")

