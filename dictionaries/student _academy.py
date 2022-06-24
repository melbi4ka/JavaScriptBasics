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
        
