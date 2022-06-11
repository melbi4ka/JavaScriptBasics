number = int(input())
position = 0
electron_list = []

while number > 0:
    position += 1 # така позицията ни започва от 1
    shell = 2 * (position ** 2) #формулата за пълнене на шела
    if number > shell:
        electron_list.append(shell)
    else:
        electron_list.append(number) # ако позицията дава възможност за повече, но от номера няма такъв остатък
    number -= shell

print(electron_list)






