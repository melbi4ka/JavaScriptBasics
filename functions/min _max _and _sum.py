def min_max_sum_function(nums):
    min_num = min(nums)
    max_num = max(nums)
    sum_num = sum(nums)
    return min_num, max_num, sum_num


numbers = list(map(int, input().split()))
minumal_num, maximal_num, sum_numbers = min_max_sum_function(numbers)
print(f"The minimum number is {minumal_num}")
print(f"The maximum number is {maximal_num}")
print(f"The sum number is: {sum_numbers}")
