numbers = input().split()
text = input()  # This is some message for you
message = ""

for i in range(len(numbers)):
    sum_of_digits = sum(map(int, numbers[i]))

    if sum_of_digits > len((text)):
        while sum_of_digits >= len(text):
            sum_of_digits -= len(text)
            if sum_of_digits <= len(text):
                message += text[sum_of_digits]

    else:
        message += text[sum_of_digits]

    text = text[:sum_of_digits] + text[sum_of_digits + 1:]

print(message)
