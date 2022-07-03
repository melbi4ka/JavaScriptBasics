import re

# pattern = r"(?<=\s)([A-Za-z0-9]+(?:[\._\-][a-z0-9]+)*)@([a-z]+[-]*[a-z]+\.[a-z\.]+)\b"
pattern = r"(?<=\s)([A-Za-z0-9]+[-._a-z0-9]*)@([a-z]+[-]*[a-z]+[\.a-z]+)\b"

text = input()
matches = re.finditer(pattern,text)

for match in matches:
    print(match.group())
