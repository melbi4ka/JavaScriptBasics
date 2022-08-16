import re
import math


pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"

text = input()

numbers_as_list = []
for char in text:
    if char.isdigit():
        numbers_as_list.append(int(char))

result = math.prod(numbers_as_list)

matches = re.finditer(pattern,text)
cooler = []
counter = 0
for match in matches:
    word = match.group(2)
    coolnes = 0
    for char in word:
        coolnes += ord(char)
    if coolnes > result:
        cooler.append(match.group())
    counter += 1

print(f"Cool threshold: {result}")
print(f"{counter} emojis found in the text. The cool ones are:")
print("\n".join(cooler))
