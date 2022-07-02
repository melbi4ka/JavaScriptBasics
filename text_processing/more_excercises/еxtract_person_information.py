import re

number = int(input())
name_pattern = r"@([a-zA-z]+)\|"
age_pattern = r"#(\d+)\*"

for _ in range(number):
    text = input()
    matches_name = re.findall(name_pattern, text)
    if matches_name:
        name = ''.join(matches_name)

    matches_age = re.findall(age_pattern, text)
    if matches_age:
        age = ''.join(matches_age)

    print(f"{name} is {age} years old.")



