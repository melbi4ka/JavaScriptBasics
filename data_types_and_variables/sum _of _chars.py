number_of_lines = int(input())
sum_ascii_value = 0

for char in range(number_of_lines):
    current_character = input()
    sum_ascii_value += ord(current_character)

print(f"The sum equals: {sum_ascii_value}")

