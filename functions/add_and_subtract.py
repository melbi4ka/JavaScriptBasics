def sum_numbers(a, b):
    return a + b


def subtract(a, b, c):
    return sum_numbers(a, b) - c

num_one = int(input())
num_two = int(input())
num_three = int(input())
print(subtract(num_one, num_two, num_three))
