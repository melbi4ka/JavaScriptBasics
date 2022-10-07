first_password = input()

a_command = input()
raw_password = ""
while a_command != "Done":
    command = a_command.split()

    if command[0] == "TakeOdd":
        for char in range(1, len(first_password)):
            if char % 2 != 0:
                raw_password += first_password[char]
        print(raw_password)

    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        substring = raw_password[index : index + length]
        raw_password = raw_password.replace(substring, "", 1)
        print(raw_password)

    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in raw_password:
            raw_password = raw_password.replace(substring, substitute)
            print(raw_password)
        else:
            print("Nothing to replace!")

    first_password = raw_password

    a_command = input()

print(f"Your password is: {first_password}")
