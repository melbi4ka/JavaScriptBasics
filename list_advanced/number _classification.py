def number_classification(nums):
    nums_list_positive = [str(n) for n in nums if n >= 0]
    nums_list_negative = [str(n) for n in nums if n < 0]
    nums_list_even = [str(n) for n in nums if n % 2 == 0]
    nums_list_odd = [str(n) for n in nums if n % 2 != 0]

    return f"Positive: {', '.join(nums_list_positive)}\n"\
           f"Negative: {', '.join(nums_list_negative)}\n"\
           f"Even: {', '.join(nums_list_even)}\n"\
           f"Odd: {', '.join(nums_list_odd)}"


numbers = [int(el) for el in input().split(", ")]
print(number_classification(numbers))
