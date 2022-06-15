def odd_even_func(num):
    even_sum = 0
    odd_sum = 0
    for k in num:
        if int(k) % 2 == 0:
            even_sum += int(k)
        else:
            odd_sum += int(k)
    return odd_sum, even_sum


number = list(input())
odd_numbers, even_numbers = odd_even_func(number)
print(f"Odd sum = {odd_numbers}, Even sum = {even_numbers}")