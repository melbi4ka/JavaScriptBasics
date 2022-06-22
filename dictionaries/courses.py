line = input().split(" : ")

student_dict = {}

while line[0] != "end":
    course_name = line[0]
    student = line[1]
    #course_name, student = line.split(" : ")

    if course_name not in student_dict:
        student_dict[course_name] = []
    student_dict[course_name].append(student)

    line = input().split(" : ")

for course_name, student in student_dict.items():
    print(f"{course_name}: {len(student)}")
    result = '\n-- '.join(student)
    print(f"-- {result}")

# sorted_courses = sorted(student_dict.items(), key = lambda kvpt: -len(kvpt[1]))
# for course_name, student in sorted_courses:
#     print(f"{course_name}: {len(student)}")
#     for name in sorted(student):
#         print(f"-- {name}")
#  сортиране първо по големината на курсовете и после вътре по азбучен ред 09/21 упражнения
# When you receive the command "end", print the courses with their names
# and total registered users, ordered by the number of registered users in descending order.
# For each course print, the registered users ordered by name in ascending order (alphabetically).






#print(student_dict)
