import re

text = input()

pattern = r"(\*\*|::)([A-Z][a-z]{2,})\1"
num_pattern = r"\d"

cools = list(map(int, re.findall(num_pattern, text)))

cool_treshold = 1
for n in cools:
    cool_treshold = cool_treshold * n
print(f"Cool threshold: {cool_treshold}")

matches = re.finditer(pattern, text)
cool_emoji = []
count = 0

for match in matches:
    if match:
        count += 1
        emoji = match.group(2)
        ascii_sum = 0
        for char in emoji:
            ascii_sum += ord(char)

        if ascii_sum > cool_treshold:
            cool_emoji.append(match.group())
print(f"{count} emojis found in the text. The cool ones are:")
x = "\n"
print(f"{x.join(cool_emoji)}")
