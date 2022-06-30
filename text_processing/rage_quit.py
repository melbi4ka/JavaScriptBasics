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

                    """ако елемента не е цифра, колектваме във временна променлива
                    ако елемента е цифра, колектваме във друга временна променлива
                    проверяваме дали следващия елемент е в рейнджа. ако е тру, проверяваме дали е цифра.
                    Ако не е цифра, брейкваме и излизаме от форцикъла. 
                    Ако е цифра се връщаме отначало във фор цикъла, докато колектнем всички цифри"""

    multyplyer = int(numbers_as_string)
    new_string += colect_el * multyplyer
    gamer_string = gamer_string[(len(colect_el) + len(numbers_as_string)):]
    """когато сме излезли от фор цикъла вече имаме числото, което умножаваме по колектната част
     намаляме първоначалния стринг с дължината на колектната част и числото """


unique_symbols = len(set(new_string))

print(f"Unique symbols used: {unique_symbols}")
print(new_string)

# print(unique_symbols)



