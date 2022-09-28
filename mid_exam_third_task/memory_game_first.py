elements = [s for s in input().split()]
command = input().split()
counter = 0

while command[0] != "end":
    first_idx = int(command[0])
    second_idx = int(command[1])
    counter += 1
    if first_idx == second_idx or not 0 <= first_idx < len(elements) or not 0 <= second_idx < len(elements):
        elements = elements[:len(elements) //2 ] + [str(-counter) + "a"]*2 + elements[len(elements) //2: ]
        print(f"Invalid input! Adding additional elements to the board")
    else:
        if elements[first_idx] == elements[second_idx]:
            print(f"Congrats! You have found matching elements - {elements[first_idx]}!")
            x = elements.pop(first_idx)
            elements.remove(x)
            #del elements[first_idx], elements[second_idx]
        else:
            print("Try again!")
    if len(elements) == 0:
        print(f"You have won in {counter} turns!")
        break

    command = input().split()

if len(elements) > 0:
    print("Sorry you lose :(")
    print(" ".join(str(s) for s in elements))

