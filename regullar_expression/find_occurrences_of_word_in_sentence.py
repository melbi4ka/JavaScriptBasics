# import re
#
#
# text = input()
# word = input()
# pattern = fr"\b{word}\b"
#
#
# matches = re.findall(pattern, text, flags=re.I)
# print(len(matches))

import re

text = input().lower()
word = input().lower()
pattern = fr"\b{word}\b"

matches = re.findall(pattern, text)
print(len(matches))
