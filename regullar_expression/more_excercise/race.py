participants_list = input().split(", ")
line = input()
participants_dict = {}

while line != "end of race":
    name = ""
    kilometers = 0
    for char in line:
        if char.isalpha():
            name += char
        elif char.isdigit():
            kilometers += int(char)

    if name in participants_list:
        if name not in participants_dict:
            participants_dict[name] = kilometers
        else:
            participants_dict[name] += kilometers

    line = input()

sorted_dict = (sorted(participants_dict.items(), key = lambda kvpt: -kvpt[1] ))
x = '\n'
print(f"1st place: {sorted_dict[0][0]}{x}"
      f"2nd place: {sorted_dict[1][0]}{x}"
      f"3rd place: {sorted_dict[2][0]}")

# print(participants_dict.items())
# print(sorted_dict)
# print(sorted_dict[0][0])


                                         

