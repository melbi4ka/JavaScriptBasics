def valid_password(passwd):
    condition_one = False
    condition_two = False
    condition_three = False
    counter = 0
    if passwd.isalnum():
        condition_two = True
    if 6 <= len(passwd) <= 10:
        condition_one = True
    for el in passwd:
        if el.isdigit():
            counter += 1
            if counter >= 2:
                condition_three = True

    if condition_one and condition_two and condition_three:
        print("Password is valid")
    else:
        if not condition_one:
            print("Password must be between 6 and 10 characters")
        if not condition_two:
            print("Password must consist only of letters and digits")
        if not condition_three:
            print("Password must have at least 2 digits")


password = input()
valid_password(password)
