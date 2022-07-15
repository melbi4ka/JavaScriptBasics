message = input()
message_lst = []

for i in message:
    message_lst.append(i)

item = None

while True:
    command = input().split('|')
    if command[0] == 'Decode':
        print(f"The decrypted message is: {''.join(message_lst)}")
        break

    if command[0] == 'Move':
        item = message_lst[0:int(command[1])]
        del message_lst[0:int(command[1])]
        for letter in item:
            message_lst.append(letter)

    if command[0] == 'Insert':
        firstPart = message_lst[:int(command[1])]
        secondPart = message_lst[int(command[1]):len(message_lst)]
        message_lst = []
        for letter in firstPart:
            message_lst.append(letter)
        for letter in command[2]:
            message_lst.append(letter)
        for letter in secondPart:
            message_lst.append(letter)

    if command[0] == 'ChangeAll':
        message_lst[:] = [x if x != command[1] else command[2] for x in message_lst]
