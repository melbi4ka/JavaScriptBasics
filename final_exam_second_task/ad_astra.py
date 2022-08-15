# import re
#
# pattern = r"(#|\|)([A-za-z]+ ?[A-Za-z]+)+\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
#
#
# text = input()
#
# new_list = []
# calorie_sum = 0
# matches = re.finditer(pattern, text)
# for match in matches:
#     new_list.append(match.group(2))
#     new_list.append(match.group(3))
#     new_list.append(match.group(4))
#     calorie_sum += int(match.group(4))
# print(f"You have food to last you for: {calorie_sum // 2000} days!")
#
# for el in range(0, len(new_list), 3):
#     item = new_list[el]
#     date = new_list[el+1]
#     callorie = new_list[el+2]
#     print(f"Item: {item}, Best before: {date}, Nutrition: {callorie}")

# патърна - започва с хаштаг или пайп в група (#|\|)
# комбинация от главни и малки букви един или повече пъти, разстояние което или го има или го няма, т.е 0 или 1 път
# комбинация от главни и малки букви един или повече пъти, всичко в група, която се среща един или повече пъти
# ([A-za-z]+ ?[A-Za-z]+)+
# това което е мачнато в първа група \1
# две цифри наклонена черта ескейпната две цифри наклонена черта ескейпната две цифри наклонена черта ескепната в група (\d{2}\/\d{2}\/\d{2})
# това което е мачнато в първа група \1
# цифри повече от 1 пъти в група (\d+)
# това което е мачнато в първа група \1

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

# патърна - започва с хаштаг или пайп в група (#|\|)
# главни, малки букви и разстояние 1 или повече пъти в група ([A-Za-z\s]+)
# това което е мачнато в първа група \1
# две цифри наклонена черта ескейпната две цифри наклонена черта ескейпната две цифри наклонена черта ескепната в група (\d{2}\/\d{2}\/\d{2})
# това което е мачнато в първа група \1
# цифри от една до 5 в група (\d{1,5})
# това което е мачнато в първа група \1








