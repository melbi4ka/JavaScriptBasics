import re

line = input()
pattern = r"[2-9|A|J|K|Q][S|H|D|C]|[1]0[S|H|D|C]"

match = re.findall(pattern, line)

print(" ".join(match))




