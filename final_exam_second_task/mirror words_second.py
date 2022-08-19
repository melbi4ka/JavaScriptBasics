import re

pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
text = input()

matches = re.finditer(pattern, text)
end_list = []
counter = 0

for match in matches:
    if match:
        first_word = match.group(2)
        second_word = match.group(3)
        if first_word == second_word[::-1]:
            mirrors = f"{first_word} <=> {second_word}"
            end_list.append(mirrors)
    counter += 1


if len(end_list) == 0 and counter == 0:
    print(f"No word pairs found!")
    print(f"No mirror words!")
else:
    print(f"{counter} word pairs found!")
    if len(end_list) == 0:
        print(f"No mirror words!")
    else:
        print(f"The mirror words are:")
        print(", ".join(end_list))
