lines = input().split()
materials_dict = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
is_obtain = False

while is_obtain is False:
    for n in range(0, len(lines), 2):
        quantity = int(lines[n])
        key = lines[n + 1].lower()
        if key in materials_dict:
            materials_dict[key] += quantity

            if key == "shards":
                if materials_dict[key] >= 250:
                    materials_dict[key] -= 250
                    print("Shadowmourne obtained!")
                    is_obtain = True
                    break
            elif key == "fragments":
                if materials_dict[key] >= 250:
                    materials_dict[key] -= 250
                    print("Valanyr obtained!")
                    is_obtain = True
                    break
            elif key == "motes":
                if materials_dict[key] >= 250:
                    materials_dict[key] -= 250
                    print("Dragonwrath obtained!")
                    is_obtain = True
                    break
        else:
            if key not in junk:
                junk[key] = quantity
            else:
                junk[key] += quantity
    if is_obtain:
        break

    lines = input().split()

for key, value in materials_dict.items():
    print(f"{key}: {value}")
for key, value in junk.items():
    print(f"{key}: {value}")

# print(materials_dict)
# print(junk)
