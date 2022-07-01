def valid_lenght(names):
    if 3 <= len(names) <= 16 and " " not in names:
        return True
    return False

def valid_char(names):
    for char in names:
        if not(char.isalnum() or char == "-" or char == "_"):
            return False
    return True

def valid_pass(names):
    if valid_lenght(names) == True and valid_char(names) == True:
        return True
    return False

usernames = input().split(", ")
for username in usernames:
    if valid_pass(username):
        print(username)
