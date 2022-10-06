import re

pattern = r"([@|#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"

text = input()
matches = re.finditer(pattern, text)
count = 0
mirrors_list = []

for match in matches:
    if match:
        count += 1
        first_word = match.group(2)
        second_word = match.group(3)

        reversed_second = second_word[::-1]

        if first_word == reversed_second:
            mirrors_list.append(f"{first_word} <=> {second_word}")

if count == 0:
    print(f"No word pairs found!")
    print(f"No mirror words!")
else:
    print(f"{count} word pairs found!")
    if len(mirrors_list) > 0:
        print("The mirror words are:")
        print(", ".join(mirrors_list))
    else:
        print("No mirror words!")
