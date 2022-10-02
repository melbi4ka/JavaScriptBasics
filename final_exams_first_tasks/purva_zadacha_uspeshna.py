password = input()
a_command = input()

while a_command != "Complete":
    command = a_command.split()
    action = command[0]


    if action == "Replace":
        char = command[1]
        value = int(command[2])

        sum = ord(char) + value
        new_char = chr(sum)
        if char in password:
            password = password.replace(char, new_char)
            print(password)

    elif action == "Make" and command[1] == "Upper":
        index = int(command[2])
        if 0 <= index < len(password):
            new_char = password[index].upper()
            password = password[:index] + new_char + password[index+1 : ]
            print(password)

    elif action == "Make" and command[1] == "Lower":
        index = int(command[2])
        if 0 <= index < len(password):
            new_char = password[index].lower()
            password = password[:index] + new_char + password[index + 1:]
            print(password)

    elif action == "Insert":
        index = int(command[1])
        char = command[2]
        if 0 <= index < len(password):
            password = password[:index] + char + password[index : ]
            print(password)

    elif action == "Validation":
        if not len(password) >= 8:
            print(f"Password must be at least 8 characters long!")
        condition_allnum = False
        condition_digit = False
        condition_upper = False
        condition_lower = False

        for el in password:
            if not el.isalnum():
                if el != "_":
                    print(f"Password must consist only of letters, digits and _!")


            if el.isupper():
                condition_upper = True


            if el.islower():
                condition_lower = True


            if el.isdigit():
                condition_digit = True


        if condition_upper == False:
            print(f"Password must consist at least one uppercase letter!")

        if condition_lower == False:
            print(f"Password must consist at least one lowercase letter!")

        if condition_digit == False:
            print(f"Password must consist at least one digit!")


    a_command = input()

# 100/100