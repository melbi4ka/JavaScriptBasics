line = input()
replace_message = ""

for el in range(len(line)-1):
    if line[el] != line[el+1]:
        replace_message += line[el]

replace_message += line[-1]


print(replace_message)