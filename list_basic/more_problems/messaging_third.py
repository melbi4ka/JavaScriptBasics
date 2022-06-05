numbers = input().split(' ')
sequence = list(input())
message = []

for num in numbers:
    digits_sum = 0
    for digit in num:
        digits_sum += int(digit)
    char_index = digits_sum % len(sequence)
    message.append(sequence[char_index])
    sequence.pop(char_index)

print(''.join(message))
