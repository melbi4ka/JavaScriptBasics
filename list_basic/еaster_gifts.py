gifts = input().split()
comand = input()

while comand != "No Money":
    current_comand = comand.split()
    index = 0
    if current_comand[0] == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == current_comand[1]:
                gifts[i] = "None"
    elif current_comand[0] == "Required":
        index = int(current_comand[2])
        if 0 < index < len(gifts):
            gifts[index] = current_comand[1]
    elif current_comand[0] == "JustInCase":
        gifts[-1] = current_comand[1]

    comand = input()


while "None" in gifts:
    gifts.remove("None")

for k in gifts: # print(" ".join(gifts))
    print(k, end=" ")

















