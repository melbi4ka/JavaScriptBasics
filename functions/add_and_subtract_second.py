def sum_numbers(a, b):
    return a + b


def subtract(summ, c):
    return summ - c


num_one = int(input())
num_two = int(input())
num_three = int(input())
sum_first_two = sum_numbers(num_one, num_two)
print(subtract(sum_first_two, num_three))

