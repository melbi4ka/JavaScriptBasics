import re

name_regex = r"name is (?P<name>[A-Z][a-z]+ [A-Z][a-z]+)"
age_regex = r" (?P<years>\d{2}) years"
birth_regex = r"on (?P<birth>\d{2}\-\d{2}\-\d{4})\.$"

text = input()
count = 0

while text != "make migrations":
    condition_name = False
    condition_age = False
    condition_birth = False
    name, age, birth = 0, 0, 0
    database = False

    result_name = re.findall(name_regex, text)
    if result_name:
        name = "".join(result_name)
        condition_name = True

    result_age = re.findall(age_regex, text)
    if result_age:
        age = "".join(result_age)
        if 9 < int(age) < 100:
            condition_age = True

    result_birth = re.findall(birth_regex, text)
    if result_birth:
        birth = "".join(result_birth)
        condition_birth = True

    if condition_age and condition_name and condition_birth:
        print(f"Name of the person: {name}.")
        print(f"Age of the person: {age}.")
        print(f"Birthdate of the person: {birth}.")
        count += 1
    else:
        pass

    text = input()

if count == 0:
    print("DB is empty")