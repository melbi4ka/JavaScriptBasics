first_string = input()
second_string = input()
last_string = first_string

for symbol in range(len(first_string)):
    left_side = second_string[:symbol+1]
    right_side = first_string[symbol+1:]
    current_string = left_side + right_side

    if current_string == last_string:
        continue
    print(current_string)
    last_string = current_string


