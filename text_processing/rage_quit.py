gamer_string = input().upper()
new_string = ""

while len(gamer_string) > 0:
    colect_el = ""
    numbers_as_string = ""
    for el in range(len(gamer_string)):
        if not gamer_string[el].isdigit():
            colect_el += gamer_string[el]
        elif gamer_string[el].isdigit():
            numbers_as_string += gamer_string[el]
            if el+1 < len(gamer_string):
                if not gamer_string[el+1].isdigit():
                    break

    multyplyer = int(numbers_as_string)
    new_string += colect_el * multyplyer
    gamer_string = gamer_string[(len(colect_el) + len(numbers_as_string)):]
    
unique_symbols = len(set(new_string))

print(f"Unique symbols used: {unique_symbols}")
print(new_string)
