number = int(input())
is_balanced = False
balanced = []

for n in range(number):
    command = input()
    if command == "(":
        balanced.append("(")
    if command == ")":
        balanced.append(")")

if len(balanced) >= 2 and len(balanced) % 2 == 0:
    for index in range(0, len(balanced), 2):
        if balanced[index] == "(" and balanced[index+1] == ")":
            is_balanced = True
        else:
            is_balanced = False

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
