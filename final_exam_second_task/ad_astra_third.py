import re

pattern = r"(#|\|)[A-za-z]+( [A-Za-z]+)*\1\d{2}\/\d{2}\/\d{2}\1\d+\1"


text = input()
matches = re.finditer(pattern, text)
product_dict = {}
n=1

for match in matches:
    valid_match = match.group()
    if "#" in valid_match:
        valid_match = valid_match[1 : -1]
        product, date, calories = valid_match.split("#")
        product_dict[n] = [product, date, calories]
        n += 1

    elif "|" in valid_match:
        valid_match = valid_match[1: -1]
        product, date, calories = valid_match.split("|")
        product_dict[n] = [product, date, calories]
        n += 1

all_calories = 0
for value in product_dict.values():
    all_calories += int(value[2])

print(f"You have food to last you for: {all_calories // 2000} days!")
for value in product_dict.values():
    print(f"Item: {value[0]}, Best before: {value[1]}, Nutrition: {value[2]}")

print(all_calories)
