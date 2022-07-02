char_one = input()
char_two = input()
randome_string = input()
between_chars = []

for el in range(ord(char_one)+1, ord(char_two)):
    new_char = chr(el)
    between_chars.append(new_char)

sum_elements = 0
for char in randome_string:
    if char in between_chars:
        sum_elements += ord(char)

print(sum_elements)
