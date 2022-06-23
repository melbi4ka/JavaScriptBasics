line = input().split("-")
contact_dict = {}


while len(line) > 1:
    contact = line
    if contact[0] not in contact_dict:
        contact_dict[contact[0]] = contact[1]

    line = input().split("-")

number = int("".join(line))

for num in range(number):
    name = input()
    if name in contact_dict.keys():
        print(f"{name} -> {contact_dict[name]}")
    else:
        print(f"Contact {name} does not exist.")


# print(contact_dict)
# print(number)
# print(name)


