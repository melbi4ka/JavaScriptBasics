line = input()
sides_dict = {}

while line != "Lumpawaroo":
    if "|" in line:
        explode = line.split(" | ")
        force_side = explode[0]
        force_user = explode[1]
        if force_side not in sides_dict:
            sides_dict[force_side] = [force_user]

        elif force_user not in str(sides_dict.values()):
            if force_side in sides_dict:
                sides_dict[force_side].append(force_user)

    elif "->" in line:
        explode = line.split(" -> ")
        force_user = explode[0]
        force_side = explode[1]
        for side, user in sides_dict.items():
            if force_user in user:
                sides_dict[side].remove(force_user)

        if force_side not in sides_dict:
            sides_dict[force_side] = [force_user]

        elif force_user not in str(sides_dict.values()):
            if force_side in sides_dict:
                sides_dict[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    line = input()

for side, user in sides_dict.items():
    if len(user) >= 1:
        print(f"Side: {side}, Members: {len(user)}")
        x = '\n! '.join(user)
        print(f"! {x}")

# 80/100
#
# print(sides_dict)



