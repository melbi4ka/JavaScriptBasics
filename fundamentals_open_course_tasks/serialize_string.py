start_string = input()
letter_dict = {}
n = 0
for char in start_string:
    x = start_string.index(char, n, len(start_string))
    n += 1
    if char not in letter_dict:
        letter_dict[char] = []
    letter_dict[char].append(str(x))

for key, value in letter_dict.items():
    print(f"{key}:{'/'.join(value)}")



