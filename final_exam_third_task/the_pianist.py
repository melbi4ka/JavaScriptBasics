number = int(input())
composer_dict = {}

for _ in range(number):
    piece, composer, key = input().split("|")
    if piece not in composer_dict:
        composer_dict[piece] = []
    composer_dict[piece].append(composer)
    composer_dict[piece].append(key)

a_command = input().split("|")
while a_command[0] != "Stop":
    piece = a_command[1]
    if a_command[0] == "Add":
        composer = a_command[2]
        key = a_command[3]
        if piece in composer_dict:
            print(f"{piece} is already in the collection!")
        else:
            composer_dict[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif a_command[0] == "Remove":
        if piece in composer_dict:
            del composer_dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif a_command[0] == "ChangeKey":
        new_key = a_command[2]
        if piece in composer_dict:
            composer_dict[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    a_command = input().split("|")

sorted_dict = dict(sorted(composer_dict.items(), key = lambda x: (x[0], x[1][1])))

for key, value in sorted_dict.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
