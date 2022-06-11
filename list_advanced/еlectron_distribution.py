number = int(input())
position = 0
electron_list = []

while number > 0:
    position += 1 # position starts from 1
    shell = 2 * (position ** 2) #shell filling formula
    if number > shell:
        electron_list.append(shell)
    else:
        electron_list.append(number) # if there is no remainder of the number, but the position allows for more
    number -= shell

print(electron_list)
