secret_message = input().split()

for word in secret_message: #минавам през всички думи
    chrs = ""
    dig = ""
    for char in word: # минавам през елементите на думата
        if char.isdigit(): # ако елемента е цифра, добавям отгоре към стринга за цифри
            dig += "".join(char)
        if char.isalpha(): # ако елемента е буква, добавям към стринга за букви
            chrs += "".join(char)
    decip_dig = chr(int(dig)) #намирам в ascii буквата, която отговаря на числото
    if len(chrs) > 1:
        decip_chrs = chrs[-1:] + chrs[1:-1] + chrs[:1] # swapвам първия и последния елемент
    else:
        decip_chrs = chrs # ако няма какво да суапвам

    print("".join(decip_dig+decip_chrs), end=" ")
