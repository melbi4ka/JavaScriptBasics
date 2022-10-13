import re

text = input()
pattern_one_happy = r"[c\(\[\*][\;|\:]"
pattern_two_happy = r"([\:|\;][\)D\*\]\}])"
pattern_one_sad = r"[;|:][([{c]"
pattern_two_sad = r"[D|)\]][;|:]"

happy_matches_one = re.findall(pattern_one_happy, text)
happy_matches_two = re.findall(pattern_two_happy, text)
happy = happy_matches_one + happy_matches_two

# print(happy)

sad_matches_one = re.findall(pattern_one_sad, text)
sad_matches_two = re.findall(pattern_two_sad, text)
sad = sad_matches_one + sad_matches_two

# print(sad)

happines_index = len(happy) / len(sad)

# print(happines_index)

final_emoji = ""
if happines_index < 1.0:
    final_emoji = ":("
elif happines_index == 1.0:
    final_emoji = ":|"
elif 1 < happines_index < 2:
    final_emoji = ":)"
elif happines_index >= 2.0:
    final_emoji = ":D"

print(f"Happiness index: {happines_index:.2f} {final_emoji}")
print(f"[Happy count: {len(happy)}, Sad count: {len(sad)}]")


