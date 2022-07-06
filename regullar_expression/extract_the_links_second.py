import re

pattern = r"((www)\.([A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[\.a-z]+)+))"


line = input()
while line:
    matches = re.finditer(pattern, line)
    for match in matches:
        print(match.group(1))

    line = input()
