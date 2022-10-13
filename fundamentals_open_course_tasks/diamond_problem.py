import re

text = input()
pattern = r"(<(.+?)>)"

matches = re.finditer(pattern, text)
num_pattern = r"\d"
no_match = True


for match in matches:
    if match:

        word = match.group(2)

        numbers = re.findall(num_pattern, word)

        carats = sum([int(n) for n in numbers])
        print(f"Found {carats} carat diamond")

        no_match = False


if no_match:
    print("Better luck next time")
