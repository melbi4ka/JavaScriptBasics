command = input()
counter = 0

while command != "END":
    if command == "coding" or command == "cat" or command == "dog" or command == "movie":
        counter += 1
    elif command == "CODING" or command == "CAT" or command == "DOG" or command == "MOVIE":
        counter += 2

    if counter > 5:
        print("You need extra sleep")
        break

    command = input()

if counter <= 5:
    print(counter)
