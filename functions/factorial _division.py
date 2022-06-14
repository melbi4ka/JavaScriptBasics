from math import factorial

def factorial_division(num_one, num_two):
    factorial_one = factorial(num_one)
    factorial_two = factorial(num_two)
    division = factorial_one/factorial_two
    return f"{division:.2f}"


number_one = int(input())
number_two = int(input())
print(factorial_division(number_one, number_two))
