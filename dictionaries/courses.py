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
