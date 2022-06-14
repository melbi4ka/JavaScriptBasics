def odd_even_func(num):
    even_sum = 0
    odd_sum = 0
    for k in num:
        m = int(k)
        if m % 2 == 0:
            even_sum += m
        else:
            odd_sum += m
    return odd_sum, even_sum


number = list(input())
odd_even = list(odd_even_func(number))
#print(odd_even)
print(f"Odd sum = {odd_even[0]}, Even sum = {odd_even[1]}")

