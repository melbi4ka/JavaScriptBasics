def check_even(num):
    if num % 2 == 0:
        return True
    return False


number = input().split()
new_number = map(int, number)
even_numbers = filter(check_even, new_number)
print(list(even_numbers))
