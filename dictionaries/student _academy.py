number = int(input())
student_dict = {}

for num in range(number):
    name = input()
    grade = float(input())

    if name not in student_dict:
        student_dict[name] = []
    student_dict[name].append(grade)

for name, grade in student_dict.items():
    result = sum(grade) / len(grade)
    if result >= 4.50:
        print(f"{name} -> {result:.2f}")

#print(student_dict)
# можем да филтрираме и да ги напълним в нов речник,над търсената оценка
# после да печатаме само филтрирания речник  09/21 упражнения
# Order the
# filtered students by average grade in descending order.
# sorted_students = sorted(student_dict.items(), key = lambda kvpt: -kvpt[1])
# for name, grades in sorted_students:
#     print(f"{name} -> {grades:.2f}")





