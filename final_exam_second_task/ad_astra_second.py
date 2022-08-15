import re

pattern = r"(#|\|)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"
text = input()

new_list = []
calorie_sum = 0
matches = re.finditer(pattern, text)
for match in matches:
    new_list.append(match.group(2))
    new_list.append(match.group(3))
    new_list.append(match.group(4))
    calorie_sum += int(match.group(4))
print(f"You have food to last you for: {calorie_sum // 2000} days!")

for el in range(0, len(new_list), 3):
    item = new_list[el]
    date = new_list[el+1]
    callorie = new_list[el+2]
    print(f"Item: {item}, Best before: {date}, Nutrition: {callorie}")
