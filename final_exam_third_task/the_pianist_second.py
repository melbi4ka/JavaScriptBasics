number = int(input())
piece_dict = {}

for _ in range(number):
    piece, composer, key = input().split("|")
    piece_dict[piece] = {'composer' : composer, 'key_piece' : key}

# print(piece_dict)

a_command = input()

while a_command != "Stop":
    command = a_command.split("|")
    action = command[0]

    if action == "Add":
        piece, composer, key = command[1:]
        if piece in piece_dict:
            print(f"{piece} is already in the collection!")
        else:
            piece_dict[piece] = {}
            piece_dict[piece]['composer'] = composer
            piece_dict[piece]['key_piece'] = key
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == "Remove":
        piece = command[1]
        if piece not in piece_dict:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            del piece_dict[piece]
            print(f"Successfully removed {piece}!")

    elif action == "ChangeKey":
        piece, new_key = command[1:]
        if piece not in piece_dict:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            piece_dict[piece]['key_piece'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")


    a_command = input()

for key, value in piece_dict.items():
    print(f"{key} -> Composer: {value['composer']}, Key: {value['key_piece']}")
