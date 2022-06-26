line = input()
sides_dict = {}

while line != "Lumpawaroo":
    if "|" in line:
        explode = line.split(" | ")
        force_side = explode[0]
        force_user = explode[1]
        check = False

        for key, value in sides_dict.items():
            if force_user in value:
                check = True
                break
        if check is False:
            if force_side not in sides_dict:
                sides_dict[force_side] = [force_user]
            elif force_side in sides_dict and force_user not in sides_dict[force_side]:
                sides_dict[force_side].append(force_user)

    elif "->" in line:
        explode = line.split(" -> ")
        force_user = explode[0]
        force_side = explode[1]
        check_two = False
        for side, user in sides_dict.items():
            if force_user in user:
                sides_dict[side].remove(force_user)

        for key, value in sides_dict.items():
            if force_user in value:
                check_two = True
                break
        if check_two is False:
            if force_side not in sides_dict:
                sides_dict[force_side] = [force_user]
            elif force_side in sides_dict and force_user not in sides_dict[force_side]:
                sides_dict[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")

    line = input()

for side, user in sides_dict.items():
    if len(user) >= 1:
        print(f"Side: {side}, Members: {len(user)}")
        x = '\n! '.join(user)
        print(f"! {x}")
