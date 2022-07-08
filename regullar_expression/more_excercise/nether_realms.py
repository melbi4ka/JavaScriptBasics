import re

line = input().split(",")

pattern = r"[^0-9\-\+\*\/\.]"
pattern_two = r"\-*((0|[0-9]+)[\.0-9]*)"


demons_dict = {}

for el in line:
    el = el.strip()
    demons_dict[el] = []
    matches = re.findall(pattern, el)

    health = 0
    for n in matches:
        health += ord(n)
    demons_dict[el].append(health)

    numbers = re.finditer(pattern_two, el)
    damage = 0
    for num in numbers:
        damage += float(num.group())

    for char in el:
        if char == "*":
            damage *= 2
        elif char == "/":
            damage /= 2

    demons_dict[el].append(damage)

sorted_demons_dict = sorted(demons_dict.items(), key=lambda kvpt: kvpt)

for n in sorted_demons_dict:
    print(f"{n[0]} - {n[1][0]} health, {n[1][1]:.2f} damage")


print(sorted_demons_dict)
