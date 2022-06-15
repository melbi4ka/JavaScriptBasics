def validate(word):
    if not 6 <= len(word) < 10:
        print("Password must be between 6 and 10 characters")

    if not word.isalnum():
        print("Password must consist only of letters and digits")

    if sum(map(lambda x: x.isdigit(), word)) < 2:
        print("Password must have at least 2 digits")

    if word.isalnum() and sum(map(lambda x: x.isdigit(), word)) >= 2 and 6 <= len(word) < 10:
        print("Password is valid")


entry = input()
validate(entry)
