import re

participants_list = input().split(", ")
line = input()
participants_dict = {participant: 0 for participant in participants_list}

while line != "end of race":
    name = "".join(re.findall(r'[A-Za-z]', line))
    kilometers = sum([int(el) for el in re.findall(r'\d', line)])
    if name in participants_dict:
        participants_dict[name] += kilometers

    line = input()

sorted_dict = (sorted(participants_dict.items(), key = lambda kvpt: -kvpt[1]))
x = '\n'
print(f"1st place: {sorted_dict[0][0]}{x}"
       f"2nd place: {sorted_dict[1][0]}{x}"
       f"3rd place: {sorted_dict[2][0]}")
print(participants_dict)
