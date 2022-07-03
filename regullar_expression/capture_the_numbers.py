import re

pattern = r"\d+"
line = input()
output_matches = []

while line:
    matches = re.findall(pattern, line)
    if matches:
        output_matches.append(" ".join(matches))
    line = input()

print(*output_matches)
