
str_password = input()
command = input().split()

while command[0] != "Done":

    if command[0] == "TakeOdd":
        raw_pass = ""
        for n in range(len(str_password)):
            if n % 2 != 0:
                raw_pass += str_password[n]
        str_password = raw_pass
        print(str_password)
    if command[0] == "Cut":
        index = int(command[1])
        a_len = int(command[2])
        cut_part = str_password[index:index+a_len]
        str_password = str_password.replace(cut_part, "", 1)
        print(str_password)
    if command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in str_password:
            str_password = str_password.replace(substring, substitute)
            print(str_password)
        else:
            print("Nothing to replace!")

    command = input().split()

print(f"Your password is: {str_password}")

