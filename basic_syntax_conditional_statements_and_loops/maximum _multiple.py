divisor = int(input())
bound = int(input())
max_multiply = 0

for number in range(divisor + 1, bound + 1):
    if number % divisor == 0:
        max_multiply = number
print(max_multiply)


