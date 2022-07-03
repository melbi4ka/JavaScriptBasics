import re

pattern = r"((?<=\s)([A-Za-z0-9]+[-\._a-z0-9]*)@([a-z]+)(-[a-z]+)*\.([\.a-z]+))\b"
# pattern = r"((?<=\s)([A-Za-z0-9]+[-\._a-z0-9]*)@[a-z\-]+(\.[a-z]+)+)\b"

text = input()
matches = re.findall(pattern,text)

for n in matches:
    print(n[0])
